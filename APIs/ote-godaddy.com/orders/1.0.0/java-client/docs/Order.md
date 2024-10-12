

# Order


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billTo** | [**BillTo**](BillTo.md) |  |  |
|**createdAt** | **String** | Date and time when the current order is created on |  |
|**currency** | **String** | Currency in which the order has been placed |  |
|**items** | [**List&lt;LineItem&gt;**](LineItem.md) |  |  |
|**orderId** | **String** | Unique identifier of current order |  |
|**parentOrderId** | **String** | Unique identifier of the parent order. All refund/chargeback orders are tied to the original order. The orginal order&#39;s &#x60;orderId&#x60; is the &#x60;parentOrderId&#x60; of refund/chargeback orders |  [optional] |
|**payments** | [**List&lt;Payment&gt;**](Payment.md) |  |  |
|**pricing** | [**OrderPricing**](OrderPricing.md) |  |  |



