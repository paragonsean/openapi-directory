# DevTestLabsClient.PolicyProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The description of the policy. | [optional] 
**evaluatorType** | **String** | The evaluator type of the policy. | [optional] 
**factData** | **String** | The fact data of the policy. | [optional] 
**factName** | **String** | The fact name of the policy. | [optional] 
**provisioningState** | **String** | The provisioning status of the resource. | [optional] 
**status** | **String** | The status of the policy. | [optional] 
**threshold** | **String** | The threshold of the policy. | [optional] 



## Enum: EvaluatorTypeEnum


* `AllowedValuesPolicy` (value: `"AllowedValuesPolicy"`)

* `MaxValuePolicy` (value: `"MaxValuePolicy"`)





## Enum: FactNameEnum


* `UserOwnedLabVmCount` (value: `"UserOwnedLabVmCount"`)

* `LabVmCount` (value: `"LabVmCount"`)

* `LabVmSize` (value: `"LabVmSize"`)

* `GalleryImage` (value: `"GalleryImage"`)

* `UserOwnedLabVmCountInSubnet` (value: `"UserOwnedLabVmCountInSubnet"`)





## Enum: StatusEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




