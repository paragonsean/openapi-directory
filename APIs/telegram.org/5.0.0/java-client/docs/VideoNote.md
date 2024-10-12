

# VideoNote

This object represents a [video message](https://telegram.org/blog/video-messages-and-telescope) (available in Telegram apps as of [v.4.0](https://telegram.org/blog/video-messages-and-telescope)).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**duration** | **Integer** | Duration of the video in seconds as defined by sender |  |
|**fileId** | **String** | Identifier for this file, which can be used to download or reuse the file |  |
|**fileSize** | **Integer** | *Optional*. File size |  [optional] |
|**fileUniqueId** | **String** | Unique identifier for this file, which is supposed to be the same over time and for different bots. Can&#39;t be used to download or reuse the file. |  |
|**length** | **Integer** | Video width and height (diameter of the video message) as defined by sender |  |
|**thumb** | [**PhotoSize**](PhotoSize.md) |  |  [optional] |



