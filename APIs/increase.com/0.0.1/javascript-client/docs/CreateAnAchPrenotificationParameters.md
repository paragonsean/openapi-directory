# IncreaseApi.CreateAnAchPrenotificationParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountNumber** | **String** | The account number for the destination account. | 
**addendum** | **String** | Additional information that will be sent to the recipient. | [optional] 
**companyDescriptiveDate** | **String** | The description of the date of the transfer. | [optional] 
**companyDiscretionaryData** | **String** | The data you choose to associate with the transfer. | [optional] 
**companyEntryDescription** | **String** | The description of the transfer you wish to be shown to the recipient. | [optional] 
**companyName** | **String** | The name by which the recipient knows you. | [optional] 
**creditDebitIndicator** | **String** | Whether the Prenotification is for a future debit or credit. | [optional] 
**effectiveDate** | **Date** | The transfer effective date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**individualId** | **String** | Your identifer for the transfer recipient. | [optional] 
**individualName** | **String** | The name of the transfer recipient. This value is information and not verified by the recipient&#39;s bank. | [optional] 
**routingNumber** | **String** | The American Bankers&#39; Association (ABA) Routing Transit Number (RTN) for the destination account. | 
**standardEntryClassCode** | **String** | The Standard Entry Class (SEC) code to use for the ACH Prenotification. | [optional] 



## Enum: CreditDebitIndicatorEnum


* `credit` (value: `"credit"`)

* `debit` (value: `"debit"`)





## Enum: StandardEntryClassCodeEnum


* `corporate_credit_or_debit` (value: `"corporate_credit_or_debit"`)

* `prearranged_payments_and_deposit` (value: `"prearranged_payments_and_deposit"`)

* `internet_initiated` (value: `"internet_initiated"`)




