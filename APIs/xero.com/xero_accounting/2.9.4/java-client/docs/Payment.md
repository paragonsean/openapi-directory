

# Payment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | [**Account**](Account.md) |  |  [optional] |
|**amount** | **Double** | The amount of the payment. Must be less than or equal to the outstanding amount owing on the invoice e.g. 200.00 |  [optional] |
|**bankAccountNumber** | **String** | The suppliers bank account number the payment is being made to |  [optional] |
|**batchPaymentID** | **UUID** | Present if the payment was created as part of a batch. |  [optional] |
|**code** | **String** | Code of account you are using to make the payment e.g. 001 (note- not all accounts have a code value) |  [optional] |
|**creditNote** | [**CreditNote**](CreditNote.md) |  |  [optional] |
|**creditNoteNumber** | **String** | Number of invoice or credit note you are applying payment to e.g. INV-4003 |  [optional] |
|**currencyRate** | **Double** | Exchange rate when payment is received. Only used for non base currency invoices and credit notes e.g. 0.7500 |  [optional] |
|**date** | **String** | Date the payment is being made (YYYY-MM-DD) e.g. 2009-09-06 |  [optional] |
|**details** | **String** | The information to appear on the supplier&#39;s bank account |  [optional] |
|**hasAccount** | **Boolean** | A boolean to indicate if a contact has an validation errors |  [optional] |
|**hasValidationErrors** | **Boolean** | A boolean to indicate if a contact has an validation errors |  [optional] |
|**invoice** | [**Invoice**](Invoice.md) |  |  [optional] |
|**invoiceNumber** | **String** | Number of invoice or credit note you are applying payment to e.g.INV-4003 |  [optional] |
|**isReconciled** | **Boolean** | An optional parameter for the payment. A boolean indicating whether you would like the payment to be created as reconciled when using PUT, or whether a payment has been reconciled when using GET |  [optional] |
|**overpayment** | [**Overpayment**](Overpayment.md) |  |  [optional] |
|**particulars** | **String** | The suppliers bank account number the payment is being made to |  [optional] |
|**paymentID** | **UUID** | The Xero identifier for an Payment e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9 |  [optional] |
|**paymentType** | [**PaymentTypeEnum**](#PaymentTypeEnum) | See Payment Types. |  [optional] [readonly] |
|**prepayment** | [**Prepayment**](Prepayment.md) |  |  [optional] |
|**reference** | **String** | An optional description for the payment e.g. Direct Debit |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the payment. |  [optional] |
|**statusAttributeString** | **String** | A string to indicate if a invoice status |  [optional] |
|**updatedDateUTC** | **String** | UTC timestamp of last update to the payment |  [optional] [readonly] |
|**validationErrors** | [**List&lt;ValidationError&gt;**](ValidationError.md) | Displays array of validation error messages from the API |  [optional] |



## Enum: PaymentTypeEnum

| Name | Value |
|---- | -----|
| ACCRECPAYMENT | &quot;ACCRECPAYMENT&quot; |
| ACCPAYPAYMENT | &quot;ACCPAYPAYMENT&quot; |
| ARCREDITPAYMENT | &quot;ARCREDITPAYMENT&quot; |
| APCREDITPAYMENT | &quot;APCREDITPAYMENT&quot; |
| AROVERPAYMENTPAYMENT | &quot;AROVERPAYMENTPAYMENT&quot; |
| ARPREPAYMENTPAYMENT | &quot;ARPREPAYMENTPAYMENT&quot; |
| APPREPAYMENTPAYMENT | &quot;APPREPAYMENTPAYMENT&quot; |
| APOVERPAYMENTPAYMENT | &quot;APOVERPAYMENTPAYMENT&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| AUTHORISED | &quot;AUTHORISED&quot; |
| DELETED | &quot;DELETED&quot; |



