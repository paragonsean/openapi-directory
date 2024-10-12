

# EnterpriseChannelProperties

The parameters to provide for the Enterprise Channel.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nodes** | [**List&lt;EnterpriseChannelNode&gt;**](EnterpriseChannelNode.md) | The nodes associated with the Enterprise Channel. |  |
|**state** | [**StateEnum**](#StateEnum) | The current state of the Enterprise Channel. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| CREATE_FAILED | &quot;CreateFailed&quot; |
| STARTED | &quot;Started&quot; |
| STARTING | &quot;Starting&quot; |
| START_FAILED | &quot;StartFailed&quot; |
| STOPPED | &quot;Stopped&quot; |
| STOPPING | &quot;Stopping&quot; |
| STOP_FAILED | &quot;StopFailed&quot; |
| DELETING | &quot;Deleting&quot; |
| DELETE_FAILED | &quot;DeleteFailed&quot; |



