SETLOCAL enabledelayedexpansion
@echo off
SET ROOT=%~dp0/..

call %~dp0\resetvars > nul 2>nul
call python --version >nul 2>nul
IF NOT %ERRORLEVEL%==0 (
    ECHO You probably don't have the python interpreter installed. Please install it
    GOTO CHOOSE-INSTALL-PYTHON
) else (
    EXIT /b 0
)

:CHOOSE-INSTALL-PYTHON
CHOICE /C YN /M "Do you want me to install python interpreter v3.7.4 from https://www.python.org/?"
IF %ERRORLEVEL%==1 (
    GOTO CHECK-BEFORE-INSTALL
) else (
    Exit /b 1
)

:CHECK-BEFORE-INSTALL
    SET choco=0
    FOR /F "tokens=* USEBACKQ" %%F IN (`choco --confirm`) DO (
        SET var=%%F
    )
    IF NOT "x%var:Chocolatey=%"=="x%var%" (
        CHOICE /C YN /M "Choco was found on your machine. Should use it?"
        IF %ERRORLEVEL%==1 (
            SET choco=1
        )
    ) else (
        ECHO Unfortunately, you don't have Chocolatey. Install will be by conventional way.
    )
    IF "%choco%"==1 (
        GOTO CHOCO-INSTALL
    ) ELSE (
        GOTO DEFAULT-INSTALL
    )

:CHOCO-INSTALL
    ECHO installing python interpreter by choco...
    call choco install python3 >nul 2>nul
    GOTO AFTER-INSTALL

:DEFAULT-INSTALL
    IF NOT exist %ROOT%/%DOWNLOAD_FOLDER% mkdir %DOWNLOAD_FOLDER%
    IF NOT exist %ROOT%/%DOWNLOAD_FOLDER%/python-3.7.4-amd64.exe (
        ECHO Downloading python interpreter...
        call PowerShell -Command "(new-object net.webclient).DownloadFile('https://www.python.org/ftp/python/3.7.4/python-3.7.4-amd64.exe', './download/python-3.7.4-amd64.exe')"
    ) ELSE (
        ECHO You already have downloaded python interpreter. Skip download phase...
    )
    ECHO installing python interpreter...
    call %ROOT%/%DOWNLOAD_FOLDER%/python-3.7.4-amd64.exe /quiet PrependPath=1
    GOTO AFTER-INSTALL

:AFTER-INSTALL
    ECHO Updating path variables...
    call scripts\resetvars >nul 2>nul
    call python --version >nul 2>nul
    IF NOT %ERRORLEVEL%==0 (
        ECHO Sorry, something goes wrong
        Exit /b 1
    ) else (
        ECHO python successfully installed
    )