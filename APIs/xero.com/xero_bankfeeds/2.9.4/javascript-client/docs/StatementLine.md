# XeroBankFeedsApi.StatementLine

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | Transaction amount | [optional] 
**chequeNumber** | **String** | The cheque/check number | [optional] 
**creditDebitIndicator** | [**CreditDebitIndicator**](CreditDebitIndicator.md) |  | [optional] 
**description** | **String** | Transaction description | [optional] 
**payeeName** | **String** | Typically the merchant or payee name | [optional] 
**postedDate** | **Date** | The date that the transaction was processed or cleared as seen in internet banking ISO-8601 YYYY-MM-DD | [optional] 
**reference** | **String** | Optional field to enhance the Description | [optional] 
**transactionId** | **String** | Financial institute&#39;s internal transaction identifier. If provided this field is factored into duplicate detection. | [optional] 


