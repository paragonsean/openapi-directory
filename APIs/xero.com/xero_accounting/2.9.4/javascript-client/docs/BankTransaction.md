# XeroAccountingApi.BankTransaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bankAccount** | [**Account**](Account.md) |  | 
**bankTransactionID** | **String** | Xero generated unique identifier for bank transaction | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**currencyCode** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**currencyRate** | **Number** | Exchange rate to base currency when money is spent or received. e.g.0.7500 Only used for bank transactions in non base currency. If this isn’t specified for non base currency accounts then either the user-defined rate (preference) or the XE.com day rate will be used. Setting currency is only supported on overpayments. | [optional] 
**date** | **String** | Date of transaction – YYYY-MM-DD | [optional] 
**hasAttachments** | **Boolean** | Boolean to indicate if a bank transaction has an attachment | [optional] [readonly] [default to false]
**isReconciled** | **Boolean** | Boolean to show if transaction is reconciled | [optional] 
**lineAmountTypes** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**lineItems** | [**[LineItem]**](LineItem.md) | See LineItems | 
**overpaymentID** | **String** | Xero generated unique identifier for an Overpayment. This will be returned on BankTransactions with a Type of SPEND-OVERPAYMENT or RECEIVE-OVERPAYMENT | [optional] [readonly] 
**prepaymentID** | **String** | Xero generated unique identifier for a Prepayment. This will be returned on BankTransactions with a Type of SPEND-PREPAYMENT or RECEIVE-PREPAYMENT | [optional] [readonly] 
**reference** | **String** | Reference for the transaction. Only supported for SPEND and RECEIVE transactions. | [optional] 
**status** | **String** | See Bank Transaction Status Codes | [optional] 
**statusAttributeString** | **String** | A string to indicate if a invoice status | [optional] 
**subTotal** | **Number** | Total of bank transaction excluding taxes | [optional] 
**total** | **Number** | Total of bank transaction tax inclusive | [optional] 
**totalTax** | **Number** | Total tax on bank transaction | [optional] 
**type** | **String** | See Bank Transaction Types | 
**updatedDateUTC** | **String** | Last modified date UTC format | [optional] [readonly] 
**url** | **String** | URL link to a source document – shown as “Go to App Name” | [optional] 
**validationErrors** | [**[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 



## Enum: StatusEnum


* `AUTHORISED` (value: `"AUTHORISED"`)

* `DELETED` (value: `"DELETED"`)

* `VOIDED` (value: `"VOIDED"`)





## Enum: TypeEnum


* `RECEIVE` (value: `"RECEIVE"`)

* `RECEIVE-OVERPAYMENT` (value: `"RECEIVE-OVERPAYMENT"`)

* `RECEIVE-PREPAYMENT` (value: `"RECEIVE-PREPAYMENT"`)

* `SPEND` (value: `"SPEND"`)

* `SPEND-OVERPAYMENT` (value: `"SPEND-OVERPAYMENT"`)

* `SPEND-PREPAYMENT` (value: `"SPEND-PREPAYMENT"`)

* `RECEIVE-TRANSFER` (value: `"RECEIVE-TRANSFER"`)

* `SPEND-TRANSFER` (value: `"SPEND-TRANSFER"`)




