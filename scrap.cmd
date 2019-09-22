@echo off

SET ENV_FOLDER=venv
SET DOWNLOAD_FOLDER=download

call scripts\ensure-python
if NOT %ERRORLEVEL% == 0 (
    ECHO Error in ensure-python phase
    EXIT /b 1
)

call scripts\ensure-pip
if NOT %ERRORLEVEL% == 0 (
    ECHO Error in ensure-pip phase
    EXIT /b 1
)
call %~dp0\scripts\resetvars >nul 2>nul

call virtualenv --version >nul 2>nul
IF NOT %ERRORLEVEL% == 0  (
    ECHO Where is no virtualenv package. Installing...
    call pip install virtualenv
    EXIT /b 1
)

IF NOT EXIST %ENV_FOLDER% (
    ECHO installing virtual environtment...
    call virtualenv %ENV_FOLDER% >nul 2>nul
    ECHO installing packages
    call %ENV_FOLDER%\scripts\activate
    pip install -r requirements.txt >nul 2>nul
    call deactivate
)
call env\scripts\activate
call python scrap.py %*
call deactivate