

# AlgorithmRulesRule

Set of conditions. The return value of the rule is either: * The return value for single met condition or * The defined default return value if no conditions are met.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conditions** | [**List&lt;AlgorithmRulesRuleCondition&gt;**](AlgorithmRulesRuleCondition.md) | List of conditions in this rule. The criteria among conditions should be mutually exclusive. |  [optional] |
|**defaultReturnValue** | [**AlgorithmRulesSignalValue**](AlgorithmRulesSignalValue.md) |  |  [optional] |



