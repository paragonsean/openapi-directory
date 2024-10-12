

# GoogleCloudRecommendationengineV1beta1CatalogItem

CatalogItem captures all metadata information of items to be recommended.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categoryHierarchies** | [**List&lt;GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchy&gt;**](GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchy.md) | Required. Catalog item categories. This field is repeated for supporting one catalog item belonging to several parallel category hierarchies. For example, if a shoes product belongs to both [\&quot;Shoes &amp; Accessories\&quot; -&gt; \&quot;Shoes\&quot;] and [\&quot;Sports &amp; Fitness\&quot; -&gt; \&quot;Athletic Clothing\&quot; -&gt; \&quot;Shoes\&quot;], it could be represented as: \&quot;categoryHierarchies\&quot;: [ { \&quot;categories\&quot;: [\&quot;Shoes &amp; Accessories\&quot;, \&quot;Shoes\&quot;]}, { \&quot;categories\&quot;: [\&quot;Sports &amp; Fitness\&quot;, \&quot;Athletic Clothing\&quot;, \&quot;Shoes\&quot;] } ] |  [optional] |
|**description** | **String** | Optional. Catalog item description. UTF-8 encoded string with a length limit of 5 KiB. |  [optional] |
|**id** | **String** | Required. Catalog item identifier. UTF-8 encoded string with a length limit of 128 bytes. This id must be unique among all catalog items within the same catalog. It should also be used when logging user events in order for the user events to be joined with the Catalog. |  [optional] |
|**itemAttributes** | [**GoogleCloudRecommendationengineV1beta1FeatureMap**](GoogleCloudRecommendationengineV1beta1FeatureMap.md) |  |  [optional] |
|**itemGroupId** | **String** | Optional. Variant group identifier for prediction results. UTF-8 encoded string with a length limit of 128 bytes. This field must be enabled before it can be used. [Learn more](/recommendations-ai/docs/catalog#item-group-id). |  [optional] |
|**languageCode** | **String** | Optional. Deprecated. The model automatically detects the text language. Your catalog can include text in different languages, but duplicating catalog items to provide text in multiple languages can result in degraded model performance. |  [optional] |
|**productMetadata** | [**GoogleCloudRecommendationengineV1beta1ProductCatalogItem**](GoogleCloudRecommendationengineV1beta1ProductCatalogItem.md) |  |  [optional] |
|**tags** | **List&lt;String&gt;** | Optional. Filtering tags associated with the catalog item. Each tag should be a UTF-8 encoded string with a length limit of 1 KiB. This tag can be used for filtering recommendation results by passing the tag as part of the predict request filter. |  [optional] |
|**title** | **String** | Required. Catalog item title. UTF-8 encoded string with a length limit of 1 KiB. |  [optional] |



