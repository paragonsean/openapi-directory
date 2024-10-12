

# ProductsCustomBatchRequestEntry

A batch entry encoding a single non-batch products request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**batchId** | **Integer** | An entry ID, unique within the batch request. |  [optional] |
|**feedId** | **String** | The Content API Supplemental Feed ID. If present then product insertion or deletion applies to a supplemental feed instead of primary Content API feed. |  [optional] |
|**merchantId** | **String** | The ID of the managing account. |  [optional] |
|**method** | **String** | The method of the batch entry. Acceptable values are: - \&quot;&#x60;delete&#x60;\&quot; - \&quot;&#x60;get&#x60;\&quot; - \&quot;&#x60;insert&#x60;\&quot; - \&quot;&#x60;update&#x60;\&quot;  |  [optional] |
|**product** | [**Product**](Product.md) |  |  [optional] |
|**productId** | **String** | The ID of the product to get or mutate. Only defined if the method is &#x60;get&#x60;, &#x60;delete&#x60;, or &#x60;update&#x60;. |  [optional] |
|**updateMask** | **String** | The comma-separated list of product attributes to be updated. Example: &#x60;\&quot;title,salePrice\&quot;&#x60;. Attributes specified in the update mask without a value specified in the body will be deleted from the product. *You must specify the update mask to delete attributes.* Only top-level product attributes can be updated. If not defined, product attributes with set values will be updated and other attributes will stay unchanged. Only defined if the method is &#x60;update&#x60;. |  [optional] |



