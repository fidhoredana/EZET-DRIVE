<p align="center">
  <img src="https://raw.githubusercontent.com/fidhoredana/EZET-DRIVE/master/ezet-drive.PNG" alt="LOGO">
</p>



## ⚡ EZET-DRIVE.py ⚡
- Bulk download Google Drive by url using Python!✨
- LIGHT and FAST!!!
- Progress bar for each download process
- Downloaded files are stored with the same name on Google Drive
- Files with the same name from different URLs will remain and not be replaced
- Automatically re-download in case of failed download
- URLs that fail to download are stored in failed_url.txt
- Support multiple kind of Google Drive URLs
    - https://drive.google.com/uc?export=download&id=xxx
    - https://drive.google.com/file/d/xxx/view?usp=sharing
## How to use?

- Clone this repository
    
    `git clone https://github.com/fidhoredana/EZET-DRIVE`

- Go inside the folder
    
    `cd EZET-DRIVE`

- Edit `url.txt` with a list of urls to download with a *new line* as separator
    
    `nano url.txt`
    
    or if you prefer to use vi
    
    `vi url.txt`
    
    Example:

    ```bash
        https://drive.google.com/uc?export=download&id=1ZXAlXgCCFROtyqwd7pPPaTDDSq-4SD
        https://drive.google.com/uc?export=download&id=xxx
        https://drive.google.com/file/d/1ZXAlXgCCsdyqwd7pPPaTDDSq-4SD/view?usp=sharing
        https://drive.google.com/file/d/xxx/view?usp=sharing
    ```
- Run the EZET-DRIVE!
    
    `python3 EZET-DRIVE.py`


## Conclusion

[!] Wait until all downloads are complete

[!] If there is a url that fails to download, EZET-DRIVE will try to re-download 3 times, if it still doesn't work, then the URL that failed to download will be saved in `failed_url.txt`

[+] Files that have been successfully downloaded will be stored in the `Downloads` folder


## For the future feature?

Maybe I will make a proxy feature so that I can overcome failed downloads due to limits from Google Drive

## Thank You!

Reach me out on instagram [@fidho_redana](https://instagram.com/fidho_redana)
