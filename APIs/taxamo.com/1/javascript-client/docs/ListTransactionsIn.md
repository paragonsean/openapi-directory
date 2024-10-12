# Taxamo.ListTransactionsIn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currencyCode** | **String** | Three letter ISO currency code. | [optional] 
**filterText** | **String** | Filtering expression | [optional] 
**format** | **String** | Output format - supports &#39;csv&#39; value for this operation. | [optional] 
**hasNote** | **Boolean** | Return only transactions with a note field set. | [optional] 
**invoiceNumber** | **String** | Transaction invoice number. | [optional] 
**keyOrCustomId** | **String** | Taxamo provided transaction key or custom id | [optional] 
**limit** | **Number** | Limit (no more than 1000, defaults to 100). | [optional] 
**offset** | **Number** | Offset | [optional] 
**orderDateFrom** | **String** | Order date from in yyyy-MM-dd format. | [optional] 
**orderDateTo** | **String** | Order date to in yyyy-MM-dd format. | [optional] 
**originalTransactionKey** | **String** | Taxamo provided original transaction key | [optional] 
**sortReverse** | **Boolean** | If true, results are sorted in descending order. | [optional] 
**statuses** | **String** | Comma separated list of of transaction statuses. &#39;N&#39; - unconfirmed transaction, &#39;C&#39; - confirmed transaction. | [optional] 
**taxCountryCode** | **String** | Two letter ISO tax country code. | [optional] 
**taxCountryCodes** | **String** | Comma separated list of two letter ISO tax country codes. | [optional] 
**totalAmountGreaterThan** | **String** | Return only transactions with total amount greater than given number. Transactions with total amount equal to a given number (e.g. 0) are not returned. | [optional] 
**totalAmountLessThan** | **String** | Return only transactions with total amount less than a given number. Transactions with total amount equal to a given number (e.g. 1) are not returned. | [optional] 


