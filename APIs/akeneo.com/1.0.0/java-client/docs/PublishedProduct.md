

# PublishedProduct


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**associations** | [**PublishedProductsAllOfEmbeddedItemsInnerAllOfAssociations**](PublishedProductsAllOfEmbeddedItemsInnerAllOfAssociations.md) |  |  [optional] |
|**categories** | **List&lt;String&gt;** | Codes of the &lt;a href&#x3D;&#39;api-reference.html#Category&#39;&gt;categories&lt;/a&gt; in which the published product is classified |  [optional] |
|**created** | **String** | Date of creation |  [optional] |
|**enabled** | **Boolean** | Whether the published product is enable |  [optional] |
|**family** | **String** | &lt;a href&#x3D;&#39;api-reference.html#Family&#39;&gt;Family&lt;/a&gt; code from which the published product inherits its attributes and attributes requirements |  [optional] |
|**groups** | **List&lt;String&gt;** | Codes of the groups to which the published product belong |  [optional] |
|**identifier** | **String** | Published product identifier, i.e. the value of the only &#x60;pim_catalog_identifier&#x60; attribute |  |
|**quantifiedAssociations** | **Object** | Warning: associations with quantities are not compatible with the published products. The response will always be empty. |  [optional] |
|**updated** | **String** | Date of the last update |  [optional] |
|**values** | [**PublishedProductsAllOfEmbeddedItemsInnerAllOfValues**](PublishedProductsAllOfEmbeddedItemsInnerAllOfValues.md) |  |  [optional] |



