

# GoogleChromePolicyVersionsV1PolicyModificationError

Error information for a modification request of a specific policy on a specific target.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errors** | **List&lt;String&gt;** | Output only. The non-field errors related to the modification. |  [optional] [readonly] |
|**fieldErrors** | [**List&lt;GoogleChromePolicyVersionsV1PolicyModificationFieldError&gt;**](GoogleChromePolicyVersionsV1PolicyModificationFieldError.md) | Output only. The error messages related to the modification. |  [optional] [readonly] |
|**policySchema** | **String** | Output only. The specific policy schema modification that had an error. |  [optional] [readonly] |
|**policyTargetKey** | [**GoogleChromePolicyVersionsV1PolicyTargetKey**](GoogleChromePolicyVersionsV1PolicyTargetKey.md) |  |  [optional] |



