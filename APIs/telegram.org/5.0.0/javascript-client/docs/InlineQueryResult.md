# TelegramBotApi.InlineQueryResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audioFileId** | **String** | A valid file identifier for the audio file | 
**caption** | **String** | *Optional*. Caption, 0-1024 characters after entities parsing | [optional] 
**captionEntities** | [**[MessageEntity]**](MessageEntity.md) | *Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode* | [optional] 
**id** | **String** | Unique identifier for this result, 1-64 bytes | 
**inputMessageContent** | [**InputMessageContent**](InputMessageContent.md) |  | 
**parseMode** | **String** | *Optional*. Mode for parsing entities in the voice message caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**replyMarkup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 
**type** | **String** | Type of the result, must be *voice* | 
**description** | **String** | *Optional*. Short description of the result | [optional] 
**documentFileId** | **String** | A valid file identifier for the file | 
**title** | **String** | Recording title | 
**gifFileId** | **String** | A valid file identifier for the GIF file | 
**mpeg4FileId** | **String** | A valid file identifier for the MP4 file | 
**photoFileId** | **String** | A valid file identifier of the photo | 
**stickerFileId** | **String** | A valid file identifier of the sticker | 
**videoFileId** | **String** | A valid file identifier for the video file | 
**voiceFileId** | **String** | A valid file identifier for the voice message | 
**hideUrl** | **Boolean** | *Optional*. Pass *True*, if you don&#39;t want the URL to be shown in the message | [optional] 
**thumbHeight** | **Number** | *Optional*. Thumbnail height | [optional] 
**thumbUrl** | **String** | URL of the thumbnail (jpeg only) for the video | 
**thumbWidth** | **Number** | *Optional*. Thumbnail width | [optional] 
**url** | **String** | *Optional*. URL of the result | [optional] 
**audioDuration** | **Number** | *Optional*. Audio duration in seconds | [optional] 
**audioUrl** | **String** | A valid URL for the audio file | 
**performer** | **String** | *Optional*. Performer | [optional] 
**firstName** | **String** | Contact&#39;s first name | 
**lastName** | **String** | *Optional*. Contact&#39;s last name | [optional] 
**phoneNumber** | **String** | Contact&#39;s phone number | 
**vcard** | **String** | *Optional*. Additional data about the contact in the form of a [vCard](https://en.wikipedia.org/wiki/VCard), 0-2048 bytes | [optional] 
**gameShortName** | **String** | Short name of the game | 
**documentUrl** | **String** | A valid URL for the file | 
**mimeType** | **String** | Mime type of the content of video url, “text/html” or “video/mp4” | 
**gifDuration** | **Number** | *Optional*. Duration of the GIF | [optional] 
**gifHeight** | **Number** | *Optional*. Height of the GIF | [optional] 
**gifUrl** | **String** | A valid URL for the GIF file. File size must not exceed 1MB | 
**gifWidth** | **Number** | *Optional*. Width of the GIF | [optional] 
**thumbMimeType** | **String** | *Optional*. MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. Defaults to “image/jpeg” | [optional] [default to &#39;image/jpeg&#39;]
**heading** | **Number** | *Optional*. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified. | [optional] 
**horizontalAccuracy** | **Number** | *Optional*. The radius of uncertainty for the location, measured in meters; 0-1500 | [optional] 
**latitude** | **Number** | Latitude of the venue location in degrees | 
**livePeriod** | **Number** | *Optional*. Period in seconds for which the location can be updated, should be between 60 and 86400. | [optional] 
**longitude** | **Number** | Longitude of the venue location in degrees | 
**proximityAlertRadius** | **Number** | *Optional*. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified. | [optional] 
**mpeg4Duration** | **Number** | *Optional*. Video duration | [optional] 
**mpeg4Height** | **Number** | *Optional*. Video height | [optional] 
**mpeg4Url** | **String** | A valid URL for the MP4 file. File size must not exceed 1MB | 
**mpeg4Width** | **Number** | *Optional*. Video width | [optional] 
**photoHeight** | **Number** | *Optional*. Height of the photo | [optional] 
**photoUrl** | **String** | A valid URL of the photo. Photo must be in **jpeg** format. Photo size must not exceed 5MB | 
**photoWidth** | **Number** | *Optional*. Width of the photo | [optional] 
**address** | **String** | Address of the venue | 
**foursquareId** | **String** | *Optional*. Foursquare identifier of the venue if known | [optional] 
**foursquareType** | **String** | *Optional*. Foursquare type of the venue, if known. (For example, “arts\\_entertainment/default”, “arts\\_entertainment/aquarium” or “food/icecream”.) | [optional] 
**googlePlaceId** | **String** | *Optional*. Google Places identifier of the venue | [optional] 
**googlePlaceType** | **String** | *Optional*. Google Places type of the venue. (See [supported types](https://developers.google.com/places/web-service/supported_types).) | [optional] 
**videoDuration** | **Number** | *Optional*. Video duration in seconds | [optional] 
**videoHeight** | **Number** | *Optional*. Video height | [optional] 
**videoUrl** | **String** | A valid URL for the embedded video player or video file | 
**videoWidth** | **Number** | *Optional*. Video width | [optional] 
**voiceDuration** | **Number** | *Optional*. Recording duration in seconds | [optional] 
**voiceUrl** | **String** | A valid URL for the voice recording | 



## Enum: ThumbMimeTypeEnum


* `image/jpeg` (value: `"image/jpeg"`)

* `image/gif` (value: `"image/gif"`)

* `video/mp4` (value: `"video/mp4"`)




