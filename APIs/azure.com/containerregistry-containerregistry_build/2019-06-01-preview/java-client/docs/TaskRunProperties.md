

# TaskRunProperties

The properties of task run.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**forceUpdateTag** | **String** | How the run should be forced to rerun even if the run request configuration has not changed |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state of this task run |  [optional] [readonly] |
|**runRequest** | [**RunRequest**](RunRequest.md) |  |  [optional] |
|**runResult** | [**Run**](Run.md) |  |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



