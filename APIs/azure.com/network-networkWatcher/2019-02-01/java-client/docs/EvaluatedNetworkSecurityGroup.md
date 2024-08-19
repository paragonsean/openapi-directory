

# EvaluatedNetworkSecurityGroup

Results of network security group evaluation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appliedTo** | **String** | Resource ID of nic or subnet to which network security group is applied. |  [optional] |
|**matchedRule** | [**MatchedRule**](MatchedRule.md) |  |  [optional] |
|**networkSecurityGroupId** | **String** | Network security group ID. |  [optional] |
|**rulesEvaluationResult** | [**List&lt;NetworkSecurityRulesEvaluationResult&gt;**](NetworkSecurityRulesEvaluationResult.md) | List of network security rules evaluation results. |  [optional] [readonly] |



