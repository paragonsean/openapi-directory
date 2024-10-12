# DevTestLabsClient.PolicyProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdDate** | **Date** | The creation date of the policy. | [optional] [readonly] 
**description** | **String** | The description of the policy. | [optional] 
**evaluatorType** | **String** | The evaluator type of the policy (i.e. AllowedValuesPolicy, MaxValuePolicy). | [optional] 
**factData** | **String** | The fact data of the policy. | [optional] 
**factName** | **String** | The fact name of the policy (e.g. LabVmCount, LabVmSize, MaxVmsAllowedPerLab, etc. | [optional] 
**provisioningState** | **String** | The provisioning status of the resource. | [optional] 
**status** | **String** | The status of the policy. | [optional] 
**threshold** | **String** | The threshold of the policy (i.e. a number for MaxValuePolicy, and a JSON array of values for AllowedValuesPolicy). | [optional] 
**uniqueIdentifier** | **String** | The unique immutable identifier of a resource (Guid). | [optional] 



## Enum: EvaluatorTypeEnum


* `AllowedValuesPolicy` (value: `"AllowedValuesPolicy"`)

* `MaxValuePolicy` (value: `"MaxValuePolicy"`)





## Enum: FactNameEnum


* `UserOwnedLabVmCount` (value: `"UserOwnedLabVmCount"`)

* `UserOwnedLabPremiumVmCount` (value: `"UserOwnedLabPremiumVmCount"`)

* `LabVmCount` (value: `"LabVmCount"`)

* `LabPremiumVmCount` (value: `"LabPremiumVmCount"`)

* `LabVmSize` (value: `"LabVmSize"`)

* `GalleryImage` (value: `"GalleryImage"`)

* `UserOwnedLabVmCountInSubnet` (value: `"UserOwnedLabVmCountInSubnet"`)

* `LabTargetCost` (value: `"LabTargetCost"`)





## Enum: StatusEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




