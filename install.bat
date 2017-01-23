@ECHO OFF
@REM Author: Jason Lim

SET sOURCE=%~dp0winlog\
SET DESTINATION="C:\Program Files\winlog"

@ECHO "Installing..."
@robocopy %SOURCE% %DESTINATION% /e

@SchTasks /Create /SC ONSTART /TN "winlog" /TR "D:\MiscProject\lokiLoggy\winlog\winlog.exe" /RL HIGHEST