ECHO

ECHO ****** clearing chrome cache

Taskkill /F /IM chrome.exe /T > nul

Set chromeDataDir=c:\users\%USERNAME%\Appdata\Local\Google\Chrome\user Data\Default

Set chromecache=%chromeDataDir%\cache

Del /s /f /q "%chromecache%\*.*"

Del /s /f /q "%chromeDataDir%\*cookies*.*"

Del /s /f /q "%chromeDataDir%\History*.*"

Set chromeDataDir=c:\users\%USERNAME%\Local settings\Application Data\Google\chrome\user Data\Default

Set chromecache="%chromeData%"\cache"

Del /s /f /q "%chromecache%\*.*"

Del /s /f /q "%chromeDataDir%\*cookies*.*"

Del /s /f /q "%chromeDataDir%\*History*.*"

ECHO ***** Clearing chrome cache done

