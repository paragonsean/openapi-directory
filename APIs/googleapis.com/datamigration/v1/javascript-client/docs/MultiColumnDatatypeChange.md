# DatabaseMigrationApi.MultiColumnDatatypeChange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customFeatures** | **{String: Object}** | Optional. Custom engine specific features. | [optional] 
**newDataType** | **String** | Required. New data type. | [optional] 
**overrideFractionalSecondsPrecision** | **Number** | Optional. Column fractional seconds precision - used only for timestamp based datatypes - if not specified and relevant uses the source column fractional seconds precision. | [optional] 
**overrideLength** | **String** | Optional. Column length - e.g. varchar (50) - if not specified and relevant uses the source column length. | [optional] 
**overridePrecision** | **Number** | Optional. Column precision - when relevant - if not specified and relevant uses the source column precision. | [optional] 
**overrideScale** | **Number** | Optional. Column scale - when relevant - if not specified and relevant uses the source column scale. | [optional] 
**sourceDataTypeFilter** | **String** | Required. Filter on source data type. | [optional] 
**sourceNumericFilter** | [**SourceNumericFilter**](SourceNumericFilter.md) |  | [optional] 
**sourceTextFilter** | [**SourceTextFilter**](SourceTextFilter.md) |  | [optional] 


