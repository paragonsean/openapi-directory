

# GoogleCloudDatacatalogV1SerializedTaxonomy

A nested protocol buffer that represents a taxonomy and the hierarchy of its policy tags. Used for taxonomy replacement, import, and export.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activatedPolicyTypes** | [**List&lt;ActivatedPolicyTypesEnum&gt;**](#List&lt;ActivatedPolicyTypesEnum&gt;) | A list of policy types that are activated per taxonomy. |  [optional] |
|**description** | **String** | Description of the serialized taxonomy. At most 2000 bytes when encoded in UTF-8. If not set, defaults to an empty description. |  [optional] |
|**displayName** | **String** | Required. Display name of the taxonomy. At most 200 bytes when encoded in UTF-8. |  [optional] |
|**policyTags** | [**List&lt;GoogleCloudDatacatalogV1SerializedPolicyTag&gt;**](GoogleCloudDatacatalogV1SerializedPolicyTag.md) | Top level policy tags associated with the taxonomy, if any. |  [optional] |



## Enum: List&lt;ActivatedPolicyTypesEnum&gt;

| Name | Value |
|---- | -----|
| POLICY_TYPE_UNSPECIFIED | &quot;POLICY_TYPE_UNSPECIFIED&quot; |
| FINE_GRAINED_ACCESS_CONTROL | &quot;FINE_GRAINED_ACCESS_CONTROL&quot; |



