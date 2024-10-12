

# PatchProductsUuidRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**associations** | [**Products2AllOfEmbeddedItemsInnerAllOfAssociations**](Products2AllOfEmbeddedItemsInnerAllOfAssociations.md) |  |  [optional] |
|**categories** | **List&lt;String&gt;** | Codes of the &lt;a href&#x3D;&#39;api-reference.html#Category&#39;&gt;categories&lt;/a&gt; in which the product is classified |  [optional] |
|**completenesses** | [**List&lt;Products1AllOfEmbeddedItemsInnerAllOfCompletenessesInner&gt;**](Products1AllOfEmbeddedItemsInnerAllOfCompletenessesInner.md) | Product completenesses for each channel/locale combination (only available since the 7.0 version, and when the \&quot;with_completenesses\&quot; query parameter is set to \&quot;true\&quot;) |  [optional] |
|**created** | **String** | Date of creation |  [optional] |
|**enabled** | **Boolean** | Whether the product is enabled |  [optional] |
|**family** | **String** | &lt;a href&#x3D;&#39;api-reference.html#Family&#39;&gt;Family&lt;/a&gt; code from which the product inherits its attributes and attributes requirements. |  [optional] |
|**groups** | **List&lt;String&gt;** | Codes of the groups to which the product belong |  [optional] |
|**metadata** | [**Products1AllOfEmbeddedItemsInnerAllOfMetadata**](Products1AllOfEmbeddedItemsInnerAllOfMetadata.md) |  |  [optional] |
|**parent** | **String** | Code of the parent &lt;a href&#x3D;&#39;api-reference.html#Productmodel&#39;&gt;product model&lt;/a&gt; when the product is a variant (only available since the 2.0). This parent can be modified since the 2.3. |  [optional] |
|**qualityScores** | **Object** | Product quality scores for each channel/locale combination (only available since the 5.0 and when the \&quot;with_quality_scores\&quot; query parameter is set to \&quot;true\&quot;) |  [optional] |
|**quantifiedAssociations** | [**Products2AllOfEmbeddedItemsInnerAllOfQuantifiedAssociations**](Products2AllOfEmbeddedItemsInnerAllOfQuantifiedAssociations.md) |  |  [optional] |
|**updated** | **String** | Date of the last update |  [optional] |
|**uuid** | **String** | Product uuid |  |
|**values** | [**Products1AllOfEmbeddedItemsInnerAllOfValues**](Products1AllOfEmbeddedItemsInnerAllOfValues.md) |  |  [optional] |



