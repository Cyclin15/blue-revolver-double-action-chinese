@echo off
setlocal
set "DEST=%APPDATA%\blue-revolver-double-action"
if not exist "%DEST%" mkdir "%DEST%"
xcopy /Y /I /E "%~dp0userlocs" "%DEST%\userlocs"
if errorlevel 1 goto fail
xcopy /Y /I /E "%~dp0game" "%DEST%\game"
if errorlevel 1 goto fail
echo.
echo ---------------------------------------------
echo  Install OK.
echo  Launch the game, then select:
echo     OPTIONS -^> LANGUAGE -^> Chinese (zhong wen)
echo ---------------------------------------------
pause
exit /b 0
:fail
echo.
echo Install FAILED. Extract the whole zip first,
echo then run install.bat from the extracted folder.
pause
exit /b 1
