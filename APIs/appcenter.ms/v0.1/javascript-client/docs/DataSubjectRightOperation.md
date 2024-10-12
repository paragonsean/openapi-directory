# AppCenterClient.DataSubjectRightOperation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appId** | **String** | Application identifier if applicable | [optional] 
**context** | **String** | JSON object decribing what to delete (TODO - make separate definition?) | 
**operationId** | **String** | Unique operation identifier | 
**participant** | **String** | Participant to execute the response | 
**participantData** | **String** | String field to be used by participant for any intermediate statuses or data they need to save | [optional] 
**requestId** | **String** | Unique request identifier | 
**requestType** | **String** | Request type | 
**status** | **String** | Operation status | 



## Enum: RequestTypeEnum


* `Unsupported` (value: `"Unsupported"`)

* `Delete` (value: `"Delete"`)

* `Purge` (value: `"Purge"`)

* `UndoDelete` (value: `"UndoDelete"`)

* `Scheduled` (value: `"Scheduled"`)

* `AppDelete` (value: `"AppDelete"`)

* `AppPurge` (value: `"AppPurge"`)

* `AppUndoDelete` (value: `"AppUndoDelete"`)

* `Export` (value: `"Export"`)

* `CustomerAccountDelete` (value: `"CustomerAccountDelete"`)

* `CustomerAccountExport` (value: `"CustomerAccountExport"`)

* `CustomerUserDelete` (value: `"CustomerUserDelete"`)

* `CustomerUserExport` (value: `"CustomerUserExport"`)





## Enum: StatusEnum


* `None` (value: `"None"`)

* `Created` (value: `"Created"`)

* `Queued` (value: `"Queued"`)

* `InProgress` (value: `"InProgress"`)

* `Completed` (value: `"Completed"`)

* `Failed` (value: `"Failed"`)




