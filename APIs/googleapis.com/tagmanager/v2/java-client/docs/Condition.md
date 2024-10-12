

# Condition

Represents a predicate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**parameter** | [**List&lt;Parameter&gt;**](Parameter.md) | A list of named parameters (key/value), depending on the condition&#39;s type. Notes: - For binary operators, include parameters named arg0 and arg1 for specifying the left and right operands, respectively. - At this time, the left operand (arg0) must be a reference to a variable. - For case-insensitive Regex matching, include a boolean parameter named ignore_case that is set to true. If not specified or set to any other value, the matching will be case sensitive. - To negate an operator, include a boolean parameter named negate boolean parameter that is set to true. @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of operator for this condition. @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CONDITION_TYPE_UNSPECIFIED | &quot;conditionTypeUnspecified&quot; |
| EQUALS | &quot;equals&quot; |
| CONTAINS | &quot;contains&quot; |
| STARTS_WITH | &quot;startsWith&quot; |
| ENDS_WITH | &quot;endsWith&quot; |
| MATCH_REGEX | &quot;matchRegex&quot; |
| GREATER | &quot;greater&quot; |
| GREATER_OR_EQUALS | &quot;greaterOrEquals&quot; |
| LESS | &quot;less&quot; |
| LESS_OR_EQUALS | &quot;lessOrEquals&quot; |
| CSS_SELECTOR | &quot;cssSelector&quot; |
| URL_MATCHES | &quot;urlMatches&quot; |



