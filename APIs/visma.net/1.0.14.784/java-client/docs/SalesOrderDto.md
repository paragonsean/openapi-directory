

# SalesOrderDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attachments** | [**List&lt;AttachmentDto&gt;**](AttachmentDto.md) | The attachments of the order |  [optional] |
|**billing** | [**SalesOrderBillingDto**](SalesOrderBillingDto.md) |  |  [optional] |
|**branch** | [**CdDescriptionPairDto**](CdDescriptionPairDto.md) |  |  [optional] |
|**cancelBy** | **OffsetDateTime** | The cancel date for the order  Unless a specific time zone offset is included (e.g. &#39;2012-12-24T00:00:00+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**createdBy** | **String** | The user name of the creator of the order. If the order was created by an API call this field will be null or empty. |  [optional] |
|**currencyId** | **String** | CurrencyId for the order. |  [optional] |
|**customer** | [**SalesOrderCustomerDto**](SalesOrderCustomerDto.md) |  |  [optional] |
|**date** | **OffsetDateTime** | Date the order was submitted  Unless a specific time zone offset is included (e.g. &#39;2012-12-24T00:00:00+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**description** | **String** | Description of the order |  [optional] |
|**financialInformation** | [**SalesOrderFinancialInfoDto**](SalesOrderFinancialInfoDto.md) |  |  [optional] |
|**freight** | [**SalesOrderFreightDto**](SalesOrderFreightDto.md) |  |  [optional] |
|**isRotRutDeductable** | **Boolean** | Whether the order is ROT/RUT deductible |  [optional] |
|**lastModified** | **OffsetDateTime** | Date the order was last modified  Unless a specific time zone offset is included (e.g. &#39;2012-12-24T00:00:00+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**note** | **String** | Any notes on the order |  [optional] |
|**orderId** | **String** | The unique identifier of the order |  [optional] |
|**orderQty** | **Double** | The total quantity of inventory items in the order |  [optional] |
|**origin** | [**SalesOrderOriginDto**](SalesOrderOriginDto.md) |  |  [optional] |
|**originalOrderId** | **String** | The unique identifier of the original order |  [optional] |
|**originalOrderType** | **String** | The type code for the original sales order |  [optional] |
|**owner** | [**EmployeeDto**](EmployeeDto.md) |  |  [optional] |
|**paymentSettings** | [**SalesOrderPaymentDto**](SalesOrderPaymentDto.md) |  |  [optional] |
|**print** | [**SalesOrderPrintDto**](SalesOrderPrintDto.md) |  |  [optional] |
|**project** | [**ProjectDto**](ProjectDto.md) |  |  [optional] |
|**requestOn** | **OffsetDateTime** | Date the order was requested  Unless a specific time zone offset is included (e.g. &#39;2012-12-24T00:00:00+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**salesPerson** | [**SalesPersonDto**](SalesPersonDto.md) |  |  [optional] |
|**shipping** | [**SalesOrderShippingDto**](SalesOrderShippingDto.md) |  |  [optional] |
|**status** | [**SalesOrderStatusDto**](SalesOrderStatusDto.md) |  |  [optional] |
|**totals** | [**SalesOrderTotalsDto**](SalesOrderTotalsDto.md) |  |  [optional] |
|**type** | **String** | The type code for the sales order |  [optional] |
|**useReplacementCostForMarginAndProfit** | **Boolean** | When this option is set to &#x60;true&#x60;, the &#x60;costTotal&#x60; of the order will be calculated based on &#x60;replacementUnitCost&#x60;.  If option is set to &#x60;false&#x60;, the &#x60;costTotal&#x60; will be calculated based on &#x60;unitCost&#x60; |  [optional] |
|**version** | **byte[]** | An internal order version used for detecting concurrent updates to an order |  [optional] |



