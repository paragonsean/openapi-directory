

# FileEntity

List Folders by path

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**crc32** | **String** | File CRC32 checksum. This is sometimes delayed, so if you get a blank response, wait and try again. |  [optional] |
|**createdAt** | **OffsetDateTime** | File created date/time |  [optional] |
|**displayName** | **String** | File/Folder display name |  [optional] |
|**downloadUri** | **String** | Link to download file. Provided only in response to a download request. |  [optional] |
|**isLocked** | **Boolean** | Is this folder locked and unable to be modified? |  [optional] |
|**md5** | **String** | File MD5 checksum. This is sometimes delayed, so if you get a blank response, wait and try again. |  [optional] |
|**mimeType** | **String** | MIME Type.  This is determined by the filename extension and is not stored separately internally. |  [optional] |
|**mtime** | **OffsetDateTime** | File last modified date/time, according to the server.  This is the timestamp of the last Files.com operation of the file, regardless of what modified timestamp was sent. |  [optional] |
|**path** | **String** | File/Folder path |  [optional] |
|**permissions** | **String** | A short string representing the current user&#39;s permissions.  Can be &#x60;r&#x60;,&#x60;w&#x60;,&#x60;d&#x60;, &#x60;l&#x60; or any combination |  [optional] |
|**preview** | [**PreviewEntity**](PreviewEntity.md) |  |  [optional] |
|**previewId** | **Integer** | File preview ID |  [optional] |
|**priorityColor** | **String** | Bookmark/priority color of file/folder |  [optional] |
|**providedMtime** | **OffsetDateTime** | File last modified date/time, according to the client who set it.  Files.com allows desktop, FTP, SFTP, and WebDAV clients to set modified at times.  This allows Desktop&lt;-&gt;Cloud syncing to preserve modified at times. |  [optional] |
|**region** | **String** | Region location |  [optional] |
|**size** | **Integer** | File/Folder size |  [optional] |
|**subfoldersLockedQuestionMark** | **Boolean** | Are subfolders locked and unable to be modified? |  [optional] |
|**type** | **String** | Type: &#x60;directory&#x60; or &#x60;file&#x60;. |  [optional] |



