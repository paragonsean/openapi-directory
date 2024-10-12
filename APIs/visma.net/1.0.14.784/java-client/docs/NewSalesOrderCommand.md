

# NewSalesOrderCommand


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billing** | [**NewSalesOrderBillingDto**](NewSalesOrderBillingDto.md) |  |  [optional] |
|**branchId** | **String** | The branch with which this order is associated. Prio for setting the Branch ID being:  &lt;list type&#x3D;\&quot;number\&quot;&gt;&lt;item&gt;BranchID set in body&lt;/item&gt;&lt;item&gt;BranchID from call header&lt;/item&gt;&lt;item&gt;BranchID from customer location&lt;/item&gt;&lt;item&gt;Company&#39;s default branch ID&lt;/item&gt;&lt;/list&gt; |  [optional] |
|**cancelBy** | **OffsetDateTime** | Sets the cancel by date for the order to create. If not supplied, the order type&#39;s days to keep will be added to the current date to determine the value of this field  Unless a specific time zone offset is specified with the date (e.g. &#39;2012-12-24T13:30:23+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**currencyId** | **String** | Override the CurrencyId for the order. Must be a valid currency Id. If not specified, the customer&#39;s currency is used if not null. If null, company base currency is used |  [optional] |
|**customer** | [**NewSalesOrderCustomerDto**](NewSalesOrderCustomerDto.md) |  |  |
|**date** | **OffsetDateTime** | Sets the order date of the order to create. If not supplied, the current date will be used  Unless a specific time zone offset is specified with the date (e.g. &#39;2012-12-24T13:30:23+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**description** | **String** | Sets the description for the order to create  &lt;br&gt;Note that text fields should not contain any personally identifiable or otherwise sensitive data |  [optional] |
|**financialInformation** | [**NewSalesOrderFinancialInfoDto**](NewSalesOrderFinancialInfoDto.md) |  |  [optional] |
|**freight** | [**NewSalesOrderFreightDto**](NewSalesOrderFreightDto.md) |  |  [optional] |
|**note** | **String** | Any note to apply to the order header. |  [optional] |
|**orderId** | **String** | Sets the new id that should be assigned to the new sales order.  This is required if the specified Visma.net.ERP.SalesOrders.Api.Application.Commands.NewSalesOrder.NewSalesOrderCommand.Type has manual numbering set up. If not it should be null or empty. |  [optional] |
|**orderLines** | [**List&lt;NewSalesOrderLineDto&gt;**](NewSalesOrderLineDto.md) | The lines that are added to the order upon creation |  [optional] |
|**originalOrderId** | **String** | Sets the unique identifier of the original order |  [optional] |
|**originalOrderType** | **String** | Sets the type code for the original sales order |  [optional] |
|**ownerId** | **String** | Sets the owner (employee) for the order |  [optional] |
|**paymentSettings** | [**NewSalesOrderPaymentSettings**](NewSalesOrderPaymentSettings.md) |  |  [optional] |
|**print** | [**SalesOrderPrintDto**](SalesOrderPrintDto.md) |  |  [optional] |
|**projectId** | **String** | The project with which this sales order is associated |  [optional] |
|**requestOn** | **OffsetDateTime** | Sets the requested on date for the order to create. If not supplied, the current date will be used  Unless a specific time zone offset is specified with the date (e.g. &#39;2012-12-24T13:30:23+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**salesPersonId** | **String** | Sets default sales person for the order |  [optional] |
|**shipping** | [**NewSalesOrderShippingDto**](NewSalesOrderShippingDto.md) |  |  [optional] |
|**status** | **String** | Sets the initial status code for the order. Must be null, empty or one of \&quot;Open\&quot; or \&quot;Hold\&quot;. If not supplied the value will be determined by the sales order type. |  [optional] |
|**taxZoneId** | **String** | Override the TaxZoneId for the order. If not specified, the customer&#39;s location&#39;s TaxZoneId will be used |  [optional] |
|**type** | **String** | Sets the type id of an active sales order type to create |  |
|**useReplacementCostForMarginAndProfit** | **Boolean** | When this option is set to &#x60;true&#x60;, the &#x60;costTotal&#x60; of the order will be calculated based on &#x60;replacementUnitCost&#x60;.  If option is set to &#x60;false&#x60;, the &#x60;costTotal&#x60; will be calculated based on &#x60;unitCost&#x60; |  [optional] |



