

# PurchaseInvoiceDocumentTotals


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**payable** | **BigDecimal** | The total invoice amount payable including tax. |  [optional] |
|**prepaid** | **BigDecimal** | The amount already paid. |  [optional] |
|**rounding** | **BigDecimal** | The difference between the payable amount and the total invoice amount including tax. |  [optional] |
|**total** | **BigDecimal** | The total invoice amount, including tax. This is equal to the sum of the invoice_lines (amount_excluding_tax + tax.amount) and the allowances and charges. |  [optional] |



