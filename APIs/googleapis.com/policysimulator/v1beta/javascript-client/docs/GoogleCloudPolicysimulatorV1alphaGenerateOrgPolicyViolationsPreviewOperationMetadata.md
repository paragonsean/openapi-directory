# PolicySimulatorApi.GoogleCloudPolicysimulatorV1alphaGenerateOrgPolicyViolationsPreviewOperationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requestTime** | **String** | Time when the request was received. | [optional] 
**resourcesFound** | **Number** | Total number of resources that need scanning. Should equal resource_scanned + resources_pending | [optional] 
**resourcesPending** | **Number** | Number of resources still to scan. | [optional] 
**resourcesScanned** | **Number** | Number of resources already scanned. | [optional] 
**startTime** | **String** | Time when the request started processing, i.e. when the state was set to RUNNING. | [optional] 
**state** | **String** | The current state of the operation. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"PREVIEW_STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PREVIEW_PENDING"`)

* `RUNNING` (value: `"PREVIEW_RUNNING"`)

* `SUCCEEDED` (value: `"PREVIEW_SUCCEEDED"`)

* `FAILED` (value: `"PREVIEW_FAILED"`)




