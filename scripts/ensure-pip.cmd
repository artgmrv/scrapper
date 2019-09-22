SETLOCAL enabledelayedexpansion
@echo off
SET ROOT=%~dp0/..

call pip --version >nul 2>nul
IF NOT %ERRORLEVEL% == 0  (
    ECHO You probably don't have pip installed.
    GOTO INSTALL-PIP
) else (
    GOTO END
)

:INSTALL-PIP
    CHOICE /C YN /M "Do you want me to install pip?"
    IF %ERRORLEVEL%==1 (
        ECHO Trying to install pip...
        IF NOT exist %DOWNLOAD_FOLDER% mkdir %DOWNLOAD_FOLDER%
        IF NOT exist %ROOT%/%DOWNLOAD_FOLDER%/get-pip.py (
            ECHO Downloading file from https://bootstrap.pypa.io/get-pip.py...
            call PowerShell -Command "(new-object net.webclient).DownloadFile('https://bootstrap.pypa.io/get-pip.py', './download/get-pip.py')"
        ) else (
            ECHO get-pip.py already exist. Skip download phase...
        )
        ECHO Installing pip...
        call python %ROOT%\download\get-pip.py >nul 2>nul
        GOTO FINISH-CHECK
    ) else (
        ECHO Exit from script...
        EXIT /b 1
    )

:FINISH-CHECK
    call %~dp0\resetvars >nul 2>nul
    call pip --version >nul 2>nul
    IF NOT %ERRORLEVEL% == 0 (
        ECHO Sorry, something goes wrong. Please execute "python get-pip.py" after downloading pip manually from https://bootstrap.pypa.io/get-pip.py
        EXIT /b 1
    )

:END