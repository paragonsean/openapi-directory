

# PosCustomBatchRequestEntry


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**batchId** | **Integer** | An entry ID, unique within the batch request. |  [optional] |
|**inventory** | [**PosInventory**](PosInventory.md) |  |  [optional] |
|**merchantId** | **String** | The ID of the POS data provider. |  [optional] |
|**method** | **String** | The method of the batch entry. Acceptable values are: - \&quot;&#x60;delete&#x60;\&quot; - \&quot;&#x60;get&#x60;\&quot; - \&quot;&#x60;insert&#x60;\&quot; - \&quot;&#x60;inventory&#x60;\&quot; - \&quot;&#x60;sale&#x60;\&quot;  |  [optional] |
|**sale** | [**PosSale**](PosSale.md) |  |  [optional] |
|**store** | [**PosStore**](PosStore.md) |  |  [optional] |
|**storeCode** | **String** | The store code. This should be set only if the method is &#x60;delete&#x60; or &#x60;get&#x60;. |  [optional] |
|**targetMerchantId** | **String** | The ID of the account for which to get/submit data. |  [optional] |



