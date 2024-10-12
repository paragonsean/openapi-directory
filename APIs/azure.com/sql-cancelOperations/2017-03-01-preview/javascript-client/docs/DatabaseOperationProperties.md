# SqlManagementClient.DatabaseOperationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**databaseName** | **String** | The name of the database the operation is being performed on. | [optional] [readonly] 
**description** | **String** | The operation description. | [optional] [readonly] 
**errorCode** | **Number** | The operation error code. | [optional] [readonly] 
**errorDescription** | **String** | The operation error description. | [optional] [readonly] 
**errorSeverity** | **Number** | The operation error severity. | [optional] [readonly] 
**estimatedCompletionTime** | **Date** | The estimated completion time of the operation. | [optional] [readonly] 
**isCancellable** | **Boolean** | Whether the operation can be cancelled. | [optional] [readonly] 
**isUserError** | **Boolean** | Whether or not the error is a user error. | [optional] [readonly] 
**operation** | **String** | The name of operation. | [optional] [readonly] 
**operationFriendlyName** | **String** | The friendly name of operation. | [optional] [readonly] 
**percentComplete** | **Number** | The percentage of the operation completed. | [optional] [readonly] 
**serverName** | **String** | The name of the server. | [optional] [readonly] 
**startTime** | **Date** | The operation start time. | [optional] [readonly] 
**state** | **String** | The operation state. | [optional] [readonly] 



## Enum: StateEnum


* `Pending` (value: `"Pending"`)

* `InProgress` (value: `"InProgress"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `CancelInProgress` (value: `"CancelInProgress"`)

* `Cancelled` (value: `"Cancelled"`)




