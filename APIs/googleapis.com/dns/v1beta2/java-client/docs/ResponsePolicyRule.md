

# ResponsePolicyRule

A Response Policy Rule is a selector that applies its behavior to queries that match the selector. Selectors are DNS names, which may be wildcards or exact matches. Each DNS query subject to a Response Policy matches at most one ResponsePolicyRule, as identified by the dns_name field with the longest matching suffix.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**behavior** | [**BehaviorEnum**](#BehaviorEnum) | Answer this query with a behavior rather than DNS data. |  [optional] |
|**dnsName** | **String** | The DNS name (wildcard or exact) to apply this rule to. Must be unique within the Response Policy Rule. |  [optional] |
|**kind** | **String** |  |  [optional] |
|**localData** | [**ResponsePolicyRuleLocalData**](ResponsePolicyRuleLocalData.md) |  |  [optional] |
|**ruleName** | **String** | An identifier for this rule. Must be unique with the ResponsePolicy. |  [optional] |



## Enum: BehaviorEnum

| Name | Value |
|---- | -----|
| BEHAVIOR_UNSPECIFIED | &quot;behaviorUnspecified&quot; |
| BYPASS_RESPONSE_POLICY | &quot;bypassResponsePolicy&quot; |



