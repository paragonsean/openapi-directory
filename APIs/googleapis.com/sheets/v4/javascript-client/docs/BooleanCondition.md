# GoogleSheetsApi.BooleanCondition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **String** | The type of condition. | [optional] 
**values** | [**[ConditionValue]**](ConditionValue.md) | The values of the condition. The number of supported values depends on the condition type. Some support zero values, others one or two values, and ConditionType.ONE_OF_LIST supports an arbitrary number of values. | [optional] 



## Enum: TypeEnum


* `CONDITION_TYPE_UNSPECIFIED` (value: `"CONDITION_TYPE_UNSPECIFIED"`)

* `NUMBER_GREATER` (value: `"NUMBER_GREATER"`)

* `NUMBER_GREATER_THAN_EQ` (value: `"NUMBER_GREATER_THAN_EQ"`)

* `NUMBER_LESS` (value: `"NUMBER_LESS"`)

* `NUMBER_LESS_THAN_EQ` (value: `"NUMBER_LESS_THAN_EQ"`)

* `NUMBER_EQ` (value: `"NUMBER_EQ"`)

* `NUMBER_NOT_EQ` (value: `"NUMBER_NOT_EQ"`)

* `NUMBER_BETWEEN` (value: `"NUMBER_BETWEEN"`)

* `NUMBER_NOT_BETWEEN` (value: `"NUMBER_NOT_BETWEEN"`)

* `TEXT_CONTAINS` (value: `"TEXT_CONTAINS"`)

* `TEXT_NOT_CONTAINS` (value: `"TEXT_NOT_CONTAINS"`)

* `TEXT_STARTS_WITH` (value: `"TEXT_STARTS_WITH"`)

* `TEXT_ENDS_WITH` (value: `"TEXT_ENDS_WITH"`)

* `TEXT_EQ` (value: `"TEXT_EQ"`)

* `TEXT_IS_EMAIL` (value: `"TEXT_IS_EMAIL"`)

* `TEXT_IS_URL` (value: `"TEXT_IS_URL"`)

* `DATE_EQ` (value: `"DATE_EQ"`)

* `DATE_BEFORE` (value: `"DATE_BEFORE"`)

* `DATE_AFTER` (value: `"DATE_AFTER"`)

* `DATE_ON_OR_BEFORE` (value: `"DATE_ON_OR_BEFORE"`)

* `DATE_ON_OR_AFTER` (value: `"DATE_ON_OR_AFTER"`)

* `DATE_BETWEEN` (value: `"DATE_BETWEEN"`)

* `DATE_NOT_BETWEEN` (value: `"DATE_NOT_BETWEEN"`)

* `DATE_IS_VALID` (value: `"DATE_IS_VALID"`)

* `ONE_OF_RANGE` (value: `"ONE_OF_RANGE"`)

* `ONE_OF_LIST` (value: `"ONE_OF_LIST"`)

* `BLANK` (value: `"BLANK"`)

* `NOT_BLANK` (value: `"NOT_BLANK"`)

* `CUSTOM_FORMULA` (value: `"CUSTOM_FORMULA"`)

* `BOOLEAN` (value: `"BOOLEAN"`)

* `TEXT_NOT_EQ` (value: `"TEXT_NOT_EQ"`)

* `DATE_NOT_EQ` (value: `"DATE_NOT_EQ"`)

* `FILTER_EXPRESSION` (value: `"FILTER_EXPRESSION"`)




