# XeroAccountingApi.ExpenseClaim

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amountDue** | **Number** | The amount due to be paid for an expense claim | [optional] [readonly] 
**amountPaid** | **Number** | The amount still to pay for an expense claim | [optional] [readonly] 
**expenseClaimID** | **String** | Xero generated unique identifier for an expense claim | [optional] 
**paymentDueDate** | **String** | The date when the expense claim is due to be paid YYYY-MM-DD | [optional] [readonly] 
**payments** | [**[Payment]**](Payment.md) | See Payments | [optional] 
**receiptID** | **String** | The Xero identifier for the Receipt e.g. e59a2c7f-1306-4078-a0f3-73537afcbba9 | [optional] 
**receipts** | [**[Receipt]**](Receipt.md) |  | [optional] 
**reportingDate** | **String** | The date the expense claim will be reported in Xero YYYY-MM-DD | [optional] [readonly] 
**status** | **String** | Current status of an expense claim – see status types | [optional] 
**total** | **Number** | The total of an expense claim being paid | [optional] [readonly] 
**updatedDateUTC** | **String** | Last modified date UTC format | [optional] [readonly] 
**user** | [**User**](User.md) |  | [optional] 



## Enum: StatusEnum


* `SUBMITTED` (value: `"SUBMITTED"`)

* `AUTHORISED` (value: `"AUTHORISED"`)

* `PAID` (value: `"PAID"`)

* `VOIDED` (value: `"VOIDED"`)

* `DELETED` (value: `"DELETED"`)




