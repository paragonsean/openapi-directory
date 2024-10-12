# Superset.ChartDataFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**col** | **String** | The column to filter. | 
**op** | **String** | The comparison operator. | 
**val** | **Object** | The value or values to compare against. Can be a string, integer, decimal or list, depending on the operator. | [optional] 



## Enum: OpEnum


* `DOUBLE_EQUAL` (value: `"=="`)

* `NOT_EQUAL` (value: `"!="`)

* `GREATER_THAN` (value: `">"`)

* `LESS_THAN` (value: `"<"`)

* `GREATER_THAN_OR_EQUAL_TO` (value: `">="`)

* `LESS_THAN_OR_EQUAL_TO` (value: `"<="`)

* `LIKE` (value: `"LIKE"`)

* `ILIKE` (value: `"ILIKE"`)

* `IS NULL` (value: `"IS NULL"`)

* `IS NOT NULL` (value: `"IS NOT NULL"`)

* `IN` (value: `"IN"`)

* `NOT IN` (value: `"NOT IN"`)

* `REGEX` (value: `"REGEX"`)

* `IS TRUE` (value: `"IS TRUE"`)

* `IS FALSE` (value: `"IS FALSE"`)




