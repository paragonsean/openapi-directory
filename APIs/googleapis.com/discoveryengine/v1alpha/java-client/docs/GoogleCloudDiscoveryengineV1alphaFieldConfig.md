

# GoogleCloudDiscoveryengineV1alphaFieldConfig

Configurations for fields of a schema. For example, configuring a field is indexable, or searchable.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**completableOption** | [**CompletableOptionEnum**](#CompletableOptionEnum) | If completable_option is COMPLETABLE_ENABLED, field values are directly used and returned as suggestions for Autocomplete in CompletionService.CompleteQuery. If completable_option is unset, the server behavior defaults to COMPLETABLE_DISABLED for fields that support setting completable options, which are just &#x60;string&#x60; fields. For those fields that do not support setting completable options, the server will skip completable option setting, and setting completable_option for those fields will throw &#x60;INVALID_ARGUMENT&#x60; error. |  [optional] |
|**dynamicFacetableOption** | [**DynamicFacetableOptionEnum**](#DynamicFacetableOptionEnum) | If dynamic_facetable_option is DYNAMIC_FACETABLE_ENABLED, field values are available for dynamic facet. Could only be DYNAMIC_FACETABLE_DISABLED if FieldConfig.indexable_option is INDEXABLE_DISABLED. Otherwise, an &#x60;INVALID_ARGUMENT&#x60; error will be returned. If dynamic_facetable_option is unset, the server behavior defaults to DYNAMIC_FACETABLE_DISABLED for fields that support setting dynamic facetable options. For those fields that do not support setting dynamic facetable options, such as &#x60;object&#x60; and &#x60;boolean&#x60;, the server will skip dynamic facetable option setting, and setting dynamic_facetable_option for those fields will throw &#x60;INVALID_ARGUMENT&#x60; error. |  [optional] |
|**fieldPath** | **String** | Required. Field path of the schema field. For example: &#x60;title&#x60;, &#x60;description&#x60;, &#x60;release_info.release_year&#x60;. |  [optional] |
|**fieldType** | [**FieldTypeEnum**](#FieldTypeEnum) | Output only. Raw type of the field. |  [optional] [readonly] |
|**indexableOption** | [**IndexableOptionEnum**](#IndexableOptionEnum) | If indexable_option is INDEXABLE_ENABLED, field values are indexed so that it can be filtered or faceted in SearchService.Search. If indexable_option is unset, the server behavior defaults to INDEXABLE_DISABLED for fields that support setting indexable options. For those fields that do not support setting indexable options, such as &#x60;object&#x60; and &#x60;boolean&#x60; and key properties, the server will skip indexable_option setting, and setting indexable_option for those fields will throw &#x60;INVALID_ARGUMENT&#x60; error. |  [optional] |
|**keyPropertyType** | **String** | Output only. Type of the key property that this field is mapped to. Empty string if this is not annotated as mapped to a key property. Example types are &#x60;title&#x60;, &#x60;description&#x60;. Full list is defined by &#x60;keyPropertyMapping&#x60; in the schema field annotation. If the schema field has a &#x60;KeyPropertyMapping&#x60; annotation, &#x60;indexable_option&#x60; and &#x60;searchable_option&#x60; of this field cannot be modified. |  [optional] [readonly] |
|**recsFilterableOption** | [**RecsFilterableOptionEnum**](#RecsFilterableOptionEnum) | If recs_filterable_option is FILTERABLE_ENABLED, field values are filterable by filter expression in RecommendationService.Recommend. If FILTERABLE_ENABLED but the field type is numerical, field values are not filterable by text queries in RecommendationService.Recommend. Only textual fields are supported. If recs_filterable_option is unset, the default setting is FILTERABLE_DISABLED for fields that support setting filterable options. When a field set to [FILTERABLE_DISABLED] is filtered, a warning is generated and an empty result is returned. |  [optional] |
|**retrievableOption** | [**RetrievableOptionEnum**](#RetrievableOptionEnum) | If retrievable_option is RETRIEVABLE_ENABLED, field values are included in the search results. If retrievable_option is unset, the server behavior defaults to RETRIEVABLE_DISABLED for fields that support setting retrievable options. For those fields that do not support setting retrievable options, such as &#x60;object&#x60; and &#x60;boolean&#x60;, the server will skip retrievable option setting, and setting retrievable_option for those fields will throw &#x60;INVALID_ARGUMENT&#x60; error. |  [optional] |
|**searchableOption** | [**SearchableOptionEnum**](#SearchableOptionEnum) | If searchable_option is SEARCHABLE_ENABLED, field values are searchable by text queries in SearchService.Search. If SEARCHABLE_ENABLED but field type is numerical, field values will not be searchable by text queries in SearchService.Search, as there are no text values associated to numerical fields. If searchable_option is unset, the server behavior defaults to SEARCHABLE_DISABLED for fields that support setting searchable options. Only &#x60;string&#x60; fields that have no key property mapping support setting searchable_option. For those fields that do not support setting searchable options, the server will skip searchable option setting, and setting searchable_option for those fields will throw &#x60;INVALID_ARGUMENT&#x60; error. |  [optional] |



## Enum: CompletableOptionEnum

| Name | Value |
|---- | -----|
| OPTION_UNSPECIFIED | &quot;COMPLETABLE_OPTION_UNSPECIFIED&quot; |
| ENABLED | &quot;COMPLETABLE_ENABLED&quot; |
| DISABLED | &quot;COMPLETABLE_DISABLED&quot; |



## Enum: DynamicFacetableOptionEnum

| Name | Value |
|---- | -----|
| OPTION_UNSPECIFIED | &quot;DYNAMIC_FACETABLE_OPTION_UNSPECIFIED&quot; |
| ENABLED | &quot;DYNAMIC_FACETABLE_ENABLED&quot; |
| DISABLED | &quot;DYNAMIC_FACETABLE_DISABLED&quot; |



## Enum: FieldTypeEnum

| Name | Value |
|---- | -----|
| FIELD_TYPE_UNSPECIFIED | &quot;FIELD_TYPE_UNSPECIFIED&quot; |
| OBJECT | &quot;OBJECT&quot; |
| STRING | &quot;STRING&quot; |
| NUMBER | &quot;NUMBER&quot; |
| INTEGER | &quot;INTEGER&quot; |
| BOOLEAN | &quot;BOOLEAN&quot; |
| GEOLOCATION | &quot;GEOLOCATION&quot; |
| DATETIME | &quot;DATETIME&quot; |



## Enum: IndexableOptionEnum

| Name | Value |
|---- | -----|
| OPTION_UNSPECIFIED | &quot;INDEXABLE_OPTION_UNSPECIFIED&quot; |
| ENABLED | &quot;INDEXABLE_ENABLED&quot; |
| DISABLED | &quot;INDEXABLE_DISABLED&quot; |



## Enum: RecsFilterableOptionEnum

| Name | Value |
|---- | -----|
| OPTION_UNSPECIFIED | &quot;FILTERABLE_OPTION_UNSPECIFIED&quot; |
| ENABLED | &quot;FILTERABLE_ENABLED&quot; |
| DISABLED | &quot;FILTERABLE_DISABLED&quot; |



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



