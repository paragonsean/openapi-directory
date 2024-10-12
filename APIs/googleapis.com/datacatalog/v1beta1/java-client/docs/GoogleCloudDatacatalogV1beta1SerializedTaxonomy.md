

# GoogleCloudDatacatalogV1beta1SerializedTaxonomy

Message capturing a taxonomy and its policy tag hierarchy as a nested proto. Used for taxonomy import/export and mutation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activatedPolicyTypes** | [**List&lt;ActivatedPolicyTypesEnum&gt;**](#List&lt;ActivatedPolicyTypesEnum&gt;) | A list of policy types that are activated for a taxonomy. |  [optional] |
|**description** | **String** | Description of the serialized taxonomy. The length of the description is limited to 2000 bytes when encoded in UTF-8. If not set, defaults to an empty description. |  [optional] |
|**displayName** | **String** | Required. Display name of the taxonomy. Max 200 bytes when encoded in UTF-8. |  [optional] |
|**policyTags** | [**List&lt;GoogleCloudDatacatalogV1beta1SerializedPolicyTag&gt;**](GoogleCloudDatacatalogV1beta1SerializedPolicyTag.md) | Top level policy tags associated with the taxonomy if any. |  [optional] |



## Enum: List&lt;ActivatedPolicyTypesEnum&gt;

| Name | Value |
|---- | -----|
| POLICY_TYPE_UNSPECIFIED | &quot;POLICY_TYPE_UNSPECIFIED&quot; |
| FINE_GRAINED_ACCESS_CONTROL | &quot;FINE_GRAINED_ACCESS_CONTROL&quot; |



