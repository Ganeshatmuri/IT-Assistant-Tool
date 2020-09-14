@ECHO OFF
Icacls "E:\C BACKUP\pytds\PycharmProjects\submission\cleanupdrive.bat" /grant Everyone:f
del /s /f /q %userprofile%\Recent\*.*

rd /s /q %userprofile%\Recent  
  
md %userprofile%\Recent 

del /s /f /q %windir%\Prefetch\*.*    

rd /s /q %windir%\Prefetch  
  
md %windir%\Prefetch 

del /s /f /q %windir%\temp\*.*

rd /s /q %windir%\temp    

md %windir%\temp 

del /s /f /q %USERPROFILE%\appdata\local\temp\*.*

rd /s /q %USERPROFILE%\appdata\local\temp    

md %USERPROFILE%\appdata\local\temp

del /s /f /q %windir%\SoftwareDistribution\Download\*.*

rd /s /q %windir%\SoftwareDistribution\Download 

md %windir%\SoftwareDistribution\Download 

del /s /q %systemdrive%\$Recycle.bin

forfiles -p "C:\Windows\Logs" -s -m *.log -d -90 -c "cmd /c del @PATH"


