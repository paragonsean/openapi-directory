# AmazonDataLifecycleManager.CreateLifecyclePolicyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executionRoleArn** | **String** | The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy. | 
**description** | **String** | A description of the lifecycle policy. The characters ^[0-9A-Za-z _-]+$ are supported. | 
**state** | **String** | The desired activation state of the lifecycle policy after creation. | 
**policyDetails** | [**CreateLifecyclePolicyRequestPolicyDetails**](CreateLifecyclePolicyRequestPolicyDetails.md) |  | 
**tags** | **{String: String}** | The tags to apply to the lifecycle policy during creation. | [optional] 



## Enum: StateEnum


* `ENABLED` (value: `"ENABLED"`)

* `DISABLED` (value: `"DISABLED"`)




