

# SoftwareUpdateConfigurationCollectionItemProperties

Software update configuration collection item properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **OffsetDateTime** | Creation time of the software update configuration, which only appears in the response. |  [optional] [readonly] |
|**frequency** | [**FrequencyEnum**](#FrequencyEnum) | Gets or sets the frequency of the schedule. |  [optional] |
|**lastModifiedTime** | **OffsetDateTime** | Last time software update configuration was modified, which only appears in the response. |  [optional] [readonly] |
|**nextRun** | **OffsetDateTime** | ext run time of the update. |  [optional] |
|**provisioningState** | **String** | Provisioning state for the software update configuration, which only appears in the response. |  [optional] [readonly] |
|**startTime** | **OffsetDateTime** | the start time of the update. |  [optional] |
|**updateConfiguration** | [**CollectionItemUpdateConfiguration**](CollectionItemUpdateConfiguration.md) |  |  [optional] |



## Enum: FrequencyEnum

| Name | Value |
|---- | -----|
| ONE_TIME | &quot;OneTime&quot; |
| DAY | &quot;Day&quot; |
| HOUR | &quot;Hour&quot; |
| WEEK | &quot;Week&quot; |
| MONTH | &quot;Month&quot; |
| MINUTE | &quot;Minute&quot; |



