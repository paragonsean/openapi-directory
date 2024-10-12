

# SchemaPropertiesFieldName

Schema of any given field described in the `properties` field.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**items** | **Object** | Object containing the type of the items if the field is an array. Typically, arrays will contain strings and will be used for fields such as &#x60;email&#x60;. |  [optional] |
|**pii** | **Boolean** | Indicates whether property is Personal Identifiable Information. |  |
|**sensitive** | **Boolean** | Indicates whether property is sensitive data. |  |
|**type** | **String** | Schema property type. |  |



