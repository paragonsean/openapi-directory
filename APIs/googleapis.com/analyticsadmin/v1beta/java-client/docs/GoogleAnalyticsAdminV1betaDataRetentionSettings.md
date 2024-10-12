

# GoogleAnalyticsAdminV1betaDataRetentionSettings

Settings values for data retention. This is a singleton resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventDataRetention** | [**EventDataRetentionEnum**](#EventDataRetentionEnum) | The length of time that event-level data is retained. |  [optional] |
|**name** | **String** | Output only. Resource name for this DataRetentionSetting resource. Format: properties/{property}/dataRetentionSettings |  [optional] [readonly] |
|**resetUserDataOnNewActivity** | **Boolean** | If true, reset the retention period for the user identifier with every event from that user. |  [optional] |



## Enum: EventDataRetentionEnum

| Name | Value |
|---- | -----|
| RETENTION_DURATION_UNSPECIFIED | &quot;RETENTION_DURATION_UNSPECIFIED&quot; |
| TWO_MONTHS | &quot;TWO_MONTHS&quot; |
| FOURTEEN_MONTHS | &quot;FOURTEEN_MONTHS&quot; |
| TWENTY_SIX_MONTHS | &quot;TWENTY_SIX_MONTHS&quot; |
| THIRTY_EIGHT_MONTHS | &quot;THIRTY_EIGHT_MONTHS&quot; |
| FIFTY_MONTHS | &quot;FIFTY_MONTHS&quot; |



