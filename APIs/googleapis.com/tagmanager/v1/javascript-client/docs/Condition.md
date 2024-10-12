# TagManagerApi.Condition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter** | [**[Parameter]**](Parameter.md) | A list of named parameters (key/value), depending on the condition&#39;s type. Notes: - For binary operators, include parameters named arg0 and arg1 for specifying the left and right operands, respectively. - At this time, the left operand (arg0) must be a reference to a variable. - For case-insensitive Regex matching, include a boolean parameter named ignore_case that is set to true. If not specified or set to any other value, the matching will be case sensitive. - To negate an operator, include a boolean parameter named negate boolean parameter that is set to true. @mutable tagmanager.accounts.containers.triggers.create @mutable tagmanager.accounts.containers.triggers.update | [optional] 
**type** | **String** | The type of operator for this condition. @mutable tagmanager.accounts.containers.triggers.create @mutable tagmanager.accounts.containers.triggers.update | [optional] 



## Enum: TypeEnum


* `equals` (value: `"equals"`)

* `contains` (value: `"contains"`)

* `startsWith` (value: `"startsWith"`)

* `endsWith` (value: `"endsWith"`)

* `matchRegex` (value: `"matchRegex"`)

* `greater` (value: `"greater"`)

* `greaterOrEquals` (value: `"greaterOrEquals"`)

* `less` (value: `"less"`)

* `lessOrEquals` (value: `"lessOrEquals"`)

* `cssSelector` (value: `"cssSelector"`)

* `urlMatches` (value: `"urlMatches"`)




