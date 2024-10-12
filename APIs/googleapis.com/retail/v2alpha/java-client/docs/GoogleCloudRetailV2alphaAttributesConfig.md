

# GoogleCloudRetailV2alphaAttributesConfig

Catalog level attribute config.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributeConfigLevel** | [**AttributeConfigLevelEnum**](#AttributeConfigLevelEnum) | Output only. The AttributeConfigLevel used for this catalog. |  [optional] [readonly] |
|**catalogAttributes** | [**Map&lt;String, GoogleCloudRetailV2alphaCatalogAttribute&gt;**](GoogleCloudRetailV2alphaCatalogAttribute.md) | Enable attribute(s) config at catalog level. For example, indexable, dynamic_facetable, or searchable for each attribute. The key is catalog attribute&#39;s name. For example: &#x60;color&#x60;, &#x60;brands&#x60;, &#x60;attributes.custom_attribute&#x60;, such as &#x60;attributes.xyz&#x60;. The maximum number of catalog attributes allowed in a request is 1000. |  [optional] |
|**name** | **String** | Required. Immutable. The fully qualified resource name of the attribute config. Format: &#x60;projects/_*_/locations/_*_/catalogs/_*_/attributesConfig&#x60; |  [optional] |



## Enum: AttributeConfigLevelEnum

| Name | Value |
|---- | -----|
| ATTRIBUTE_CONFIG_LEVEL_UNSPECIFIED | &quot;ATTRIBUTE_CONFIG_LEVEL_UNSPECIFIED&quot; |
| PRODUCT_LEVEL_ATTRIBUTE_CONFIG | &quot;PRODUCT_LEVEL_ATTRIBUTE_CONFIG&quot; |
| CATALOG_LEVEL_ATTRIBUTE_CONFIG | &quot;CATALOG_LEVEL_ATTRIBUTE_CONFIG&quot; |



