

# GoogleCloudRetailV2betaCatalogAttribute

Catalog level attribute config for an attribute. For example, if customers want to enable/disable facet for a specific attribute.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dynamicFacetableOption** | [**DynamicFacetableOptionEnum**](#DynamicFacetableOptionEnum) | If DYNAMIC_FACETABLE_ENABLED, attribute values are available for dynamic facet. Could only be DYNAMIC_FACETABLE_DISABLED if CatalogAttribute.indexable_option is INDEXABLE_DISABLED. Otherwise, an INVALID_ARGUMENT error is returned. Must be specified, otherwise throws INVALID_FORMAT error. |  [optional] |
|**exactSearchableOption** | [**ExactSearchableOptionEnum**](#ExactSearchableOptionEnum) | If EXACT_SEARCHABLE_ENABLED, attribute values will be exact searchable. This property only applies to textual custom attributes and requires indexable set to enabled to enable exact-searchable. If unset, the server behavior defaults to EXACT_SEARCHABLE_DISABLED. |  [optional] |
|**facetConfig** | [**GoogleCloudRetailV2betaCatalogAttributeFacetConfig**](GoogleCloudRetailV2betaCatalogAttributeFacetConfig.md) |  |  [optional] |
|**inUse** | **Boolean** | Output only. Indicates whether this attribute has been used by any products. &#x60;True&#x60; if at least one Product is using this attribute in Product.attributes. Otherwise, this field is &#x60;False&#x60;. CatalogAttribute can be pre-loaded by using CatalogService.AddCatalogAttribute, CatalogService.ImportCatalogAttributes, or CatalogService.UpdateAttributesConfig APIs. This field is &#x60;False&#x60; for pre-loaded CatalogAttributes. Only pre-loaded catalog attributes that are neither in use by products nor predefined can be deleted. Catalog attributes that are either in use by products or are predefined attributes cannot be deleted; however, their configuration properties will reset to default values upon removal request. After catalog changes, it takes about 10 minutes for this field to update. |  [optional] [readonly] |
|**indexableOption** | [**IndexableOptionEnum**](#IndexableOptionEnum) | When AttributesConfig.attribute_config_level is CATALOG_LEVEL_ATTRIBUTE_CONFIG, if INDEXABLE_ENABLED attribute values are indexed so that it can be filtered, faceted, or boosted in SearchService.Search. Must be specified when AttributesConfig.attribute_config_level is CATALOG_LEVEL_ATTRIBUTE_CONFIG, otherwise throws INVALID_FORMAT error. |  [optional] |
|**key** | **String** | Required. Attribute name. For example: &#x60;color&#x60;, &#x60;brands&#x60;, &#x60;attributes.custom_attribute&#x60;, such as &#x60;attributes.xyz&#x60;. To be indexable, the attribute name can contain only alpha-numeric characters and underscores. For example, an attribute named &#x60;attributes.abc_xyz&#x60; can be indexed, but an attribute named &#x60;attributes.abc-xyz&#x60; cannot be indexed. If the attribute key starts with &#x60;attributes.&#x60;, then the attribute is a custom attribute. Attributes such as &#x60;brands&#x60;, &#x60;patterns&#x60;, and &#x60;title&#x60; are built-in and called system attributes. |  [optional] |
|**recommendationsFilteringOption** | [**RecommendationsFilteringOptionEnum**](#RecommendationsFilteringOptionEnum) | When AttributesConfig.attribute_config_level is CATALOG_LEVEL_ATTRIBUTE_CONFIG, if RECOMMENDATIONS_FILTERING_ENABLED, attribute values are filterable for recommendations. This option works for categorical features only, does not work for numerical features, inventory filtering. |  [optional] |
|**retrievableOption** | [**RetrievableOptionEnum**](#RetrievableOptionEnum) | If RETRIEVABLE_ENABLED, attribute values are retrievable in the search results. If unset, the server behavior defaults to RETRIEVABLE_DISABLED. |  [optional] |
|**searchableOption** | [**SearchableOptionEnum**](#SearchableOptionEnum) | When AttributesConfig.attribute_config_level is CATALOG_LEVEL_ATTRIBUTE_CONFIG, if SEARCHABLE_ENABLED, attribute values are searchable by text queries in SearchService.Search. If SEARCHABLE_ENABLED but attribute type is numerical, attribute values will not be searchable by text queries in SearchService.Search, as there are no text values associated to numerical attributes. Must be specified, when AttributesConfig.attribute_config_level is CATALOG_LEVEL_ATTRIBUTE_CONFIG, otherwise throws INVALID_FORMAT error. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. The type of this attribute. This is derived from the attribute in Product.attributes. |  [optional] [readonly] |



## Enum: DynamicFacetableOptionEnum

| Name | Value |
|---- | -----|
| OPTION_UNSPECIFIED | &quot;DYNAMIC_FACETABLE_OPTION_UNSPECIFIED&quot; |
| ENABLED | &quot;DYNAMIC_FACETABLE_ENABLED&quot; |
| DISABLED | &quot;DYNAMIC_FACETABLE_DISABLED&quot; |



## Enum: ExactSearchableOptionEnum

| Name | Value |
|---- | -----|
| OPTION_UNSPECIFIED | &quot;EXACT_SEARCHABLE_OPTION_UNSPECIFIED&quot; |
| ENABLED | &quot;EXACT_SEARCHABLE_ENABLED&quot; |
| DISABLED | &quot;EXACT_SEARCHABLE_DISABLED&quot; |



## Enum: IndexableOptionEnum

| Name | Value |
|---- | -----|
| OPTION_UNSPECIFIED | &quot;INDEXABLE_OPTION_UNSPECIFIED&quot; |
| ENABLED | &quot;INDEXABLE_ENABLED&quot; |
| DISABLED | &quot;INDEXABLE_DISABLED&quot; |



## Enum: RecommendationsFilteringOptionEnum

| Name | Value |
|---- | -----|
| OPTION_UNSPECIFIED | &quot;RECOMMENDATIONS_FILTERING_OPTION_UNSPECIFIED&quot; |
| DISABLED | &quot;RECOMMENDATIONS_FILTERING_DISABLED&quot; |
| ENABLED | &quot;RECOMMENDATIONS_FILTERING_ENABLED&quot; |



## Enum: RetrievableOptionEnum

| Name | Value |
|---- | -----|
| OPTION_UNSPECIFIED | &quot;RETRIEVABLE_OPTION_UNSPECIFIED&quot; |
| ENABLED | &quot;RETRIEVABLE_ENABLED&quot; |
| DISABLED | &quot;RETRIEVABLE_DISABLED&quot; |



## Enum: SearchableOptionEnum

| Name | Value |
|---- | -----|
| OPTION_UNSPECIFIED | &quot;SEARCHABLE_OPTION_UNSPECIFIED&quot; |
| ENABLED | &quot;SEARCHABLE_ENABLED&quot; |
| DISABLED | &quot;SEARCHABLE_DISABLED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| TEXTUAL | &quot;TEXTUAL&quot; |
| NUMERICAL | &quot;NUMERICAL&quot; |



