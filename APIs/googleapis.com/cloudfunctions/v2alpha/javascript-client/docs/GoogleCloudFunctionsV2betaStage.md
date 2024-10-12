# CloudFunctionsApi.GoogleCloudFunctionsV2betaStage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **String** | Message describing the Stage | [optional] 
**name** | **String** | Name of the Stage. This will be unique for each Stage. | [optional] 
**resource** | **String** | Resource of the Stage | [optional] 
**resourceUri** | **String** | Link to the current Stage resource | [optional] 
**state** | **String** | Current state of the Stage | [optional] 
**stateMessages** | [**[GoogleCloudFunctionsV2betaStateMessage]**](GoogleCloudFunctionsV2betaStateMessage.md) | State messages from the current Stage. | [optional] 



## Enum: NameEnum


* `NAME_UNSPECIFIED` (value: `"NAME_UNSPECIFIED"`)

* `ARTIFACT_REGISTRY` (value: `"ARTIFACT_REGISTRY"`)

* `BUILD` (value: `"BUILD"`)

* `SERVICE` (value: `"SERVICE"`)

* `TRIGGER` (value: `"TRIGGER"`)

* `SERVICE_ROLLBACK` (value: `"SERVICE_ROLLBACK"`)

* `TRIGGER_ROLLBACK` (value: `"TRIGGER_ROLLBACK"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `NOT_STARTED` (value: `"NOT_STARTED"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)

* `COMPLETE` (value: `"COMPLETE"`)




