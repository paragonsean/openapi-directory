# DiscoveryEngineApi.GoogleCloudDiscoveryengineV1alphaFieldConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completableOption** | **String** | If completable_option is COMPLETABLE_ENABLED, field values are directly used and returned as suggestions for Autocomplete in CompletionService.CompleteQuery. If completable_option is unset, the server behavior defaults to COMPLETABLE_DISABLED for fields that support setting completable options, which are just &#x60;string&#x60; fields. For those fields that do not support setting completable options, the server will skip completable option setting, and setting completable_option for those fields will throw &#x60;INVALID_ARGUMENT&#x60; error. | [optional] 
**dynamicFacetableOption** | **String** | If dynamic_facetable_option is DYNAMIC_FACETABLE_ENABLED, field values are available for dynamic facet. Could only be DYNAMIC_FACETABLE_DISABLED if FieldConfig.indexable_option is INDEXABLE_DISABLED. Otherwise, an &#x60;INVALID_ARGUMENT&#x60; error will be returned. If dynamic_facetable_option is unset, the server behavior defaults to DYNAMIC_FACETABLE_DISABLED for fields that support setting dynamic facetable options. For those fields that do not support setting dynamic facetable options, such as &#x60;object&#x60; and &#x60;boolean&#x60;, the server will skip dynamic facetable option setting, and setting dynamic_facetable_option for those fields will throw &#x60;INVALID_ARGUMENT&#x60; error. | [optional] 
**fieldPath** | **String** | Required. Field path of the schema field. For example: &#x60;title&#x60;, &#x60;description&#x60;, &#x60;release_info.release_year&#x60;. | [optional] 
**fieldType** | **String** | Output only. Raw type of the field. | [optional] [readonly] 
**indexableOption** | **String** | If indexable_option is INDEXABLE_ENABLED, field values are indexed so that it can be filtered or faceted in SearchService.Search. If indexable_option is unset, the server behavior defaults to INDEXABLE_DISABLED for fields that support setting indexable options. For those fields that do not support setting indexable options, such as &#x60;object&#x60; and &#x60;boolean&#x60; and key properties, the server will skip indexable_option setting, and setting indexable_option for those fields will throw &#x60;INVALID_ARGUMENT&#x60; error. | [optional] 
**keyPropertyType** | **String** | Output only. Type of the key property that this field is mapped to. Empty string if this is not annotated as mapped to a key property. Example types are &#x60;title&#x60;, &#x60;description&#x60;. Full list is defined by &#x60;keyPropertyMapping&#x60; in the schema field annotation. If the schema field has a &#x60;KeyPropertyMapping&#x60; annotation, &#x60;indexable_option&#x60; and &#x60;searchable_option&#x60; of this field cannot be modified. | [optional] [readonly] 
**recsFilterableOption** | **String** | If recs_filterable_option is FILTERABLE_ENABLED, field values are filterable by filter expression in RecommendationService.Recommend. If FILTERABLE_ENABLED but the field type is numerical, field values are not filterable by text queries in RecommendationService.Recommend. Only textual fields are supported. If recs_filterable_option is unset, the default setting is FILTERABLE_DISABLED for fields that support setting filterable options. When a field set to [FILTERABLE_DISABLED] is filtered, a warning is generated and an empty result is returned. | [optional] 
**retrievableOption** | **String** | If retrievable_option is RETRIEVABLE_ENABLED, field values are included in the search results. If retrievable_option is unset, the server behavior defaults to RETRIEVABLE_DISABLED for fields that support setting retrievable options. For those fields that do not support setting retrievable options, such as &#x60;object&#x60; and &#x60;boolean&#x60;, the server will skip retrievable option setting, and setting retrievable_option for those fields will throw &#x60;INVALID_ARGUMENT&#x60; error. | [optional] 
**searchableOption** | **String** | If searchable_option is SEARCHABLE_ENABLED, field values are searchable by text queries in SearchService.Search. If SEARCHABLE_ENABLED but field type is numerical, field values will not be searchable by text queries in SearchService.Search, as there are no text values associated to numerical fields. If searchable_option is unset, the server behavior defaults to SEARCHABLE_DISABLED for fields that support setting searchable options. Only &#x60;string&#x60; fields that have no key property mapping support setting searchable_option. For those fields that do not support setting searchable options, the server will skip searchable option setting, and setting searchable_option for those fields will throw &#x60;INVALID_ARGUMENT&#x60; error. | [optional] 



## Enum: CompletableOptionEnum


* `OPTION_UNSPECIFIED` (value: `"COMPLETABLE_OPTION_UNSPECIFIED"`)

* `ENABLED` (value: `"COMPLETABLE_ENABLED"`)

* `DISABLED` (value: `"COMPLETABLE_DISABLED"`)





## Enum: DynamicFacetableOptionEnum


* `OPTION_UNSPECIFIED` (value: `"DYNAMIC_FACETABLE_OPTION_UNSPECIFIED"`)

* `ENABLED` (value: `"DYNAMIC_FACETABLE_ENABLED"`)

* `DISABLED` (value: `"DYNAMIC_FACETABLE_DISABLED"`)





## Enum: FieldTypeEnum


* `FIELD_TYPE_UNSPECIFIED` (value: `"FIELD_TYPE_UNSPECIFIED"`)

* `OBJECT` (value: `"OBJECT"`)

* `STRING` (value: `"STRING"`)

* `NUMBER` (value: `"NUMBER"`)

* `INTEGER` (value: `"INTEGER"`)

* `BOOLEAN` (value: `"BOOLEAN"`)

* `GEOLOCATION` (value: `"GEOLOCATION"`)

* `DATETIME` (value: `"DATETIME"`)





## Enum: IndexableOptionEnum


* `OPTION_UNSPECIFIED` (value: `"INDEXABLE_OPTION_UNSPECIFIED"`)

* `ENABLED` (value: `"INDEXABLE_ENABLED"`)

* `DISABLED` (value: `"INDEXABLE_DISABLED"`)





## Enum: RecsFilterableOptionEnum


* `OPTION_UNSPECIFIED` (value: `"FILTERABLE_OPTION_UNSPECIFIED"`)

* `ENABLED` (value: `"FILTERABLE_ENABLED"`)

* `DISABLED` (value: `"FILTERABLE_DISABLED"`)





## Enum: RetrievableOptionEnum


* `OPTION_UNSPECIFIED` (value: `"RETRIEVABLE_OPTION_UNSPECIFIED"`)

* `ENABLED` (value: `"RETRIEVABLE_ENABLED"`)

* `DISABLED` (value: `"RETRIEVABLE_DISABLED"`)





## Enum: SearchableOptionEnum


* `OPTION_UNSPECIFIED` (value: `"SEARCHABLE_OPTION_UNSPECIFIED"`)

* `ENABLED` (value: `"SEARCHABLE_ENABLED"`)

* `DISABLED` (value: `"SEARCHABLE_DISABLED"`)




