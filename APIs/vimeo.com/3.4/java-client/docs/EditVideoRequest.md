

# EditVideoRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentRating** | **List&lt;String&gt;** | A list of values describing the content in this video. You can find the full list in the [&#x60;/contentratings&#x60;](https://developer.vimeo.com/api/endpoints/videos#GET/contentratings) endpoint. |  [optional] |
|**description** | **String** | The new description of the video. |  [optional] |
|**embed** | [**UploadVideoAlt1RequestEmbed**](UploadVideoAlt1RequestEmbed.md) |  |  [optional] |
|**license** | [**LicenseEnum**](#LicenseEnum) | The Creative Commons license. |  [optional] |
|**locale** | **String** | The video&#39;s default language. For a full list of valid languages, use the [/languages?filter&#x3D;texttracks](https://developer.vimeo.com/api/endpoints/videos#GET/languages) endpoint. |  [optional] |
|**name** | **String** | The new title for the video. |  [optional] |
|**password** | **String** | The password. When you set &#x60;privacy.view&#x60; to &#x60;password&#x60;, you must provide the password as an additional parameter. |  [optional] |
|**privacy** | [**EditVideoRequestPrivacy**](EditVideoRequestPrivacy.md) |  |  [optional] |
|**ratings** | [**UploadVideoAlt1RequestRatings**](UploadVideoAlt1RequestRatings.md) |  |  [optional] |
|**reviewPage** | [**UploadVideoAlt1RequestReviewPage**](UploadVideoAlt1RequestReviewPage.md) |  |  [optional] |
|**spatial** | [**UploadVideoAlt1RequestSpatial**](UploadVideoAlt1RequestSpatial.md) |  |  [optional] |



## Enum: LicenseEnum

| Name | Value |
|---- | -----|
| BY | &quot;by&quot; |
| BY_NC | &quot;by-nc&quot; |
| BY_NC_ND | &quot;by-nc-nd&quot; |
| BY_NC_SA | &quot;by-nc-sa&quot; |
| BY_ND | &quot;by-nd&quot; |
| BY_SA | &quot;by-sa&quot; |
| CC0 | &quot;cc0&quot; |



