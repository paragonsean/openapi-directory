# ServiceUsageApi.ConsumerPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **{String: String}** | Optional. Annotations is an unstructured key-value map stored with a policy that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. [AIP-128](https://google.aip.dev/128#annotations) | [optional] 
**enableRules** | [**[EnableRule]**](EnableRule.md) | Enable rules define usable services and service groups. | [optional] 
**etag** | **String** | An opaque tag indicating the current version of the policy, used for concurrency control. | [optional] 
**name** | **String** | Output only. The resource name of the policy. We only allow consumer policy name as &#x60;default&#x60; for now: &#x60;projects/12345/consumerPolicies/default&#x60;, &#x60;folders/12345/consumerPolicies/default&#x60;, &#x60;organizations/12345/consumerPolicies/default&#x60;. | [optional] [readonly] 
**updateTime** | **String** | The last-modified time. | [optional] 


