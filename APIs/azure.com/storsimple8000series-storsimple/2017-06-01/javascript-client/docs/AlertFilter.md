# StorSimple8000SeriesManagementClient.AlertFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appearedOnTime** | **Date** | Specifies the appeared time (in UTC) of the alerts to be filtered. Only &#39;Greater-Than&#39; and &#39;Lesser-Than&#39; operators are supported for this property. | [optional] 
**severity** | **String** | Specifies the severity of the alerts to be filtered. Only &#39;Equality&#39; operator is supported for this property. | [optional] 
**sourceName** | **String** | Specifies the source name of the alerts to be filtered. Only &#39;Equality&#39; operator is supported for this property. | [optional] 
**sourceType** | **String** | Specifies the source type of the alerts to be filtered. Only &#39;Equality&#39; operator is supported for this property. | [optional] 
**status** | **String** | Specifies the status of the alerts to be filtered. Only &#39;Equality&#39; operator is supported for this property. | [optional] 



## Enum: SeverityEnum


* `Informational` (value: `"Informational"`)

* `Warning` (value: `"Warning"`)

* `Critical` (value: `"Critical"`)





## Enum: SourceTypeEnum


* `Resource` (value: `"Resource"`)

* `Device` (value: `"Device"`)





## Enum: StatusEnum


* `Active` (value: `"Active"`)

* `Cleared` (value: `"Cleared"`)




