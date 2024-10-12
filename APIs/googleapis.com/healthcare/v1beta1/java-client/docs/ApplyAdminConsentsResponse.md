

# ApplyAdminConsentsResponse

Response when all admin Consent resources in scope were processed and all affected resources were reindexed successfully. This structure will be included in the response when the operation finishes successfully.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**affectedResources** | **String** | The number of resources (including the Consent resources) that may have consent access change. |  [optional] |
|**consentApplySuccess** | **String** | If &#x60;validate_only&#x3D;false&#x60; in ApplyAdminConsentsRequest, this counter contains the number of Consent resources that were successfully applied. Otherwise, it is the number of Consent resources that are supported. |  [optional] |
|**failedResources** | **String** | The number of resources (including the Consent resources) that ApplyAdminConsents failed to re-index. |  [optional] |



