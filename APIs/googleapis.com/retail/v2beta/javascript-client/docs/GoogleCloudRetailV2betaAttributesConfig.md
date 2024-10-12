# VertexAiSearchForRetailApi.GoogleCloudRetailV2betaAttributesConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributeConfigLevel** | **String** | Output only. The AttributeConfigLevel used for this catalog. | [optional] [readonly] 
**catalogAttributes** | [**{String: GoogleCloudRetailV2betaCatalogAttribute}**](GoogleCloudRetailV2betaCatalogAttribute.md) | Enable attribute(s) config at catalog level. For example, indexable, dynamic_facetable, or searchable for each attribute. The key is catalog attribute&#39;s name. For example: &#x60;color&#x60;, &#x60;brands&#x60;, &#x60;attributes.custom_attribute&#x60;, such as &#x60;attributes.xyz&#x60;. The maximum number of catalog attributes allowed in a request is 1000. | [optional] 
**name** | **String** | Required. Immutable. The fully qualified resource name of the attribute config. Format: &#x60;projects/_*_/locations/_*_/catalogs/_*_/attributesConfig&#x60; | [optional] 



## Enum: AttributeConfigLevelEnum


* `ATTRIBUTE_CONFIG_LEVEL_UNSPECIFIED` (value: `"ATTRIBUTE_CONFIG_LEVEL_UNSPECIFIED"`)

* `PRODUCT_LEVEL_ATTRIBUTE_CONFIG` (value: `"PRODUCT_LEVEL_ATTRIBUTE_CONFIG"`)

* `CATALOG_LEVEL_ATTRIBUTE_CONFIG` (value: `"CATALOG_LEVEL_ATTRIBUTE_CONFIG"`)




