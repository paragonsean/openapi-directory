# AmazonDataLifecycleManager.UpdateLifecyclePolicyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executionRoleArn** | **String** | The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy. | [optional] 
**state** | **String** | The desired activation state of the lifecycle policy after creation. | [optional] 
**description** | **String** | A description of the lifecycle policy. | [optional] 
**policyDetails** | [**CreateLifecyclePolicyRequestPolicyDetails**](CreateLifecyclePolicyRequestPolicyDetails.md) |  | [optional] 



## Enum: StateEnum


* `ENABLED` (value: `"ENABLED"`)

* `DISABLED` (value: `"DISABLED"`)




