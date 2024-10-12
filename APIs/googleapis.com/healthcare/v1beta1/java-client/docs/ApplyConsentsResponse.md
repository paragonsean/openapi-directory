

# ApplyConsentsResponse

Response when all Consent resources in scope were processed and all affected resources were reindexed successfully. This structure is included in the response when the operation finishes successfully.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**affectedResources** | **String** | The number of resources (including the Consent resources) that may have consensual access change. |  [optional] |
|**consentApplyFailure** | **String** | If &#x60;validate_only &#x3D; false&#x60; in ApplyConsentsRequest, this counter is the number of Consent resources that were failed to apply. Otherwise, it is the number of Consent resources that are not supported or invalid. |  [optional] |
|**consentApplySuccess** | **String** | If &#x60;validate_only &#x3D; false&#x60; in ApplyConsentsRequest, this counter is the number of Consent resources that were successfully applied. Otherwise, it is the number of Consent resources that are supported. |  [optional] |
|**failedResources** | **String** | The number of resources (including the Consent resources) that ApplyConsents failed to re-index. |  [optional] |



