class Translation(object):
    START_TEXT = """Salom {},
Men CC-URL Uploader man!
Siz bu bot orqali HTTP/HTTPS linklarni yuklashingiz mumkin!

to`liq malumot uchun /help buyrug`ini yuboring!"""
    FORMAT_SELECTION = "Kerakli formatni tanlang: <a href='{}'>fayl hajmi taxminiy bo‘lishi mumkin</a> \nAgar maxsus eskiz o‘rnatmoqchi bo‘lsangiz, quyidagi tugmalardan birini bosishdan oldin yoki keyin tezda surat yuboring.\nSiz foydalanishingiz mumkin Avtomatik yaratilgan eskizni o'chirish uchun /deletethumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """Agar siz premium videolarni yuklab olishni istasangiz, quyidagi formatda taqdim eting:
URL | filename | username | password"""
    DOWNLOAD_START = "Olinyabdi.."
    UPLOAD_START = "Yuklanyabdi.."
    RCHD_TG_API_LIMIT = " {} sekundda yuklandi .\nYuklangan fayl hajmi: {}\nUzr. Lekin, Telegram API cheklovlari tufayli 2 GB dan katta fayllarni yuklay olmayman."
    AFTER_SUCCESSFUL_UPLOAD_MSG = " @cc_upload_bot botini ishlatganingiz uchun rahmat)"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = " {} sekundda olindi.\n {} sekundda yuklandi.\n\n@cc_upload_bot"
    SAVED_CUSTOM_THUMB_NAIL = "Maxsus video/fayl eskizi saqlandi. Ushbu rasm video/faylda ishlatiladi."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Maxsus eskiz muvaffaqiyatli tozalandi."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    HELP_USER = """How to Use Me? Follow These steps!
    
1. Send url (example.domain/File.mp4 | New Filename.mp4).
2. Send Image As Custom Thumbnail (Optional).
3. Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File (video) as file with Screenshots
   Video  - Give File as video without Screenshots
   File   - Give File without Screenshots

If bot didn't respond, contact @Close_Coder"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
You can use /rename command after receiving file to rename it with custom thumbnail support.
"""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
