

# CreateAnAchPrenotificationParameters


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountNumber** | **String** | The account number for the destination account. |  |
|**addendum** | **String** | Additional information that will be sent to the recipient. |  [optional] |
|**companyDescriptiveDate** | **String** | The description of the date of the transfer. |  [optional] |
|**companyDiscretionaryData** | **String** | The data you choose to associate with the transfer. |  [optional] |
|**companyEntryDescription** | **String** | The description of the transfer you wish to be shown to the recipient. |  [optional] |
|**companyName** | **String** | The name by which the recipient knows you. |  [optional] |
|**creditDebitIndicator** | [**CreditDebitIndicatorEnum**](#CreditDebitIndicatorEnum) | Whether the Prenotification is for a future debit or credit. |  [optional] |
|**effectiveDate** | **LocalDate** | The transfer effective date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**individualId** | **String** | Your identifer for the transfer recipient. |  [optional] |
|**individualName** | **String** | The name of the transfer recipient. This value is information and not verified by the recipient&#39;s bank. |  [optional] |
|**routingNumber** | **String** | The American Bankers&#39; Association (ABA) Routing Transit Number (RTN) for the destination account. |  |
|**standardEntryClassCode** | [**StandardEntryClassCodeEnum**](#StandardEntryClassCodeEnum) | The Standard Entry Class (SEC) code to use for the ACH Prenotification. |  [optional] |



## Enum: CreditDebitIndicatorEnum

| Name | Value |
|---- | -----|
| CREDIT | &quot;credit&quot; |
| DEBIT | &quot;debit&quot; |



## Enum: StandardEntryClassCodeEnum

| Name | Value |
|---- | -----|
| CORPORATE_CREDIT_OR_DEBIT | &quot;corporate_credit_or_debit&quot; |
| PREARRANGED_PAYMENTS_AND_DEPOSIT | &quot;prearranged_payments_and_deposit&quot; |
| INTERNET_INITIATED | &quot;internet_initiated&quot; |



