

# PurchaseInvoiceInvoiceLine


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accounting** | [**PurchaseInvoiceAccountingDetails**](PurchaseInvoiceAccountingDetails.md) |  |  [optional] |
|**allowanceCharge** | **BigDecimal** | DEPRECATED - use allowance_charges. |  [optional] |
|**allowanceChargeArray** | [**List&lt;PurchaseInvoiceInvoiceLineAllowanceCharge&gt;**](PurchaseInvoiceInvoiceLineAllowanceCharge.md) |  |  [optional] |
|**allowanceCharges** | **List&lt;BigDecimal&gt;** | Deprecated. |  [optional] |
|**amountExcludingTax** | **BigDecimal** | The amount excluding Tax. This is equal to quantity x price_amount + ∑ allowance_charges. |  [optional] |
|**amountExcludingVat** | **BigDecimal** | DEPRECATED - use amount_excluding_tax. The amount excluding VAT. |  [optional] |
|**description** | **String** | The description for the invoice line. |  [optional] |
|**name** | **String** | A short name for the invoice line. |  [optional] |
|**periodEnd** | **String** | The end date of the period this invoice line relates to. Format \&quot;YYYY-MM-DD\&quot;. |  [optional] |
|**periodStart** | **String** | The start date of the period this invoice line relates to. Format \&quot;YYYY-MM-DD\&quot;. |  [optional] |
|**price** | [**PurchaseInvoiceInvoiceLinePrice**](PurchaseInvoiceInvoiceLinePrice.md) |  |  [optional] |
|**tax** | [**PurchaseInvoiceTax**](PurchaseInvoiceTax.md) |  |  [optional] |
|**units** | [**PurchaseInvoiceInvoiceLineItem**](PurchaseInvoiceInvoiceLineItem.md) |  |  [optional] |
|**vat** | [**VATDetails**](VATDetails.md) |  |  [optional] |



