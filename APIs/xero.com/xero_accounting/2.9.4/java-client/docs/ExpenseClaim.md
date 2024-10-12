

# ExpenseClaim


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amountDue** | **Double** | The amount due to be paid for an expense claim |  [optional] [readonly] |
|**amountPaid** | **Double** | The amount still to pay for an expense claim |  [optional] [readonly] |
|**expenseClaimID** | **UUID** | Xero generated unique identifier for an expense claim |  [optional] |
|**paymentDueDate** | **String** | The date when the expense claim is due to be paid YYYY-MM-DD |  [optional] [readonly] |
|**payments** | [**List&lt;Payment&gt;**](Payment.md) | See Payments |  [optional] |
|**receiptID** | **UUID** | The Xero identifier for the Receipt e.g. e59a2c7f-1306-4078-a0f3-73537afcbba9 |  [optional] |
|**receipts** | [**List&lt;Receipt&gt;**](Receipt.md) |  |  [optional] |
|**reportingDate** | **String** | The date the expense claim will be reported in Xero YYYY-MM-DD |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Current status of an expense claim – see status types |  [optional] |
|**total** | **Double** | The total of an expense claim being paid |  [optional] [readonly] |
|**updatedDateUTC** | **String** | Last modified date UTC format |  [optional] [readonly] |
|**user** | [**User**](User.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUBMITTED | &quot;SUBMITTED&quot; |
| AUTHORISED | &quot;AUTHORISED&quot; |
| PAID | &quot;PAID&quot; |
| VOIDED | &quot;VOIDED&quot; |
| DELETED | &quot;DELETED&quot; |



