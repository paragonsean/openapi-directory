

# OrdersSetLineItemMetadataRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotations** | [**List&lt;OrderMerchantProvidedAnnotation&gt;**](OrderMerchantProvidedAnnotation.md) |  |  [optional] |
|**lineItemId** | **String** | The ID of the line item to set metadata. Either lineItemId or productId is required. |  [optional] |
|**operationId** | **String** | The ID of the operation. Unique across all operations for a given order. |  [optional] |
|**productId** | **String** | The ID of the product to set metadata. This is the REST ID used in the products service. Either lineItemId or productId is required. |  [optional] |



