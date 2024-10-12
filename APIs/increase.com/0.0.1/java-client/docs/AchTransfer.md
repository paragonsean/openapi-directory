

# AchTransfer

ACH transfers move funds between your Increase account and any other account accessible by the Automated Clearing House (ACH).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The Account to which the transfer belongs. |  |
|**accountNumber** | **String** | The destination account number. |  |
|**addendum** | **String** | Additional information that will be sent to the recipient. |  |
|**amount** | **Integer** | The transfer amount in USD cents. A positive amount indicates a credit transfer pushing funds to the receiving account. A negative amount indicates a debit transfer pulling funds from the receiving account. |  |
|**approval** | [**TransferApproval**](TransferApproval.md) |  |  |
|**cancellation** | [**TransferCancellation**](TransferCancellation.md) |  |  |
|**companyDescriptiveDate** | **String** | The description of the date of the transfer. |  |
|**companyDiscretionaryData** | **String** | The data you chose to associate with the transfer. |  |
|**companyEntryDescription** | **String** | The description of the transfer you set to be shown to the recipient. |  |
|**companyName** | **String** | The name by which the recipient knows you. |  |
|**createdAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the transfer was created. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transfer&#39;s currency. For ACH transfers this is always equal to &#x60;usd&#x60;. |  |
|**effectiveDate** | **LocalDate** | The transfer effective date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  |
|**externalAccountId** | **String** | The identifier of the External Account the transfer was made to, if any. |  |
|**funding** | [**FundingEnum**](#FundingEnum) | The type of the account to which the transfer will be sent. |  |
|**id** | **String** | The ACH transfer&#39;s identifier. |  |
|**individualId** | **String** | Your identifer for the transfer recipient. |  |
|**individualName** | **String** | The name of the transfer recipient. This value is information and not verified by the recipient&#39;s bank. |  |
|**network** | [**NetworkEnum**](#NetworkEnum) | The transfer&#39;s network. |  |
|**notificationsOfChange** | [**List&lt;ACHNotificationOfChange&gt;**](ACHNotificationOfChange.md) | If the receiving bank accepts the transfer but notifies that future transfers should use different details, this will contain those details. |  |
|**_return** | [**ACHTransferReturn**](ACHTransferReturn.md) |  |  |
|**routingNumber** | **String** | The American Bankers&#39; Association (ABA) Routing Transit Number (RTN). |  |
|**standardEntryClassCode** | [**StandardEntryClassCodeEnum**](#StandardEntryClassCodeEnum) | The Standard Entry Class (SEC) code to use for the transfer. |  |
|**statementDescriptor** | **String** | The descriptor that will show on the recipient&#39;s bank statement. |  |
|**status** | [**StatusEnum**](#StatusEnum) | The lifecycle status of the transfer. |  |
|**submission** | [**ACHTransferSubmission**](ACHTransferSubmission.md) |  |  |
|**transactionId** | **String** | The ID for the transaction funding the transfer. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;ach_transfer&#x60;. |  |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| CAD | &quot;CAD&quot; |
| CHF | &quot;CHF&quot; |
| EUR | &quot;EUR&quot; |
| GBP | &quot;GBP&quot; |
| JPY | &quot;JPY&quot; |
| USD | &quot;USD&quot; |



## Enum: FundingEnum

| Name | Value |
|---- | -----|
| CHECKING | &quot;checking&quot; |
| SAVINGS | &quot;savings&quot; |



## Enum: NetworkEnum

| Name | Value |
|---- | -----|
| ACH | &quot;ach&quot; |



## Enum: StandardEntryClassCodeEnum

| Name | Value |
|---- | -----|
| CORPORATE_CREDIT_OR_DEBIT | &quot;corporate_credit_or_debit&quot; |
| PREARRANGED_PAYMENTS_AND_DEPOSIT | &quot;prearranged_payments_and_deposit&quot; |
| INTERNET_INITIATED | &quot;internet_initiated&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING_APPROVAL | &quot;pending_approval&quot; |
| CANCELED | &quot;canceled&quot; |
| PENDING_REVIEWING | &quot;pending_reviewing&quot; |
| PENDING_SUBMISSION | &quot;pending_submission&quot; |
| SUBMITTED | &quot;submitted&quot; |
| RETURNED | &quot;returned&quot; |
| REQUIRES_ATTENTION | &quot;requires_attention&quot; |
| REJECTED | &quot;rejected&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACH_TRANSFER | &quot;ach_transfer&quot; |



