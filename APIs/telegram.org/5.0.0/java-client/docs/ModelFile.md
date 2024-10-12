

# ModelFile

This object represents a file ready to be downloaded. The file can be downloaded via the link `https://api.telegram.org/file/bot<token>/<file_path>`. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling [getFile](https://core.telegram.org/bots/api/#getfile).  Maximum file size to download is 20 MB

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileId** | **String** | Identifier for this file, which can be used to download or reuse the file |  |
|**filePath** | **String** | *Optional*. File path. Use &#x60;https://api.telegram.org/file/bot&lt;token&gt;/&lt;file_path&gt;&#x60; to get the file. |  [optional] |
|**fileSize** | **Integer** | *Optional*. File size, if known |  [optional] |
|**fileUniqueId** | **String** | Unique identifier for this file, which is supposed to be the same over time and for different bots. Can&#39;t be used to download or reuse the file. |  |



