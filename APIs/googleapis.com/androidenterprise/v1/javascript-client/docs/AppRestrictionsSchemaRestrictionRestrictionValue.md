# GooglePlayEmmApi.AppRestrictionsSchemaRestrictionRestrictionValue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **String** | The type of the value being provided. | [optional] 
**valueBool** | **Boolean** | The boolean value - this will only be present if type is bool. | [optional] 
**valueInteger** | **Number** | The integer value - this will only be present if type is integer. | [optional] 
**valueMultiselect** | **[String]** | The list of string values - this will only be present if type is multiselect. | [optional] 
**valueString** | **String** | The string value - this will be present for types string, choice and hidden. | [optional] 



## Enum: TypeEnum


* `bool` (value: `"bool"`)

* `string` (value: `"string"`)

* `integer` (value: `"integer"`)

* `choice` (value: `"choice"`)

* `multiselect` (value: `"multiselect"`)

* `hidden` (value: `"hidden"`)

* `bundle` (value: `"bundle"`)

* `bundleArray` (value: `"bundleArray"`)




