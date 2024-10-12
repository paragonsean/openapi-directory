# CustomerInsightsManagementClient.PropertyDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arrayValueSeparator** | **String** | Array value separator for properties with isArray set. | [optional] 
**dataSourcePrecedenceRules** | [**[DataSourcePrecedence]**](DataSourcePrecedence.md) | This is specific to interactions modeled as activities. Data sources are used to determine where data is stored and also in precedence rules. | [optional] [readonly] 
**enumValidValues** | [**[ProfileEnumValidValuesFormat]**](ProfileEnumValidValuesFormat.md) | Describes valid values for an enum property. | [optional] 
**fieldName** | **String** | Name of the property. | 
**fieldType** | **String** | Type of the property. | 
**isArray** | **Boolean** | Indicates if the property is actually an array of the fieldType above on the data api. | [optional] 
**isAvailableInGraph** | **Boolean** | Whether property is available in graph or not. | [optional] 
**isEnum** | **Boolean** | Indicates if the property is an enum. | [optional] 
**isFlagEnum** | **Boolean** | Indicates if the property is an flag enum. | [optional] 
**isImage** | **Boolean** | Whether the property is an Image. | [optional] 
**isLocalizedString** | **Boolean** | Whether the property is a localized string. | [optional] 
**isName** | **Boolean** | Whether the property is a name or a part of name. | [optional] 
**isRequired** | **Boolean** | Whether property value is required on instances, IsRequired field only for Interaction. Profile Instance will not check for required field. | [optional] 
**maxLength** | **Number** | Max length of string. Used only if type is string. | [optional] 
**propertyId** | **String** | The ID associated with the property. | [optional] 
**schemaItemPropLink** | **String** | URL encoded schema.org item prop link for the property. | [optional] 


