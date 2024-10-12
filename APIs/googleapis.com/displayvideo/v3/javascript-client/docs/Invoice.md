# DisplayVideo360Api.Invoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budgetInvoiceGroupingId** | **String** | The budget grouping ID for this invoice. This field will only be set if the invoice level of the corresponding billing profile was set to \&quot;Budget invoice grouping ID\&quot;. | [optional] 
**budgetSummaries** | [**[BudgetSummary]**](BudgetSummary.md) | The list of summarized information for each budget associated with this invoice. This field will only be set if the invoice detail level of the corresponding billing profile was set to \&quot;Budget level PO\&quot;. | [optional] 
**correctedInvoiceId** | **String** | The ID of the original invoice being adjusted by this invoice, if applicable. May appear on the invoice PDF as &#x60;Reference invoice number&#x60;. If replaced_invoice_ids is set, this field will be empty. | [optional] 
**currencyCode** | **String** | The currency used in the invoice in ISO 4217 format. | [optional] 
**displayName** | **String** | The display name of the invoice. | [optional] 
**dueDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**invoiceId** | **String** | The unique ID of the invoice. | [optional] 
**invoiceType** | **String** | The type of invoice document. | [optional] 
**issueDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**name** | **String** | The resource name of the invoice. | [optional] 
**nonBudgetMicros** | **String** | The total amount of costs or adjustments not tied to a particular budget, in micros of the invoice&#39;s currency. For example, if currency_code is &#x60;USD&#x60;, then 1000000 represents one US dollar. | [optional] 
**paymentsAccountId** | **String** | The ID of the payments account the invoice belongs to. Appears on the invoice PDF as &#x60;Billing Account Number&#x60;. | [optional] 
**paymentsProfileId** | **String** | The ID of the payments profile the invoice belongs to. Appears on the invoice PDF as &#x60;Billing ID&#x60;. | [optional] 
**pdfUrl** | **String** | The URL to download a PDF copy of the invoice. This URL is user specific and requires a valid OAuth 2.0 access token to access. The access token must be provided in an &#x60;Authorization: Bearer&#x60; HTTP header and be authorized for one of the following scopes: * &#x60;https://www.googleapis.com/auth/display-video-mediaplanning&#x60; * &#x60;https://www.googleapis.com/auth/display-video&#x60; The URL will be valid for 7 days after retrieval of this invoice object or until this invoice is retrieved again. | [optional] 
**purchaseOrderNumber** | **String** | Purchase order number associated with the invoice. | [optional] 
**replacedInvoiceIds** | **[String]** | The ID(s) of any originally issued invoice that is being cancelled by this invoice, if applicable. Multiple invoices may be listed if those invoices are being consolidated into a single invoice. May appear on invoice PDF as &#x60;Replaced invoice numbers&#x60;. If corrected_invoice_id is set, this field will be empty. | [optional] 
**serviceDateRange** | [**DateRange**](DateRange.md) |  | [optional] 
**subtotalAmountMicros** | **String** | The pre-tax subtotal amount, in micros of the invoice&#39;s currency. For example, if currency_code is &#x60;USD&#x60;, then 1000000 represents one US dollar. | [optional] 
**totalAmountMicros** | **String** | The invoice total amount, in micros of the invoice&#39;s currency. For example, if currency_code is &#x60;USD&#x60;, then 1000000 represents one US dollar. | [optional] 
**totalTaxAmountMicros** | **String** | The sum of all taxes in invoice, in micros of the invoice&#39;s currency. For example, if currency_code is &#x60;USD&#x60;, then 1000000 represents one US dollar. | [optional] 



## Enum: InvoiceTypeEnum


* `UNSPECIFIED` (value: `"INVOICE_TYPE_UNSPECIFIED"`)

* `CREDIT` (value: `"INVOICE_TYPE_CREDIT"`)

* `INVOICE` (value: `"INVOICE_TYPE_INVOICE"`)




