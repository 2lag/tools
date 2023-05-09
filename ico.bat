@echo off
setlocal enabledelayedexpansion

set "icon_file=C:\WINDOWS\System32\imageres.dll,8"
set /a "count=0"

for /d %%A in (*) do (
    if exist "%%A\desktop.ini" (
        echo Skipping: "%%A" - desktop.ini already exists.
    ) else (
        echo Creating: "%%A\desktop.ini"
        echo [.ShellClassInfo] > "%%A\desktop.ini"
        echo IconResource=!icon_file! >> "%%A\desktop.ini"
        echo [ViewState] >> "%%A\desktop.ini"
        echo Mode= >> "%%A\desktop.ini"
        echo Vid= >> "%%A\desktop.ini"
        echo FolderType=Generic >> "%%A\desktop.ini"
        attrib +S "%%A"
        attrib +H "%%A\desktop.ini"
        set /a "count+=1"
    )
)
echo %count% folder icons have been updated!
pause