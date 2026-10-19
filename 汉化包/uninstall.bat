@echo off
setlocal
rem All work is done in one PowerShell command so this .bat stays pure ASCII
rem (the Chinese filename is built from char codes, immune to codepage issues).
powershell -NoProfile -Command "$d=\"$env:APPDATA\blue-revolver-double-action\"; $f=$d+'brda_config.json'; if(Test-Path $f){$t=[IO.File]::ReadAllText($f); $t=$t -replace '\"language\"\s*:\s*\"[^\"]*\"','\"language\": \"english\"'; [IO.File]::WriteAllText($f,$t,(New-Object Text.UTF8Encoding($false)))}; Remove-Item -LiteralPath ($d+'userlocs\'+[char]20013+[char]25991+'.json') -ErrorAction SilentlyContinue; Remove-Item -LiteralPath ($d+'game\fonts.lua') -ErrorAction SilentlyContinue; if((Test-Path ($d+'game')) -and -not (Get-ChildItem -LiteralPath ($d+'game') -Recurse -File)){Remove-Item -LiteralPath ($d+'game') -Recurse -Force}; Write-Host ''; Write-Host 'Localization removed.'"
pause
