# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1alphaDataRetentionSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eventDataRetention** | **String** | The length of time that event-level data is retained. | [optional] 
**name** | **String** | Output only. Resource name for this DataRetentionSetting resource. Format: properties/{property}/dataRetentionSettings | [optional] [readonly] 
**resetUserDataOnNewActivity** | **Boolean** | If true, reset the retention period for the user identifier with every event from that user. | [optional] 



## Enum: EventDataRetentionEnum


* `RETENTION_DURATION_UNSPECIFIED` (value: `"RETENTION_DURATION_UNSPECIFIED"`)

* `TWO_MONTHS` (value: `"TWO_MONTHS"`)

* `FOURTEEN_MONTHS` (value: `"FOURTEEN_MONTHS"`)

* `TWENTY_SIX_MONTHS` (value: `"TWENTY_SIX_MONTHS"`)

* `THIRTY_EIGHT_MONTHS` (value: `"THIRTY_EIGHT_MONTHS"`)

* `FIFTY_MONTHS` (value: `"FIFTY_MONTHS"`)




