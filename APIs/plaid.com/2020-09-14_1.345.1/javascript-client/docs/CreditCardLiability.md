# ThePlaidApi.CreditCardLiability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The ID of the account that this liability belongs to. | 
**aprs** | [**[APR]**](APR.md) | The various interest rates that apply to the account. APR information is not provided by all card issuers; if APR data is not available, this array will be empty. | 
**isOverdue** | **Boolean** | true if a payment is currently overdue. Availability for this field is limited. | 
**lastPaymentAmount** | **Number** | The amount of the last payment. | 
**lastPaymentDate** | **Date** | The date of the last payment. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). Availability for this field is limited. | 
**lastStatementBalance** | **Number** | The total amount owed as of the last statement issued | 
**lastStatementIssueDate** | **Date** | The date of the last statement. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). | 
**minimumPaymentAmount** | **Number** | The minimum payment due for the next billing cycle. | 
**nextPaymentDueDate** | **Date** | The due date for the next payment. The due date is &#x60;null&#x60; if a payment is not expected. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). | 


