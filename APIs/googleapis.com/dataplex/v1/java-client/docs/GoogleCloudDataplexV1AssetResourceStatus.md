

# GoogleCloudDataplexV1AssetResourceStatus

Status of the resource referenced by an asset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**managedAccessIdentity** | **String** | Output only. Service account associated with the BigQuery Connection. |  [optional] [readonly] |
|**message** | **String** | Additional information about the current state. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The current state of the managed resource. |  [optional] |
|**updateTime** | **String** | Last update time of the status. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| READY | &quot;READY&quot; |
| ERROR | &quot;ERROR&quot; |



