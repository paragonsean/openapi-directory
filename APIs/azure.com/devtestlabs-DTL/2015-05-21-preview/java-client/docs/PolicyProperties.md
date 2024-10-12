

# PolicyProperties

Properties of a Policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The description of the policy. |  [optional] |
|**evaluatorType** | [**EvaluatorTypeEnum**](#EvaluatorTypeEnum) | The evaluator type of the policy. |  [optional] |
|**factData** | **String** | The fact data of the policy. |  [optional] |
|**factName** | [**FactNameEnum**](#FactNameEnum) | The fact name of the policy. |  [optional] |
|**provisioningState** | **String** | The provisioning status of the resource. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the policy. |  [optional] |
|**threshold** | **String** | The threshold of the policy. |  [optional] |



## Enum: EvaluatorTypeEnum

| Name | Value |
|---- | -----|
| ALLOWED_VALUES_POLICY | &quot;AllowedValuesPolicy&quot; |
| MAX_VALUE_POLICY | &quot;MaxValuePolicy&quot; |



## Enum: FactNameEnum

| Name | Value |
|---- | -----|
| USER_OWNED_LAB_VM_COUNT | &quot;UserOwnedLabVmCount&quot; |
| LAB_VM_COUNT | &quot;LabVmCount&quot; |
| LAB_VM_SIZE | &quot;LabVmSize&quot; |
| GALLERY_IMAGE | &quot;GalleryImage&quot; |
| USER_OWNED_LAB_VM_COUNT_IN_SUBNET | &quot;UserOwnedLabVmCountInSubnet&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



