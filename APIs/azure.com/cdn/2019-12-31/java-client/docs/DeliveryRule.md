

# DeliveryRule

A rule that specifies a set of actions and conditions

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actions** | [**List&lt;DeliveryRuleAction&gt;**](DeliveryRuleAction.md) | A list of actions that are executed when all the conditions of a rule are satisfied. |  |
|**conditions** | [**List&lt;DeliveryRuleCondition&gt;**](DeliveryRuleCondition.md) | A list of conditions that must be matched for the actions to be executed |  [optional] |
|**name** | **String** | Name of the rule |  [optional] |
|**order** | **Integer** | The order in which the rules are applied for the endpoint. Possible values {0,1,2,3,………}. A rule with a lesser order will be applied before a rule with a greater order. Rule with order 0 is a special rule. It does not require any condition and actions listed in it will always be applied. |  |



