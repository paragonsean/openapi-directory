

# TerminalOrder


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingEntity** | [**BillingEntity**](BillingEntity.md) | The details of the entity that the order is billed to. |  [optional] |
|**customerOrderReference** | **String** | The merchant-defined purchase order number. This will be printed on the packing list. |  [optional] |
|**id** | **String** | The unique identifier of the order. |  [optional] |
|**items** | [**List&lt;OrderItem&gt;**](OrderItem.md) | The products included in the order. |  [optional] |
|**orderDate** | **String** | The date and time that the order was placed, in UTC ISO 8601 format. For example, \&quot;2011-12-03T10:15:30Z\&quot;. |  [optional] |
|**shippingLocation** | [**ShippingLocation**](ShippingLocation.md) | The details of the location where the order is shipped to. |  [optional] |
|**status** | **String** | The processing status of the order. |  [optional] |
|**trackingUrl** | **String** | The URL, provided by the carrier company, where the shipment can be tracked. |  [optional] |



