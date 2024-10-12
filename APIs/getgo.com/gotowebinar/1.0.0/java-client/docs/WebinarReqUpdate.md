

# WebinarReqUpdate

Describes the details of the webinar

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A description of the webinar (2048 characters maximum) |  [optional] |
|**locale** | [**LocaleEnum**](#LocaleEnum) | The webinar language |  [optional] |
|**subject** | **String** | The name/subject of the webinar (128 characters maximum) |  [optional] |
|**timeZone** | **String** | The time zone where the webinar is taking place (must be a valid time zone ID, see https://goto-developer.logmein.com/time-zones). If this parameter is not passed, the timezone of the organizer&#39;s profile will be used |  [optional] |
|**times** | [**List&lt;DateTimeRange&gt;**](DateTimeRange.md) | Array with start and end time(s) for webinar |  [optional] |



## Enum: LocaleEnum

| Name | Value |
|---- | -----|
| EN_US | &quot;en_US&quot; |
| DE_DE | &quot;de_DE&quot; |
| ES_ES | &quot;es_ES&quot; |
| FR_FR | &quot;fr_FR&quot; |
| IT_IT | &quot;it_IT&quot; |
| ZH_CN | &quot;zh_CN&quot; |



