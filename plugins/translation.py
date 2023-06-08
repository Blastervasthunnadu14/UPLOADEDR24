from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
🤗 𝐇𝐞𝐥𝐥𝐨 {}

𝐈 𝐀𝐦 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐔𝐑𝐋 𝐔𝐩𝐥𝐨𝐚𝐝𝐞𝐫 𝟐𝟒 𝐁𝐨𝐭.

**__𝐒𝐞𝐧𝐝 𝐦𝐞 𝐚 𝐝𝐢𝐫𝐞𝐜𝐭 𝐥𝐢𝐧𝐤 𝐚𝐧𝐝 𝐈 𝐰𝐢𝐥𝐥 𝐮𝐩𝐥𝐨𝐚𝐝 𝐢𝐭 𝐭𝐨 𝐭𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐚𝐬 𝐚 𝐟𝐢𝐥𝐞/𝐯𝐢𝐝𝐞𝐨..__**

**𝐔𝐬𝐞 𝐇𝐞𝐥𝐩 𝐁𝐮𝐭𝐭𝐨𝐧 𝐓𝐨 𝐊𝐧𝐨𝐰 𝐇𝐨𝐰 𝐓𝐨 𝐔𝐬𝐞 𝐌𝐞**
"""
    HELP_TEXT = """
𒊹︎︎︎ 𝐇𝐨𝐰 𝐓𝐨 𝐔𝐩𝐥𝐨𝐚𝐝 𝐅𝐢𝐥𝐞 𝐎𝐫 𝐌𝐞𝐝𝐢𝐚 

➪ 𝐒𝐞𝐧𝐝 𝐘𝐨𝐮𝐫 𝐋𝐢𝐧𝐤 𝐅𝐨𝐫 𝐔𝐩𝐥𝐨𝐚𝐝 𝐅𝐢𝐥𝐞 𝐎𝐫 𝐌𝐞𝐝𝐢𝐚.

𒊹︎︎︎ 𝐇𝐨𝐰 𝐭𝐨 𝐬𝐞𝐭 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥

➪ 𝐒𝐞𝐧𝐝 𝐘𝐨𝐮𝐫 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐏𝐡𝐨𝐭𝐨 𝐀𝐧𝐝 𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭 𝐀𝐝𝐝𝐞𝐝 𝐘𝐨𝐮𝐫 𝐏𝐡𝐨𝐭𝐨.

𒊹︎︎︎ 𝐇𝐨𝐰 𝐓𝐨 𝐃𝐞𝐥𝐞𝐭𝐢𝐧𝐠 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥

➪ 𝐒𝐞𝐧𝐝 /delthumb 𝐓𝐨 𝐃𝐞𝐥𝐞𝐭𝐞 𝐘𝐨𝐮𝐫 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥.

𒊹︎︎︎ 𝐇𝐨𝐰 𝐓𝐨 𝐒𝐡𝐨𝐰 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 

➪ 𝐒𝐞𝐧𝐝 /showthumb 𝐓𝐨 𝐕𝐢𝐞𝐰 𝐂𝐮𝐬𝐭𝐨𝐦 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 
 
"""
    ABOUT_TEXT = """
**📛 𝐌𝐘 𝐍𝐀𝐌𝐄** : [𝐔𝐏𝐋𝐎𝐀𝐃𝐄𝐑 𝟐𝟒 𝐁𝐎𝐓 ✨](https://t.me/UPLOADER24BOT)

**❤️ 𝐕𝐄𝐑𝐒𝐈𝐎𝐍** : [2.3 🔥](https://t.me/UPLOADER24BOT)

**🎬 𝐂𝐇𝐀𝐍𝐍𝐄𝐋** : [Click This To Join Our Main Channel](https://t.me/Blaster_Originals)

**📢 𝐔𝐏𝐃𝐀𝐓𝐄𝐒** : [BLASTER ORIGINALS](https://t.me/Blaster_Support_Grouo)

**🧑🏻‍💻 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑** : [ANNA VACHADU 🤓💥](https://t.me/BlasterOriginals)

"""




    PROGRESS = """
🚀 Sᴘᴇᴇᴅ : {3}/s\n
✅ Dᴏɴᴇ : {1}\n
📁 Tᴏᴛᴀʟ Sɪᴢᴇ  : {2}\n
🕔 Tɪᴍᴇ : {4}\n
"""


    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⚙️Settings', callback_data='OpenSettings')
        ],[
        InlineKeyboardButton('🌟Help', callback_data='help'),
        InlineKeyboardButton('🧑🏻‍💻About', callback_data='about')
        ],[
        InlineKeyboardButton('⛔Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙Back', callback_data='home'),
        InlineKeyboardButton('🧑🏻‍💻About', callback_data='about')
        ],[
        InlineKeyboardButton('⛔Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙Back', callback_data='home'),
        InlineKeyboardButton('🌟Help', callback_data='help')
        ],[
        InlineKeyboardButton('🔒 Close', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
    TEXT = "sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴛᴏ sᴇᴛ ɪᴛ"
    IFLONG_FILE_NAME = " Only 64 characters can be named . "
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "<b>No preminum plans available in this bot </b>  /help for Details"
    FORMAT_SELECTION = "<b>Select Your Format 👇\n\n🎥 Video = Upload As Streamble\n\n📂 File =Upload As File\n\n🙋🏻 Powered By :</b> @Blaster_Originals"
    SET_CUSTOM_USERNAME_PASSWORD = """"""
    NOYES_URL = "@robot URL detected. Please use https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    DOWNLOAD_START = "📥 Downloading..."
    UPLOAD_START = "📤 Uploading.."
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = " OWNER : BLASTER 👌\nFor the List of Telegram Bots"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Dᴏᴡɴʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs.\n\nTʜᴀɴᴋs Fᴏʀ Usɪɴɢ Mᴇ\n\nUᴘʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs"
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    SAVED_CUSTOM_THUMB_NAIL = "Save Your Thumbnail ✔️"
    DEL_ETED_CUSTOM_THUMB_NAIL = "Save Your Thumbnail ✔️."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "Delete Your Thumbnail 😏."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Thumbnail 😴"
    NO_VOID_FORMAT_FOUND = "ERROR... <code>{}</code>"
    FILE_NOT_FOUND = "Error, File not Found!!"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    SOMETHING_WRONG = "<code>Something Wrong. Try again.</code>"
    REPLY_TO_DOC_GET_LINK = "Reply to a Telegram media to get High Speed Direct Download Link"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /ren with custom thumbnail support"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS for screenshot of that specific time."""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a Telegram media (MKV), to extract embedded streams"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "For the list of Telegram bots. "
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """This Bot full free"""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    FORCE_SUBSCRIBE_TEXT = "<code>Sorry Dear You Must Join My Updates Channel for using me 😌😉....</code>"
    BANNED_USER_TEXT = "<code>You are Banned!</code>"
    CHECK_LINK = "⚡️"

