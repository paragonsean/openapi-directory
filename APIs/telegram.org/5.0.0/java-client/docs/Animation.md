

# Animation

This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**duration** | **Integer** | Duration of the video in seconds as defined by sender |  |
|**fileId** | **String** | Identifier for this file, which can be used to download or reuse the file |  |
|**fileName** | **String** | *Optional*. Original animation filename as defined by sender |  [optional] |
|**fileSize** | **Integer** | *Optional*. File size |  [optional] |
|**fileUniqueId** | **String** | Unique identifier for this file, which is supposed to be the same over time and for different bots. Can&#39;t be used to download or reuse the file. |  |
|**height** | **Integer** | Video height as defined by sender |  |
|**mimeType** | **String** | *Optional*. MIME type of the file as defined by sender |  [optional] |
|**thumb** | [**PhotoSize**](PhotoSize.md) |  |  [optional] |
|**width** | **Integer** | Video width as defined by sender |  |



