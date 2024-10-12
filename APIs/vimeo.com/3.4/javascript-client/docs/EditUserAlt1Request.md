# Vimeo.EditUserAlt1Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bio** | **String** | The user&#39;s bio. | [optional] 
**contentFilter** | **[String]** | A list of values describing the content in this video. Find the full list in the [/contentratings](https://developer.vimeo.com/api/endpoints/videos#GET/contentratings) endpoint. You must provide a comma-separated list if you are using a query string or an array if you are using JSON. | [optional] 
**link** | **String** | The user&#39;s custom Vimeo URL slug. | [optional] 
**location** | **String** | The user&#39;s location. | [optional] 
**name** | **String** | The user&#39;s display name. | [optional] 
**password** | **String** | The default password for all future videos that this user uploads. To use this field, the &#x60;videos.privacy.view&#x60; field must be &#x60;password&#x60;. | [optional] 
**videos** | [**EditUserAlt1RequestVideos**](EditUserAlt1RequestVideos.md) |  | [optional] 


