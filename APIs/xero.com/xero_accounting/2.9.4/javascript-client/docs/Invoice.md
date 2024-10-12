# XeroAccountingApi.Invoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amountCredited** | **Number** | Sum of all credit notes, over-payments and pre-payments applied to invoice | [optional] [readonly] 
**amountDue** | **Number** | Amount remaining to be paid on invoice | [optional] [readonly] 
**amountPaid** | **Number** | Sum of payments received for invoice | [optional] [readonly] 
**attachments** | [**[Attachment]**](Attachment.md) | Displays array of attachments from the API | [optional] 
**brandingThemeID** | **String** | See BrandingThemes | [optional] 
**cISDeduction** | **Number** | CIS deduction for UK contractors | [optional] [readonly] 
**cISRate** | **Number** | CIS Deduction rate for the organisation | [optional] [readonly] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**creditNotes** | [**[CreditNote]**](CreditNote.md) | Details of credit notes that have been applied to an invoice | [optional] [readonly] 
**currencyCode** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**currencyRate** | **Number** | The currency rate for a multicurrency invoice. If no rate is specified, the XE.com day rate is used. (max length &#x3D; [18].[6]) | [optional] 
**date** | **String** | Date invoice was issued – YYYY-MM-DD. If the Date element is not specified it will default to the current date based on the timezone setting of the organisation | [optional] 
**dueDate** | **String** | Date invoice is due – YYYY-MM-DD | [optional] 
**expectedPaymentDate** | **String** | Shown on sales invoices (Accounts Receivable) when this has been set | [optional] 
**fullyPaidOnDate** | **String** | The date the invoice was fully paid. Only returned on fully paid invoices | [optional] [readonly] 
**hasAttachments** | **Boolean** | boolean to indicate if an invoice has an attachment | [optional] [readonly] [default to false]
**hasErrors** | **Boolean** | A boolean to indicate if a invoice has an validation errors | [optional] [default to false]
**invoiceID** | **String** | Xero generated unique identifier for invoice | [optional] 
**invoiceNumber** | **String** | ACCREC – Unique alpha numeric code identifying invoice (when missing will auto-generate from your Organisation Invoice Settings) (max length &#x3D; 255) | [optional] 
**isDiscounted** | **Boolean** | boolean to indicate if an invoice has a discount | [optional] [readonly] 
**lineAmountTypes** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**lineItems** | [**[LineItem]**](LineItem.md) | See LineItems | [optional] 
**overpayments** | [**[Overpayment]**](Overpayment.md) | See Overpayments | [optional] [readonly] 
**payments** | [**[Payment]**](Payment.md) | See Payments | [optional] [readonly] 
**plannedPaymentDate** | **String** | Shown on bills (Accounts Payable) when this has been set | [optional] 
**prepayments** | [**[Prepayment]**](Prepayment.md) | See Prepayments | [optional] [readonly] 
**reference** | **String** | ACCREC only – additional reference number | [optional] 
**repeatingInvoiceID** | **String** | Xero generated unique identifier for repeating invoices | [optional] 
**sentToContact** | **Boolean** | Boolean to set whether the invoice in the Xero app should be marked as “sent”. This can be set only on invoices that have been approved | [optional] 
**status** | **String** | See Invoice Status Codes | [optional] 
**statusAttributeString** | **String** | A string to indicate if a invoice status | [optional] 
**subTotal** | **Number** | Total of invoice excluding taxes | [optional] [readonly] 
**total** | **Number** | Total of Invoice tax inclusive (i.e. SubTotal + TotalTax). This will be ignored if it doesn’t equal the sum of the LineAmounts | [optional] [readonly] 
**totalDiscount** | **Number** | Total of discounts applied on the invoice line items | [optional] [readonly] 
**totalTax** | **Number** | Total tax on invoice | [optional] [readonly] 
**type** | **String** | See Invoice Types | [optional] 
**updatedDateUTC** | **String** | Last modified date UTC format | [optional] [readonly] 
**url** | **String** | URL link to a source document – shown as “Go to [appName]” in the Xero app | [optional] 
**validationErrors** | [**[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 
**warnings** | [**[ValidationError]**](ValidationError.md) | Displays array of warning messages from the API | [optional] 



## Enum: StatusEnum


* `DRAFT` (value: `"DRAFT"`)

* `SUBMITTED` (value: `"SUBMITTED"`)

* `DELETED` (value: `"DELETED"`)

* `AUTHORISED` (value: `"AUTHORISED"`)

* `PAID` (value: `"PAID"`)

* `VOIDED` (value: `"VOIDED"`)





## Enum: TypeEnum


* `ACCPAY` (value: `"ACCPAY"`)

* `ACCPAYCREDIT` (value: `"ACCPAYCREDIT"`)

* `APOVERPAYMENT` (value: `"APOVERPAYMENT"`)

* `APPREPAYMENT` (value: `"APPREPAYMENT"`)

* `ACCREC` (value: `"ACCREC"`)

* `ACCRECCREDIT` (value: `"ACCRECCREDIT"`)

* `AROVERPAYMENT` (value: `"AROVERPAYMENT"`)

* `ARPREPAYMENT` (value: `"ARPREPAYMENT"`)




