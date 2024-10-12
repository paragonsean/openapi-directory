

# OrdersCustomBatchResponseEntry


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**batchId** | **Integer** | The ID of the request entry this entry responds to. |  [optional] |
|**errors** | [**Errors**](Errors.md) |  |  [optional] |
|**executionStatus** | **String** | The status of the execution. Only defined if 1. the request was successful; and 2. the method is not &#x60;get&#x60;, &#x60;getByMerchantOrderId&#x60;, or one of the test methods. Acceptable values are: - \&quot;&#x60;duplicate&#x60;\&quot; - \&quot;&#x60;executed&#x60;\&quot;  |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;&#x60;content#ordersCustomBatchResponseEntry&#x60;\&quot; |  [optional] |
|**order** | [**Order**](Order.md) |  |  [optional] |



