

# JsonSchemaVariant

In a variant data type, the value of one property is used to determine how to interpret the entire entity. Its value must exist in a map of descriminant values to schema names.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**discriminant** | **String** | The name of the type discriminant property. |  [optional] |
|**map** | [**List&lt;JsonSchemaVariantMapInner&gt;**](JsonSchemaVariantMapInner.md) | The map of discriminant value to schema to use for parsing.. |  [optional] |



