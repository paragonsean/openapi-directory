# IllumiDesk.ServerActionData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Name of server action. | [optional] 
**operation** | **String** | Manage server state. Starting a server changes state from Pending to Running. Terminating a server changes state from Running to Terminated. Stopping a server changes state from Running to Stopped. If the action results in Error, status will change to Error.  | [optional] 
**webhook** | [**Webhook**](Webhook.md) |  | [optional] 



## Enum: OperationEnum


* `start` (value: `"start"`)

* `stop` (value: `"stop"`)

* `terminate` (value: `"terminate"`)




