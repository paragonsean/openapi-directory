

# BankTransaction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bankAccount** | [**Account**](Account.md) |  |  |
|**bankTransactionID** | **UUID** | Xero generated unique identifier for bank transaction |  [optional] |
|**contact** | [**Contact**](Contact.md) |  |  [optional] |
|**currencyCode** | **CurrencyCode** |  |  [optional] |
|**currencyRate** | **Double** | Exchange rate to base currency when money is spent or received. e.g.0.7500 Only used for bank transactions in non base currency. If this isn’t specified for non base currency accounts then either the user-defined rate (preference) or the XE.com day rate will be used. Setting currency is only supported on overpayments. |  [optional] |
|**date** | **String** | Date of transaction – YYYY-MM-DD |  [optional] |
|**hasAttachments** | **Boolean** | Boolean to indicate if a bank transaction has an attachment |  [optional] [readonly] |
|**isReconciled** | **Boolean** | Boolean to show if transaction is reconciled |  [optional] |
|**lineAmountTypes** | **LineAmountTypes** |  |  [optional] |
|**lineItems** | [**List&lt;LineItem&gt;**](LineItem.md) | See LineItems |  |
|**overpaymentID** | **UUID** | Xero generated unique identifier for an Overpayment. This will be returned on BankTransactions with a Type of SPEND-OVERPAYMENT or RECEIVE-OVERPAYMENT |  [optional] [readonly] |
|**prepaymentID** | **UUID** | Xero generated unique identifier for a Prepayment. This will be returned on BankTransactions with a Type of SPEND-PREPAYMENT or RECEIVE-PREPAYMENT |  [optional] [readonly] |
|**reference** | **String** | Reference for the transaction. Only supported for SPEND and RECEIVE transactions. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | See Bank Transaction Status Codes |  [optional] |
|**statusAttributeString** | **String** | A string to indicate if a invoice status |  [optional] |
|**subTotal** | **Double** | Total of bank transaction excluding taxes |  [optional] |
|**total** | **Double** | Total of bank transaction tax inclusive |  [optional] |
|**totalTax** | **Double** | Total tax on bank transaction |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | See Bank Transaction Types |  |
|**updatedDateUTC** | **String** | Last modified date UTC format |  [optional] [readonly] |
|**url** | **String** | URL link to a source document – shown as “Go to App Name” |  [optional] |
|**validationErrors** | [**List&lt;ValidationError&gt;**](ValidationError.md) | Displays array of validation error messages from the API |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| AUTHORISED | &quot;AUTHORISED&quot; |
| DELETED | &quot;DELETED&quot; |
| VOIDED | &quot;VOIDED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| RECEIVE | &quot;RECEIVE&quot; |
| RECEIVE_OVERPAYMENT | &quot;RECEIVE-OVERPAYMENT&quot; |
| RECEIVE_PREPAYMENT | &quot;RECEIVE-PREPAYMENT&quot; |
| SPEND | &quot;SPEND&quot; |
| SPEND_OVERPAYMENT | &quot;SPEND-OVERPAYMENT&quot; |
| SPEND_PREPAYMENT | &quot;SPEND-PREPAYMENT&quot; |
| RECEIVE_TRANSFER | &quot;RECEIVE-TRANSFER&quot; |
| SPEND_TRANSFER | &quot;SPEND-TRANSFER&quot; |



