# BigQueryDataTransferApi.DataSourceParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedValues** | **[String]** | All possible values for the parameter. | [optional] 
**deprecated** | **Boolean** | If true, it should not be used in new transfers, and it should not be visible to users. | [optional] 
**description** | **String** | Parameter description. | [optional] 
**displayName** | **String** | Parameter display name in the user interface. | [optional] 
**fields** | [**[DataSourceParameter]**](DataSourceParameter.md) | Deprecated. This field has no effect. | [optional] 
**immutable** | **Boolean** | Cannot be changed after initial creation. | [optional] 
**maxValue** | **Number** | For integer and double values specifies maximum allowed value. | [optional] 
**minValue** | **Number** | For integer and double values specifies minimum allowed value. | [optional] 
**paramId** | **String** | Parameter identifier. | [optional] 
**recurse** | **Boolean** | Deprecated. This field has no effect. | [optional] 
**repeated** | **Boolean** | Deprecated. This field has no effect. | [optional] 
**required** | **Boolean** | Is parameter required. | [optional] 
**type** | **String** | Parameter type. | [optional] 
**validationDescription** | **String** | Description of the requirements for this field, in case the user input does not fulfill the regex pattern or min/max values. | [optional] 
**validationHelpUrl** | **String** | URL to a help document to further explain the naming requirements. | [optional] 
**validationRegex** | **String** | Regular expression which can be used for parameter validation. | [optional] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `STRING` (value: `"STRING"`)

* `INTEGER` (value: `"INTEGER"`)

* `DOUBLE` (value: `"DOUBLE"`)

* `BOOLEAN` (value: `"BOOLEAN"`)

* `RECORD` (value: `"RECORD"`)

* `PLUS_PAGE` (value: `"PLUS_PAGE"`)

* `LIST` (value: `"LIST"`)




