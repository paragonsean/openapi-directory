

# DataPolicy

Represents the label-policy binding.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataMaskingPolicy** | [**DataMaskingPolicy**](DataMaskingPolicy.md) |  |  [optional] |
|**dataPolicyId** | **String** | User-assigned (human readable) ID of the data policy that needs to be unique within a project. Used as {data_policy_id} in part of the resource name. |  [optional] |
|**dataPolicyType** | [**DataPolicyTypeEnum**](#DataPolicyTypeEnum) | Type of data policy. |  [optional] |
|**name** | **String** | Output only. Resource name of this data policy, in the format of &#x60;projects/{project_number}/locations/{location_id}/dataPolicies/{data_policy_id}&#x60;. |  [optional] [readonly] |
|**policyTag** | **String** | Policy tag resource name, in the format of &#x60;projects/{project_number}/locations/{location_id}/taxonomies/{taxonomy_id}/policyTags/{policyTag_id}&#x60;. |  [optional] |



## Enum: DataPolicyTypeEnum

| Name | Value |
|---- | -----|
| DATA_POLICY_TYPE_UNSPECIFIED | &quot;DATA_POLICY_TYPE_UNSPECIFIED&quot; |
| COLUMN_LEVEL_SECURITY_POLICY | &quot;COLUMN_LEVEL_SECURITY_POLICY&quot; |
| DATA_MASKING_POLICY | &quot;DATA_MASKING_POLICY&quot; |



