

# BatchPayment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | [**Account**](Account.md) |  |  [optional] |
|**amount** | **Double** | The amount of the payment. Must be less than or equal to the outstanding amount owing on the invoice e.g. 200.00 |  [optional] |
|**batchPaymentID** | **UUID** | The Xero generated unique identifier for the bank transaction (read-only) |  [optional] [readonly] |
|**code** | **String** | (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find &amp; Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero. |  [optional] |
|**date** | **String** | Date the payment is being made (YYYY-MM-DD) e.g. 2009-09-06 |  [optional] |
|**dateString** | **String** | Date the payment is being made (YYYY-MM-DD) e.g. 2009-09-06 |  [optional] |
|**details** | **String** | (Non-NZ Only) These details are sent to the org’s bank as a reference for the batch payment transaction. They will also show with the batch payment transaction in the bank reconciliation Find &amp; Match screen. Depending on your individual bank, the detail may also show on the bank statement imported into Xero. Maximum field length &#x3D; 18 |  [optional] |
|**isReconciled** | **String** | Booelan that tells you if the batch payment has been reconciled (read-only) |  [optional] [readonly] |
|**narrative** | **String** | (UK Only) Only shows on the statement line in Xero. Max length &#x3D;18 |  [optional] |
|**particulars** | **String** | (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find &amp; Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero. |  [optional] |
|**payments** | [**List&lt;Payment&gt;**](Payment.md) | An array of payments |  [optional] |
|**reference** | **String** | (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find &amp; Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | AUTHORISED or DELETED (read-only). New batch payments will have a status of AUTHORISED. It is not possible to delete batch payments via the API. |  [optional] [readonly] |
|**totalAmount** | **String** | The total of the payments that make up the batch (read-only) |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | PAYBATCH for bill payments or RECBATCH for sales invoice payments (read-only) |  [optional] [readonly] |
|**updatedDateUTC** | **String** | UTC timestamp of last update to the payment |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| AUTHORISED | &quot;AUTHORISED&quot; |
| DELETED | &quot;DELETED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PAYBATCH | &quot;PAYBATCH&quot; |
| RECBATCH | &quot;RECBATCH&quot; |



