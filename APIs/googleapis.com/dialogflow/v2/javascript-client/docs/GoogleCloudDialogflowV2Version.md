# DialogflowApi.GoogleCloudDialogflowV2Version

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The creation time of this version. This field is read-only, i.e., it cannot be set by create and update methods. | [optional] [readonly] 
**description** | **String** | Optional. The developer-provided description of this version. | [optional] 
**name** | **String** | Output only. The unique identifier of this agent version. Supported formats: - &#x60;projects//agent/versions/&#x60; - &#x60;projects//locations//agent/versions/&#x60; | [optional] [readonly] 
**status** | **String** | Output only. The status of this version. This field is read-only and cannot be set by create and update methods. | [optional] [readonly] 
**versionNumber** | **Number** | Output only. The sequential number of this version. This field is read-only which means it cannot be set by create and update methods. | [optional] [readonly] 



## Enum: StatusEnum


* `VERSION_STATUS_UNSPECIFIED` (value: `"VERSION_STATUS_UNSPECIFIED"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)

* `READY` (value: `"READY"`)

* `FAILED` (value: `"FAILED"`)




