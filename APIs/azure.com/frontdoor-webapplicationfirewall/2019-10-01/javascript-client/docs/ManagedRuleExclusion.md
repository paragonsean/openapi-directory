# WebApplicationFirewallManagement.ManagedRuleExclusion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matchVariable** | **String** | The variable type to be excluded. | 
**selector** | **String** | Selector value for which elements in the collection this exclusion applies to. | 
**selectorMatchOperator** | **String** | Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. | 



## Enum: MatchVariableEnum


* `RequestHeaderNames` (value: `"RequestHeaderNames"`)

* `RequestCookieNames` (value: `"RequestCookieNames"`)

* `QueryStringArgNames` (value: `"QueryStringArgNames"`)

* `RequestBodyPostArgNames` (value: `"RequestBodyPostArgNames"`)





## Enum: SelectorMatchOperatorEnum


* `Equals` (value: `"Equals"`)

* `Contains` (value: `"Contains"`)

* `StartsWith` (value: `"StartsWith"`)

* `EndsWith` (value: `"EndsWith"`)

* `EqualsAny` (value: `"EqualsAny"`)




