

# PolicyProperties

Properties of a Policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdDate** | **OffsetDateTime** | The creation date of the policy. |  [optional] [readonly] |
|**description** | **String** | The description of the policy. |  [optional] |
|**evaluatorType** | [**EvaluatorTypeEnum**](#EvaluatorTypeEnum) | The evaluator type of the policy (i.e. AllowedValuesPolicy, MaxValuePolicy). |  [optional] |
|**factData** | **String** | The fact data of the policy. |  [optional] |
|**factName** | [**FactNameEnum**](#FactNameEnum) | The fact name of the policy (e.g. LabVmCount, LabVmSize, MaxVmsAllowedPerLab, etc. |  [optional] |
|**provisioningState** | **String** | The provisioning status of the resource. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the policy. |  [optional] |
|**threshold** | **String** | The threshold of the policy (i.e. a number for MaxValuePolicy, and a JSON array of values for AllowedValuesPolicy). |  [optional] |
|**uniqueIdentifier** | **String** | The unique immutable identifier of a resource (Guid). |  [optional] |



## Enum: EvaluatorTypeEnum

| Name | Value |
|---- | -----|
| ALLOWED_VALUES_POLICY | &quot;AllowedValuesPolicy&quot; |
| MAX_VALUE_POLICY | &quot;MaxValuePolicy&quot; |



## Enum: FactNameEnum

| Name | Value |
|---- | -----|
| USER_OWNED_LAB_VM_COUNT | &quot;UserOwnedLabVmCount&quot; |
| USER_OWNED_LAB_PREMIUM_VM_COUNT | &quot;UserOwnedLabPremiumVmCount&quot; |
| LAB_VM_COUNT | &quot;LabVmCount&quot; |
| LAB_PREMIUM_VM_COUNT | &quot;LabPremiumVmCount&quot; |
| LAB_VM_SIZE | &quot;LabVmSize&quot; |
| GALLERY_IMAGE | &quot;GalleryImage&quot; |
| USER_OWNED_LAB_VM_COUNT_IN_SUBNET | &quot;UserOwnedLabVmCountInSubnet&quot; |
| LAB_TARGET_COST | &quot;LabTargetCost&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



