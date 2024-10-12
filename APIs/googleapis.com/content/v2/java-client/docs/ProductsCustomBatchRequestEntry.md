

# ProductsCustomBatchRequestEntry

A batch entry encoding a single non-batch products request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**batchId** | **Integer** | An entry ID, unique within the batch request. |  [optional] |
|**merchantId** | **String** | The ID of the managing account. |  [optional] |
|**method** | **String** | The method of the batch entry. Acceptable values are: - \&quot;&#x60;delete&#x60;\&quot; - \&quot;&#x60;get&#x60;\&quot; - \&quot;&#x60;insert&#x60;\&quot;  |  [optional] |
|**product** | [**Product**](Product.md) |  |  [optional] |
|**productId** | **String** | The ID of the product to get or delete. Only defined if the method is &#x60;get&#x60; or &#x60;delete&#x60;. |  [optional] |



