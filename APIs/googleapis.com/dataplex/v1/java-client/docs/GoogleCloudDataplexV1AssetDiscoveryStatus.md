

# GoogleCloudDataplexV1AssetDiscoveryStatus

Status of discovery for an asset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lastRunDuration** | **String** | The duration of the last discovery run. |  [optional] |
|**lastRunTime** | **String** | The start time of the last discovery run. |  [optional] |
|**message** | **String** | Additional information about the current state. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The current status of the discovery feature. |  [optional] |
|**stats** | [**GoogleCloudDataplexV1AssetDiscoveryStatusStats**](GoogleCloudDataplexV1AssetDiscoveryStatusStats.md) |  |  [optional] |
|**updateTime** | **String** | Last update time of the status. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| SCHEDULED | &quot;SCHEDULED&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |
| PAUSED | &quot;PAUSED&quot; |
| DISABLED | &quot;DISABLED&quot; |



