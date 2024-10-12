# HetznerCloudApi.NullableAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **String** | Command executed in the Action | 
**error** | [**ActionError**](ActionError.md) |  | 
**finished** | **String** | Point in time when the Action was finished (in ISO-8601 format). Only set if the Action is finished otherwise null. | 
**id** | **Number** | ID of the Resource | 
**progress** | **Number** | Progress of Action in percent | 
**resources** | [**[ActionResourcesInner]**](ActionResourcesInner.md) | Resources the Action relates to | 
**started** | **String** | Point in time when the Action was started (in ISO-8601 format) | 
**status** | **String** | Status of the Action | 



## Enum: StatusEnum


* `success` (value: `"success"`)

* `running` (value: `"running"`)

* `error` (value: `"error"`)




