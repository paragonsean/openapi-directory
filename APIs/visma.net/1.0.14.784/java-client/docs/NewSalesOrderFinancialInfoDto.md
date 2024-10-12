

# NewSalesOrderFinancialInfoDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cashDiscountDate** | **OffsetDateTime** | The date when the cash discount is available for the invoice created for the order. Default date is set based on the terms selected in the order.  Unless a specific time zone offset is specified with the date (e.g. &#39;2012-12-24T13:30:23+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**dueDate** | **OffsetDateTime** | The due date for the invoice created for the order. Default due date is set according to the credit terms.  Unless a specific time zone offset is specified with the date (e.g. &#39;2012-12-24T13:30:23+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**invoiceDate** | **OffsetDateTime** | Sets the invoice date of the invoice that will be generated for the order.  Unless a specific time zone offset is specified with the date (e.g. &#39;2012-12-24T13:30:23+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**invoiceId** | **String** | The reference number of the invoice generated for this order.  This can be used if the numbering sequence assigned to invoices is configured for manual numbering. |  [optional] |
|**invoiceSeparately** | **Boolean** | Sets if the order should be invoiced/billed separately |  [optional] |
|**postPeriod** | **String** | The post period for the invoice. This can be used to override the financial period. Must be a valid existing financial period. |  [optional] |



