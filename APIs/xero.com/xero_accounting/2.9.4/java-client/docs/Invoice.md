

# Invoice


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amountCredited** | **Double** | Sum of all credit notes, over-payments and pre-payments applied to invoice |  [optional] [readonly] |
|**amountDue** | **Double** | Amount remaining to be paid on invoice |  [optional] [readonly] |
|**amountPaid** | **Double** | Sum of payments received for invoice |  [optional] [readonly] |
|**attachments** | [**List&lt;Attachment&gt;**](Attachment.md) | Displays array of attachments from the API |  [optional] |
|**brandingThemeID** | **UUID** | See BrandingThemes |  [optional] |
|**ciSDeduction** | **Double** | CIS deduction for UK contractors |  [optional] [readonly] |
|**ciSRate** | **Double** | CIS Deduction rate for the organisation |  [optional] [readonly] |
|**contact** | [**Contact**](Contact.md) |  |  [optional] |
|**creditNotes** | [**List&lt;CreditNote&gt;**](CreditNote.md) | Details of credit notes that have been applied to an invoice |  [optional] [readonly] |
|**currencyCode** | **CurrencyCode** |  |  [optional] |
|**currencyRate** | **Double** | The currency rate for a multicurrency invoice. If no rate is specified, the XE.com day rate is used. (max length &#x3D; [18].[6]) |  [optional] |
|**date** | **String** | Date invoice was issued – YYYY-MM-DD. If the Date element is not specified it will default to the current date based on the timezone setting of the organisation |  [optional] |
|**dueDate** | **String** | Date invoice is due – YYYY-MM-DD |  [optional] |
|**expectedPaymentDate** | **String** | Shown on sales invoices (Accounts Receivable) when this has been set |  [optional] |
|**fullyPaidOnDate** | **String** | The date the invoice was fully paid. Only returned on fully paid invoices |  [optional] [readonly] |
|**hasAttachments** | **Boolean** | boolean to indicate if an invoice has an attachment |  [optional] [readonly] |
|**hasErrors** | **Boolean** | A boolean to indicate if a invoice has an validation errors |  [optional] |
|**invoiceID** | **UUID** | Xero generated unique identifier for invoice |  [optional] |
|**invoiceNumber** | **String** | ACCREC – Unique alpha numeric code identifying invoice (when missing will auto-generate from your Organisation Invoice Settings) (max length &#x3D; 255) |  [optional] |
|**isDiscounted** | **Boolean** | boolean to indicate if an invoice has a discount |  [optional] [readonly] |
|**lineAmountTypes** | **LineAmountTypes** |  |  [optional] |
|**lineItems** | [**List&lt;LineItem&gt;**](LineItem.md) | See LineItems |  [optional] |
|**overpayments** | [**List&lt;Overpayment&gt;**](Overpayment.md) | See Overpayments |  [optional] [readonly] |
|**payments** | [**List&lt;Payment&gt;**](Payment.md) | See Payments |  [optional] [readonly] |
|**plannedPaymentDate** | **String** | Shown on bills (Accounts Payable) when this has been set |  [optional] |
|**prepayments** | [**List&lt;Prepayment&gt;**](Prepayment.md) | See Prepayments |  [optional] [readonly] |
|**reference** | **String** | ACCREC only – additional reference number |  [optional] |
|**repeatingInvoiceID** | **UUID** | Xero generated unique identifier for repeating invoices |  [optional] |
|**sentToContact** | **Boolean** | Boolean to set whether the invoice in the Xero app should be marked as “sent”. This can be set only on invoices that have been approved |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | See Invoice Status Codes |  [optional] |
|**statusAttributeString** | **String** | A string to indicate if a invoice status |  [optional] |
|**subTotal** | **Double** | Total of invoice excluding taxes |  [optional] [readonly] |
|**total** | **Double** | Total of Invoice tax inclusive (i.e. SubTotal + TotalTax). This will be ignored if it doesn’t equal the sum of the LineAmounts |  [optional] [readonly] |
|**totalDiscount** | **Double** | Total of discounts applied on the invoice line items |  [optional] [readonly] |
|**totalTax** | **Double** | Total tax on invoice |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | See Invoice Types |  [optional] |
|**updatedDateUTC** | **String** | Last modified date UTC format |  [optional] [readonly] |
|**url** | **String** | URL link to a source document – shown as “Go to [appName]” in the Xero app |  [optional] |
|**validationErrors** | [**List&lt;ValidationError&gt;**](ValidationError.md) | Displays array of validation error messages from the API |  [optional] |
|**warnings** | [**List&lt;ValidationError&gt;**](ValidationError.md) | Displays array of warning messages from the API |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;DRAFT&quot; |
| SUBMITTED | &quot;SUBMITTED&quot; |
| DELETED | &quot;DELETED&quot; |
| AUTHORISED | &quot;AUTHORISED&quot; |
| PAID | &quot;PAID&quot; |
| VOIDED | &quot;VOIDED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACCPAY | &quot;ACCPAY&quot; |
| ACCPAYCREDIT | &quot;ACCPAYCREDIT&quot; |
| APOVERPAYMENT | &quot;APOVERPAYMENT&quot; |
| APPREPAYMENT | &quot;APPREPAYMENT&quot; |
| ACCREC | &quot;ACCREC&quot; |
| ACCRECCREDIT | &quot;ACCRECCREDIT&quot; |
| AROVERPAYMENT | &quot;AROVERPAYMENT&quot; |
| ARPREPAYMENT | &quot;ARPREPAYMENT&quot; |



