

# GoogleCloudDatacatalogV1SerializedPolicyTag

A nested protocol buffer that represents a policy tag and all its descendants.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**childPolicyTags** | [**List&lt;GoogleCloudDatacatalogV1SerializedPolicyTag&gt;**](GoogleCloudDatacatalogV1SerializedPolicyTag.md) | Children of the policy tag, if any. |  [optional] |
|**description** | **String** | Description of the serialized policy tag. At most 2000 bytes when encoded in UTF-8. If not set, defaults to an empty description. |  [optional] |
|**displayName** | **String** | Required. Display name of the policy tag. At most 200 bytes when encoded in UTF-8. |  [optional] |
|**policyTag** | **String** | Resource name of the policy tag. This field is ignored when calling &#x60;ImportTaxonomies&#x60;. |  [optional] |



