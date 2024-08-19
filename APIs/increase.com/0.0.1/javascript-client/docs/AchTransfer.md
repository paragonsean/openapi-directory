# IncreaseApi.AchTransfer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The Account to which the transfer belongs. | 
**accountNumber** | **String** | The destination account number. | 
**addendum** | **String** | Additional information that will be sent to the recipient. | 
**amount** | **Number** | The transfer amount in USD cents. A positive amount indicates a credit transfer pushing funds to the receiving account. A negative amount indicates a debit transfer pulling funds from the receiving account. | 
**approval** | [**TransferApproval**](TransferApproval.md) |  | 
**cancellation** | [**TransferCancellation**](TransferCancellation.md) |  | 
**companyDescriptiveDate** | **String** | The description of the date of the transfer. | 
**companyDiscretionaryData** | **String** | The data you chose to associate with the transfer. | 
**companyEntryDescription** | **String** | The description of the transfer you set to be shown to the recipient. | 
**companyName** | **String** | The name by which the recipient knows you. | 
**createdAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the transfer was created. | 
**currency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transfer&#39;s currency. For ACH transfers this is always equal to &#x60;usd&#x60;. | 
**effectiveDate** | **Date** | The transfer effective date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | 
**externalAccountId** | **String** | The identifier of the External Account the transfer was made to, if any. | 
**funding** | **String** | The type of the account to which the transfer will be sent. | 
**id** | **String** | The ACH transfer&#39;s identifier. | 
**individualId** | **String** | Your identifer for the transfer recipient. | 
**individualName** | **String** | The name of the transfer recipient. This value is information and not verified by the recipient&#39;s bank. | 
**network** | **String** | The transfer&#39;s network. | 
**notificationsOfChange** | [**[ACHNotificationOfChange]**](ACHNotificationOfChange.md) | If the receiving bank accepts the transfer but notifies that future transfers should use different details, this will contain those details. | 
**_return** | [**ACHTransferReturn**](ACHTransferReturn.md) |  | 
**routingNumber** | **String** | The American Bankers&#39; Association (ABA) Routing Transit Number (RTN). | 
**standardEntryClassCode** | **String** | The Standard Entry Class (SEC) code to use for the transfer. | 
**statementDescriptor** | **String** | The descriptor that will show on the recipient&#39;s bank statement. | 
**status** | **String** | The lifecycle status of the transfer. | 
**submission** | [**ACHTransferSubmission**](ACHTransferSubmission.md) |  | 
**transactionId** | **String** | The ID for the transaction funding the transfer. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;ach_transfer&#x60;. | 



## Enum: CurrencyEnum


* `CAD` (value: `"CAD"`)

* `CHF` (value: `"CHF"`)

* `EUR` (value: `"EUR"`)

* `GBP` (value: `"GBP"`)

* `JPY` (value: `"JPY"`)

* `USD` (value: `"USD"`)





## Enum: FundingEnum


* `checking` (value: `"checking"`)

* `savings` (value: `"savings"`)





## Enum: NetworkEnum


* `ach` (value: `"ach"`)





## Enum: StandardEntryClassCodeEnum


* `corporate_credit_or_debit` (value: `"corporate_credit_or_debit"`)

* `prearranged_payments_and_deposit` (value: `"prearranged_payments_and_deposit"`)

* `internet_initiated` (value: `"internet_initiated"`)





## Enum: StatusEnum


* `pending_approval` (value: `"pending_approval"`)

* `canceled` (value: `"canceled"`)

* `pending_reviewing` (value: `"pending_reviewing"`)

* `pending_submission` (value: `"pending_submission"`)

* `submitted` (value: `"submitted"`)

* `returned` (value: `"returned"`)

* `requires_attention` (value: `"requires_attention"`)

* `rejected` (value: `"rejected"`)





## Enum: TypeEnum


* `ach_transfer` (value: `"ach_transfer"`)




