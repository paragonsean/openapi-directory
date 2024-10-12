

# MultiColumnDatatypeChange

Options to configure rule type MultiColumnDatatypeChange. The rule is used to change the data type and associated properties of multiple columns at once. The rule filter field can refer to one or more entities. The rule scope can be one of:Column. This rule requires additional filters to be specified beyond the basic rule filter field, which is the source data type, but the rule supports additional filtering capabilities such as the minimum and maximum field length. All additional filters which are specified are required to be met in order for the rule to be applied (logical AND between the fields).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customFeatures** | **Map&lt;String, Object&gt;** | Optional. Custom engine specific features. |  [optional] |
|**newDataType** | **String** | Required. New data type. |  [optional] |
|**overrideFractionalSecondsPrecision** | **Integer** | Optional. Column fractional seconds precision - used only for timestamp based datatypes - if not specified and relevant uses the source column fractional seconds precision. |  [optional] |
|**overrideLength** | **String** | Optional. Column length - e.g. varchar (50) - if not specified and relevant uses the source column length. |  [optional] |
|**overridePrecision** | **Integer** | Optional. Column precision - when relevant - if not specified and relevant uses the source column precision. |  [optional] |
|**overrideScale** | **Integer** | Optional. Column scale - when relevant - if not specified and relevant uses the source column scale. |  [optional] |
|**sourceDataTypeFilter** | **String** | Required. Filter on source data type. |  [optional] |
|**sourceNumericFilter** | [**SourceNumericFilter**](SourceNumericFilter.md) |  |  [optional] |
|**sourceTextFilter** | [**SourceTextFilter**](SourceTextFilter.md) |  |  [optional] |



