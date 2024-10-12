

# ServerAction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Server trigger unique identifier. |  [optional] |
|**name** | **String** | Name for server action. |  [optional] |
|**operation** | [**OperationEnum**](#OperationEnum) | Manage server state. Starting a server changes state from Pending to Running. Terminating a server changes state from Running to Terminated. If the action results in Error, status will change to Error.  |  [optional] |
|**webhook** | [**Webhook**](Webhook.md) |  |  [optional] |



## Enum: OperationEnum

| Name | Value |
|---- | -----|
| START | &quot;start&quot; |
| STOP | &quot;stop&quot; |
| TERMINATE | &quot;terminate&quot; |



