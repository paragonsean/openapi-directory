# CloudDnsApi.ResponsePolicyRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**behavior** | **String** | Answer this query with a behavior rather than DNS data. | [optional] 
**dnsName** | **String** | The DNS name (wildcard or exact) to apply this rule to. Must be unique within the Response Policy Rule. | [optional] 
**kind** | **String** |  | [optional] [default to &#39;dns#responsePolicyRule&#39;]
**localData** | [**ResponsePolicyRuleLocalData**](ResponsePolicyRuleLocalData.md) |  | [optional] 
**ruleName** | **String** | An identifier for this rule. Must be unique with the ResponsePolicy. | [optional] 



## Enum: BehaviorEnum


* `BEHAVIOR_UNSPECIFIED` (value: `"BEHAVIOR_UNSPECIFIED"`)

* `BYPASS_RESPONSE_POLICY` (value: `"BYPASS_RESPONSE_POLICY"`)




