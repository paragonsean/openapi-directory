# Vimeo.UploadVideoAlt1Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentRating** | **[String]** | A list of values describing the content in this video. Find the full list in the [/contentratings](https://developer.vimeo.com/api/endpoints/videos#GET/contentratings) endpoint. | [optional] 
**description** | **String** | The description of the video. | [optional] 
**embed** | [**UploadVideoAlt1RequestEmbed**](UploadVideoAlt1RequestEmbed.md) |  | [optional] 
**license** | **String** | The Creative Commons license. | [optional] 
**locale** | **String** | The video&#39;s default language. For a full list of valid languages, use the [/languages?filter&#x3D;texttracks](https://developer.vimeo.com/api/endpoints/videos#GET/languages) endpoint. | [optional] 
**name** | **String** | The title of the video. | [optional] 
**password** | **String** | The password. When you set &#x60;privacy.view&#x60; to &#x60;password&#x60;, you must provide the password as an additional parameter. | [optional] 
**privacy** | [**UploadVideoAlt1RequestPrivacy**](UploadVideoAlt1RequestPrivacy.md) |  | [optional] 
**ratings** | [**UploadVideoAlt1RequestRatings**](UploadVideoAlt1RequestRatings.md) |  | [optional] 
**reviewPage** | [**UploadVideoAlt1RequestReviewPage**](UploadVideoAlt1RequestReviewPage.md) |  | [optional] 
**spatial** | [**UploadVideoAlt1RequestSpatial**](UploadVideoAlt1RequestSpatial.md) |  | [optional] 
**upload** | [**UploadVideoAlt1RequestUpload**](UploadVideoAlt1RequestUpload.md) |  | 



## Enum: LicenseEnum


* `by` (value: `"by"`)

* `by-nc` (value: `"by-nc"`)

* `by-nc-nd` (value: `"by-nc-nd"`)

* `by-nc-sa` (value: `"by-nc-sa"`)

* `by-nd` (value: `"by-nd"`)

* `by-sa` (value: `"by-sa"`)

* `cc0` (value: `"cc0"`)




