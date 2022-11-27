Pushd "%~dp0"
::cd %~d0 "%~dp0"
@echo off
::%~d0
::%cd%
::D:
::cd D:\iRoot\home\programming\python\windows_host\PyWinHost
python processor.py
ipconfig/flushdns
pause
exit