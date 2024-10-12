# CloudDataplexApi.GoogleCloudDataplexV1AssetDiscoveryStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lastRunDuration** | **String** | The duration of the last discovery run. | [optional] 
**lastRunTime** | **String** | The start time of the last discovery run. | [optional] 
**message** | **String** | Additional information about the current state. | [optional] 
**state** | **String** | The current status of the discovery feature. | [optional] 
**stats** | [**GoogleCloudDataplexV1AssetDiscoveryStatusStats**](GoogleCloudDataplexV1AssetDiscoveryStatusStats.md) |  | [optional] 
**updateTime** | **String** | Last update time of the status. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `SCHEDULED` (value: `"SCHEDULED"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)

* `PAUSED` (value: `"PAUSED"`)

* `DISABLED` (value: `"DISABLED"`)




