

# GoogleCloudPolicysimulatorV1betaGenerateOrgPolicyViolationsPreviewOperationMetadata

GenerateOrgPolicyViolationsPreviewOperationMetadata is metadata about an OrgPolicyViolationsPreview generations operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requestTime** | **String** | Time when the request was received. |  [optional] |
|**resourcesFound** | **Integer** | Total number of resources that need scanning. Should equal resource_scanned + resources_pending |  [optional] |
|**resourcesPending** | **Integer** | Number of resources still to scan. |  [optional] |
|**resourcesScanned** | **Integer** | Number of resources already scanned. |  [optional] |
|**startTime** | **String** | Time when the request started processing, i.e. when the state was set to RUNNING. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The current state of the operation. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;PREVIEW_STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PREVIEW_PENDING&quot; |
| RUNNING | &quot;PREVIEW_RUNNING&quot; |
| SUCCEEDED | &quot;PREVIEW_SUCCEEDED&quot; |
| FAILED | &quot;PREVIEW_FAILED&quot; |



