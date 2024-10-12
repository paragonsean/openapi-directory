# AgcoApi.BuildSystemSharedDTOParameterMapping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the parameter this mapping applies to | [optional] 
**source** | **String** | The source of the value.  The meaning of this value is determined by the source type.  When the source type is “Constant” then source is the value formatted as a string.  When the source type is “Variable” then the source is the name of the variable | [optional] 
**sourceType** | **String** | The source type used for supplying the parameter | [optional] 



## Enum: SourceTypeEnum


* `Constant` (value: `"Constant"`)

* `Variable` (value: `"Variable"`)




