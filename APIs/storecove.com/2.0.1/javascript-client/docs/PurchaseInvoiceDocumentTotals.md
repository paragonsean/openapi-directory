# StorecoveApi.PurchaseInvoiceDocumentTotals

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payable** | **Number** | The total invoice amount payable including tax. | [optional] 
**prepaid** | **Number** | The amount already paid. | [optional] 
**rounding** | **Number** | The difference between the payable amount and the total invoice amount including tax. | [optional] 
**total** | **Number** | The total invoice amount, including tax. This is equal to the sum of the invoice_lines (amount_excluding_tax + tax.amount) and the allowances and charges. | [optional] 


