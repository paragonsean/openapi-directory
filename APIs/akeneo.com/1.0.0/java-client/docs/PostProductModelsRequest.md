

# PostProductModelsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**associations** | [**ProductModelsAllOfEmbeddedItemsInnerAllOfAssociations**](ProductModelsAllOfEmbeddedItemsInnerAllOfAssociations.md) |  |  [optional] |
|**categories** | **List&lt;String&gt;** | Codes of the &lt;a href&#x3D;&#39;api-reference.html#Category&#39;&gt;categories&lt;/a&gt; in which the product model is categorized |  [optional] |
|**code** | **String** | Product model code |  |
|**created** | **String** | Date of creation |  [optional] |
|**family** | **String** | &lt;a href&#x3D;&#39;api-reference.html#Family&#39;&gt;Family&lt;/a&gt; code  from which the product inherits its attributes and attributes requirements (since the 3.2) |  [optional] |
|**familyVariant** | **String** | Family variant code from which the product model inherits its attributes and variant attributes |  |
|**metadata** | [**ProductModelsAllOfEmbeddedItemsInnerAllOfMetadata**](ProductModelsAllOfEmbeddedItemsInnerAllOfMetadata.md) |  |  [optional] |
|**parent** | **String** | Code of the parent &lt;a href&#x3D;&#39;api-reference.html#Productmodel&#39;&gt;product model&lt;/a&gt;. This parent can be modified since the 2.3. |  [optional] |
|**qualityScores** | **Object** | Product model quality scores for each channel/locale combination (&lt;strong&gt;only available since the 7.0 version&lt;/strong&gt; and when the \&quot;with_quality_scores\&quot; query parameter is set to \&quot;true\&quot;) |  [optional] |
|**quantifiedAssociations** | [**ProductModelsAllOfEmbeddedItemsInnerAllOfQuantifiedAssociations**](ProductModelsAllOfEmbeddedItemsInnerAllOfQuantifiedAssociations.md) |  |  [optional] |
|**updated** | **String** | Date of the last update |  [optional] |
|**values** | [**ProductModelsAllOfEmbeddedItemsInnerAllOfValues**](ProductModelsAllOfEmbeddedItemsInnerAllOfValues.md) |  |  [optional] |



