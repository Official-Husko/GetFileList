# GetFileList
With this tool you can easily generate a list of all folders and files in a target directory. Simply enter the path to your target folder and it will do the rest. To get a simple list just run the compiled exe or the python file directly. If you want to use advanced options use a cmd/wt window.
  
The Wiki can be found [here][1]

#
### Available Commands for Advanced Usage
```r
usage: GetFileList.exe [options]

options:
  -h, --help            show this help message and exit
  -p PATH_TO_TARGET, --path PATH_TO_TARGET
                        Path to Target
  -f FILE_FORMAT, --format FILE_FORMAT
                        output format. plain & json supported
  -hf CALCULATE_HASHES, --hash CALCULATE_HASHES
                        calculate the hashes for all files. CRC32 only currently
  -ext FILE_ENDING, --extention FILE_ENDING
                        choose a prefered output extension e.g. log, txt
```

#
### Basic Example Output
*GetFileList Report - 30-04-2022 18-43-19.log*
```r
==================================
Generated using GetFileList by Husko ~ The right way to get & share a file list.
Source: https://github.com/Official-Husko/GetFileList
This report was generated at: 30/04/2022 18:42:58
==================================



==================================
General Information
==================================
Directory Name: GetFileList
Directory Path: Z:\Projects\Python\GetFileList
File Count: 6
Directory Count: 1



==================================
Present Directories
==================================
[FOLDER] .git



==================================
Present Files
==================================
[FILE] Build Release.bat
[FILE] Clean Folder.bat
[FILE] icon.ico
[FILE] LICENCE
[FILE] main.py
[FILE] README.md

```

#
#### Disclaimer  
***This Tool is licensed under [GPL][2].***  


[1]:https://github.com/Official-Husko/GetFileList/wiki
[2]:https://github.com/Official-Husko/Husko-s-SteamWorkshop-Downloader/blob/stable/LICENSE