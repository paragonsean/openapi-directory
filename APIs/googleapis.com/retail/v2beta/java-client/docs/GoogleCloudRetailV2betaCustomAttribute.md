

# GoogleCloudRetailV2betaCustomAttribute

A custom attribute that is not explicitly modeled in Product.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**indexable** | **Boolean** | This field is normally ignored unless AttributesConfig.attribute_config_level of the Catalog is set to the deprecated &#39;PRODUCT_LEVEL_ATTRIBUTE_CONFIG&#39; mode. For information about product-level attribute configuration, see [Configuration modes](https://cloud.google.com/retail/docs/attribute-config#config-modes). If true, custom attribute values are indexed, so that they can be filtered, faceted or boosted in SearchService.Search. This field is ignored in a UserEvent. See SearchRequest.filter, SearchRequest.facet_specs and SearchRequest.boost_spec for more details. |  [optional] |
|**numbers** | **List&lt;Double&gt;** | The numerical values of this custom attribute. For example, &#x60;[2.3, 15.4]&#x60; when the key is \&quot;lengths_cm\&quot;. Exactly one of text or numbers should be set. Otherwise, an INVALID_ARGUMENT error is returned. |  [optional] |
|**searchable** | **Boolean** | This field is normally ignored unless AttributesConfig.attribute_config_level of the Catalog is set to the deprecated &#39;PRODUCT_LEVEL_ATTRIBUTE_CONFIG&#39; mode. For information about product-level attribute configuration, see [Configuration modes](https://cloud.google.com/retail/docs/attribute-config#config-modes). If true, custom attribute values are searchable by text queries in SearchService.Search. This field is ignored in a UserEvent. Only set if type text is set. Otherwise, a INVALID_ARGUMENT error is returned. |  [optional] |
|**text** | **List&lt;String&gt;** | The textual values of this custom attribute. For example, &#x60;[\&quot;yellow\&quot;, \&quot;green\&quot;]&#x60; when the key is \&quot;color\&quot;. Empty string is not allowed. Otherwise, an INVALID_ARGUMENT error is returned. Exactly one of text or numbers should be set. Otherwise, an INVALID_ARGUMENT error is returned. |  [optional] |



