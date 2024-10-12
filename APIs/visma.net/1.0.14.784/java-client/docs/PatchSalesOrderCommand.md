

# PatchSalesOrderCommand

The Visma.net.ERP.SalesOrders.Api.Application.Commands.PatchSalesOrder.PatchSalesOrderCommand is a command for updating parts of a sales order

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billing** | [**PatchSalesOrderBillingDto**](PatchSalesOrderBillingDto.md) |  |  [optional] |
|**branchId** | **String** | The branch with which this order is associated. |  [optional] |
|**cancelBy** | **OffsetDateTime** | Cancel by date for the order.  Unless a specific time zone offset is specified with the date (e.g. &#39;2012-12-24T13:30:23+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**currencyId** | **String** | Override the CurrencyId for the order. Must be a valid currency Id. |  [optional] |
|**customer** | [**PatchSalesOrderCustomerDto**](PatchSalesOrderCustomerDto.md) |  |  [optional] |
|**date** | **OffsetDateTime** | Sets the order date of the order.  Unless a specific time zone offset is specified with the date (e.g. &#39;2012-12-24T13:30:23+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**description** | **String** | Description for the order  &lt;br&gt;Note that text fields should not contain any personally identifiable or otherwise sensitive data |  [optional] |
|**financialInformation** | [**PatchSalesOrderFinancialInfoDto**](PatchSalesOrderFinancialInfoDto.md) |  |  [optional] |
|**freight** | [**PatchSalesOrderFreightDto**](PatchSalesOrderFreightDto.md) |  |  [optional] |
|**note** | **String** | Any note to apply to the order header. |  [optional] |
|**originalOrderId** | **String** | Sets the unique identifier of the original order |  [optional] |
|**originalOrderType** | **String** | Sets the type code for the original sales order |  [optional] |
|**ownerId** | **String** | Sets the owner (employee) for the order |  [optional] |
|**paymentSettings** | [**PatchSalesOrderPaymentSettingsDto**](PatchSalesOrderPaymentSettingsDto.md) |  |  [optional] |
|**print** | [**SalesOrderPrintDto**](SalesOrderPrintDto.md) |  |  [optional] |
|**projectId** | **String** | The project with which this sales order is associated |  [optional] |
|**requestOn** | **OffsetDateTime** | Sets the requested on date for the order.  Unless a specific time zone offset is specified with the date (e.g. &#39;2012-12-24T13:30:23+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**salesPersonId** | **String** | Sets default sales person for the order |  [optional] |
|**shipping** | [**PatchSalesOrderShippingDto**](PatchSalesOrderShippingDto.md) |  |  [optional] |
|**status** | **String** | Sets the status code for the order. Must be \&quot;Open\&quot;, \&quot;Hold\&quot; or \&quot;BackOrder\&quot;. |  [optional] |
|**taxZoneId** | **String** | Override the TaxZoneId for the order |  [optional] |
|**useReplacementCostForMarginAndProfit** | **Boolean** | When this option is set to &#x60;true&#x60;, the &#x60;costTotal&#x60; of the order will be calculated based on &#x60;replacementUnitCost&#x60;.  If option is set to &#x60;false&#x60;, the &#x60;costTotal&#x60; will be calculated based on &#x60;unitCost&#x60; |  [optional] |



