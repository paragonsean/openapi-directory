

# OrgPolicyViolationInfo

Represents OrgPolicy Violation information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**payload** | **Map&lt;String, Object&gt;** | Optional. Resource payload that is currently in scope and is subjected to orgpolicy conditions. This payload may be the subset of the actual Resource that may come in the request. This payload should not contain any core content. |  [optional] |
|**resourceTags** | **Map&lt;String, String&gt;** | Optional. Tags referenced on the resource at the time of evaluation. These also include the federated tags, if they are supplied in the CheckOrgPolicy or CheckCustomConstraints Requests. Optional field as of now. These tags are the Cloud tags that are available on the resource during the policy evaluation and will be available as part of the OrgPolicy check response for logging purposes. |  [optional] |
|**resourceType** | **String** | Optional. Resource type that the orgpolicy is checked against. Example: compute.googleapis.com/Instance, store.googleapis.com/bucket |  [optional] |
|**violationInfo** | [**List&lt;ViolationInfo&gt;**](ViolationInfo.md) | Optional. Policy violations |  [optional] |



