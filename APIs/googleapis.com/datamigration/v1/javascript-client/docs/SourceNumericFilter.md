# DatabaseMigrationApi.SourceNumericFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numericFilterOption** | **String** | Required. Enum to set the option defining the datatypes numeric filter has to be applied to | [optional] 
**sourceMaxPrecisionFilter** | **Number** | Optional. The filter will match columns with precision smaller than or equal to this number. | [optional] 
**sourceMaxScaleFilter** | **Number** | Optional. The filter will match columns with scale smaller than or equal to this number. | [optional] 
**sourceMinPrecisionFilter** | **Number** | Optional. The filter will match columns with precision greater than or equal to this number. | [optional] 
**sourceMinScaleFilter** | **Number** | Optional. The filter will match columns with scale greater than or equal to this number. | [optional] 



## Enum: NumericFilterOptionEnum


* `UNSPECIFIED` (value: `"NUMERIC_FILTER_OPTION_UNSPECIFIED"`)

* `ALL` (value: `"NUMERIC_FILTER_OPTION_ALL"`)

* `LIMIT` (value: `"NUMERIC_FILTER_OPTION_LIMIT"`)

* `LIMITLESS` (value: `"NUMERIC_FILTER_OPTION_LIMITLESS"`)




