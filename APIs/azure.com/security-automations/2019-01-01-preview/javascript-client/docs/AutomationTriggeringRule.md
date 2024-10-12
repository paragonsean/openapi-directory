# SecurityCenter.AutomationTriggeringRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expectedValue** | **String** | The expected value. | [optional] 
**operator** | **String** | A valid comparer operator to use. A case-insensitive comparison will be applied for String PropertyType. | [optional] 
**propertyJPath** | **String** | The JPath of the entity model property that should be checked. | [optional] 
**propertyType** | **String** | The data type of the compared operands (string, integer, floating point number or a boolean [true/false]] | [optional] 



## Enum: OperatorEnum


* `Equals` (value: `"Equals"`)

* `GreaterThan` (value: `"GreaterThan"`)

* `GreaterThanOrEqualTo` (value: `"GreaterThanOrEqualTo"`)

* `LesserThan` (value: `"LesserThan"`)

* `LesserThanOrEqualTo` (value: `"LesserThanOrEqualTo"`)

* `NotEquals` (value: `"NotEquals"`)

* `Contains` (value: `"Contains"`)

* `StartsWith` (value: `"StartsWith"`)

* `EndsWith` (value: `"EndsWith"`)





## Enum: PropertyTypeEnum


* `String` (value: `"String"`)

* `Integer` (value: `"Integer"`)

* `Number` (value: `"Number"`)

* `Boolean` (value: `"Boolean"`)




