

# UpdateAgentStatusRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the agent status. |  [optional] |
|**description** | **String** | The description of the agent status. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the agent status. |  [optional] |
|**displayOrder** | **Integer** | The display order of the agent status. |  [optional] |
|**resetOrderNumber** | **Boolean** | A number indicating the reset order of the agent status. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;ENABLED&quot; |
| DISABLED | &quot;DISABLED&quot; |



