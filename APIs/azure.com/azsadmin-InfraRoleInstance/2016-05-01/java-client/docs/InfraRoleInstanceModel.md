

# InfraRoleInstanceModel

All properties of an infrastructure role instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**scaleUnit** | **String** | The cluster that the virtual machine&#39;s host is part of. |  [optional] |
|**scaleUnitNode** | **String** | URI to the scale unit node. |  [optional] |
|**size** | [**InfraRoleInstanceSize**](InfraRoleInstanceSize.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The current state of the virtual machine. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STOPPED | &quot;Stopped&quot; |
| STARTING | &quot;Starting&quot; |
| RUNNING | &quot;Running&quot; |
| STOPPING | &quot;Stopping&quot; |



