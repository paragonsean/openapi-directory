

# ManagedRuleExclusion

Exclude variables from managed rule evaluation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**matchVariable** | [**MatchVariableEnum**](#MatchVariableEnum) | The variable type to be excluded. |  |
|**selector** | **String** | Selector value for which elements in the collection this exclusion applies to. |  |
|**selectorMatchOperator** | [**SelectorMatchOperatorEnum**](#SelectorMatchOperatorEnum) | Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. |  |



## Enum: MatchVariableEnum

| Name | Value |
|---- | -----|
| REQUEST_HEADER_NAMES | &quot;RequestHeaderNames&quot; |
| REQUEST_COOKIE_NAMES | &quot;RequestCookieNames&quot; |
| QUERY_STRING_ARG_NAMES | &quot;QueryStringArgNames&quot; |
| REQUEST_BODY_POST_ARG_NAMES | &quot;RequestBodyPostArgNames&quot; |



## Enum: SelectorMatchOperatorEnum

| Name | Value |
|---- | -----|
| EQUALS | &quot;Equals&quot; |
| CONTAINS | &quot;Contains&quot; |
| STARTS_WITH | &quot;StartsWith&quot; |
| ENDS_WITH | &quot;EndsWith&quot; |
| EQUALS_ANY | &quot;EqualsAny&quot; |



