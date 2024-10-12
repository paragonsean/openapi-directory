

# PassportFile

This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileDate** | **Integer** | Unix time when the file was uploaded |  |
|**fileId** | **String** | Identifier for this file, which can be used to download or reuse the file |  |
|**fileSize** | **Integer** | File size |  |
|**fileUniqueId** | **String** | Unique identifier for this file, which is supposed to be the same over time and for different bots. Can&#39;t be used to download or reuse the file. |  |



