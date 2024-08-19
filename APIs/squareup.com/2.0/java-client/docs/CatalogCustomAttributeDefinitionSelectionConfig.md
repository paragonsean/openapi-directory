

# CatalogCustomAttributeDefinitionSelectionConfig

Configuration associated with `SELECTION`-type custom attribute definitions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedSelections** | [**List&lt;CatalogCustomAttributeDefinitionSelectionConfigCustomAttributeSelection&gt;**](CatalogCustomAttributeDefinitionSelectionConfigCustomAttributeSelection.md) | The set of valid &#x60;CatalogCustomAttributeSelections&#x60;. Up to a maximum of 100 selections can be defined. Can be modified. |  [optional] |
|**maxAllowedSelections** | **Integer** | The maximum number of selections that can be set. The maximum value for this attribute is 100. The default value is 1. The value can be modified, but changing the value will not affect existing custom attribute values on objects. Clients need to handle custom attributes with more selected values than allowed by this limit. |  [optional] |



