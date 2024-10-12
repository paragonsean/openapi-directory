

# GoogleApiServiceusageV2alphaConsumerPolicy

Consumer Policy is a set of rules that define what services or service groups can be used for a cloud resource hierarchy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotations** | **Map&lt;String, String&gt;** | Optional. Annotations is an unstructured key-value map stored with a policy that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. [AIP-128](https://google.aip.dev/128#annotations) |  [optional] |
|**createTime** | **String** | Output only. The time the policy was created. For singleton policies, this is the first touch of the policy. |  [optional] [readonly] |
|**enableRules** | [**List&lt;GoogleApiServiceusageV2alphaEnableRule&gt;**](GoogleApiServiceusageV2alphaEnableRule.md) | Enable rules define usable services, groups, and categories. There can currently be at most one &#x60;EnableRule&#x60;. This restriction will be lifted in later releases. |  [optional] |
|**etag** | **String** | Output only. An opaque tag indicating the current version of the policy, used for concurrency control. |  [optional] [readonly] |
|**name** | **String** | Output only. The resource name of the policy. Only the &#x60;default&#x60; policy is supported: &#x60;projects/12345/consumerPolicies/default&#x60;, &#x60;folders/12345/consumerPolicies/default&#x60;, &#x60;organizations/12345/consumerPolicies/default&#x60;. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The time the policy was last updated. |  [optional] [readonly] |



