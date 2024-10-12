

# SalesOrderListDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**Map&lt;String, DtoLink&gt;**](DtoLink.md) | Links applicable for the dto |  [optional] |
|**currency** | **String** | The currency id for the order |  [optional] |
|**customerId** | **String** | The customer Id for the order (a.k.a CustoemrCd) |  [optional] |
|**customerName** | **String** | The name of the customer as it appears on the order |  [optional] |
|**customerOrder** | **String** | The customer order link |  [optional] |
|**customerRefNo** | **String** | The order reference number of the customer |  [optional] |
|**date** | **OffsetDateTime** | The order date  Unless a specific time zone offset is included (e.g. &#39;2012-12-24T00:00:00+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**description** | **String** | Any description on the order |  [optional] |
|**lastModified** | **OffsetDateTime** | The date and time the order was last modified |  [optional] |
|**location** | **String** | The customer location for this order |  [optional] |
|**orderId** | **String** | The order id (a.k.a OrderCd) for the order |  [optional] |
|**orderQty** | **Double** | The total number of items on the order |  [optional] |
|**orderTotal** | **Double** | The total amount on the order |  [optional] |
|**requestOn** | **OffsetDateTime** | The date the order is requested  Unless a specific time zone offset is included (e.g. &#39;2012-12-24T00:00:00+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**shippingScheduledDate** | **OffsetDateTime** | The date shipment is scheduled  Unless a specific time zone offset is included (e.g. &#39;2012-12-24T00:00:00+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**status** | **String** | The current status of the order |  [optional] |
|**type** | **String** | The type of the order |  [optional] |



