# GoToWebinar.WebinarReqUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | A description of the webinar (2048 characters maximum) | [optional] 
**locale** | **String** | The webinar language | [optional] 
**subject** | **String** | The name/subject of the webinar (128 characters maximum) | [optional] 
**timeZone** | **String** | The time zone where the webinar is taking place (must be a valid time zone ID, see https://goto-developer.logmein.com/time-zones). If this parameter is not passed, the timezone of the organizer&#39;s profile will be used | [optional] 
**times** | [**[DateTimeRange]**](DateTimeRange.md) | Array with start and end time(s) for webinar | [optional] 



## Enum: LocaleEnum


* `en_US` (value: `"en_US"`)

* `de_DE` (value: `"de_DE"`)

* `es_ES` (value: `"es_ES"`)

* `fr_FR` (value: `"fr_FR"`)

* `it_IT` (value: `"it_IT"`)

* `zh_CN` (value: `"zh_CN"`)




