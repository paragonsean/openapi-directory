# ChecksApi.Rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **String** | Rule nature | 
**operation** | **String** | Comparison between the rule and score values | 
**outcomeLabel** | **String** | Used on the scores that fulfil this rule | [optional] 
**value** | **Number** | Rule value | 



## Enum: LevelEnum


* `danger` (value: `"danger"`)

* `warning` (value: `"warning"`)

* `success` (value: `"success"`)

* `info` (value: `"info"`)





## Enum: OperationEnum


* `DOUBLE_EQUAL` (value: `"=="`)

* `GREATER_THAN_OR_EQUAL_TO` (value: `">="`)

* `GREATER_THAN` (value: `">"`)

* `LESS_THAN` (value: `"<"`)

* `LESS_THAN_OR_EQUAL_TO` (value: `"<="`)




