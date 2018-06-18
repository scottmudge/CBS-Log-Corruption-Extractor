# CBS-Log-Corruption-Extractor

## What it Does

Extracts lines only containing "Repairing corrupted file" from CBS.log after running "sfc.exe /verifyonly"

## Why?

This is useful for checking if any files are corrupted in your windows installation without actually repairing the files. This is especially useful for those who have de-bloated many Windows 10 "features"/annoyances, and don't those to be repaired or recovered by using SFC.

## How to Use?

First run `SFC.exe /VerifyOnly` in an elevated command prompt to generate a CBS logfile in %WINDIR%/Logs/CBS/CBS.log.

Then simply run `python CBSFind.py` which will then generate a cbs_finder_out.txt file containing only strings which show system file corruptions (a small portion of the total CBS.log file).

## Releases:

You can download a pre-built binary (built with Pyinstaller) here:

https://github.com/scottmudge/CBS-Log-Corruption-Extractor/releases/tag/1.0

