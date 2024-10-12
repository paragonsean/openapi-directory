

# ApplicationGatewayRewriteRule

Rewrite rule of an application gateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionSet** | [**ApplicationGatewayRewriteRuleActionSet**](ApplicationGatewayRewriteRuleActionSet.md) |  |  [optional] |
|**conditions** | [**List&lt;ApplicationGatewayRewriteRuleCondition&gt;**](ApplicationGatewayRewriteRuleCondition.md) | Conditions based on which the action set execution will be evaluated. |  [optional] |
|**name** | **String** | Name of the rewrite rule that is unique within an Application Gateway. |  [optional] |
|**ruleSequence** | **Integer** | Rule Sequence of the rewrite rule that determines the order of execution of a particular rule in a RewriteRuleSet. |  [optional] |



