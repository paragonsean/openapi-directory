# FireFinancialServicesBusinessApi.DirectDebit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | Value of the payment | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**dateCreated** | **Date** | Date the direct debit was created. Milliseconds since the epoch (1970). | [optional] 
**directDebitReference** | **String** | The direct debit reference. | [optional] 
**directDebitUuid** | **String** | The UUID for the direct debit payment | [optional] 
**isDDIC** | **Boolean** | DDIC is a Direct Debit Indemnity Claim (i.e.a refund). If if the DD is requested to be refunded it is marked isDDIC true. | [optional] 
**lastUpdated** | **Date** | Date the direct debit was last updated. Milliseconds since the epoch (1970). | [optional] 
**mandateUUid** | **String** | The UUID for the mandate | [optional] 
**originatorAlias** | **String** | The Alias of the party who sets up the direct debit. | [optional] 
**originatorName** | **String** | The creator of the party who sets up the direct debit. | [optional] 
**originatorReference** | **String** | Set by party who sets up the direct debit. | [optional] 
**schemeRejectReason** | **String** | Reason why rejected | [optional] 
**schemeRejectReasonCode** | **String** | The reject code returned by the bank indicating an issue with the direct debit. Each ARRUD code represents a rejection reason. | [optional] 
**status** | **String** | The statuses of the direct debit payments associated with the mandate. * &#39;RECIEVED&#39; - Direct Debit has been recieved * &#39;REJECT_REQUESTED&#39; - The direct debit has a rejected request associated with it * &#39;REJECT_READY_FOR_PROCESSING&#39;  * &#39;REJECT_RECORD_IN_PROGRESS&#39; * &#39;REJECT_RECORDED&#39; * &#39;REJECT_FILE_CREATED&#39; * &#39;REJECT_FILE_SENT&#39; * &#39;COLLECTED&#39; - Direct debit collected * &#39;REFUND_REQUESTED&#39; - Refund requested on direct debit * &#39;REFUND_RECORD_IN_PROGRESS&#39; - Refund in progress on direct debit * &#39;REFUND_RECORDED&#39; * &#39;REFUND_FILE_CREATED&#39; * &#39;REFUND_FILE_SENT&#39;   | [optional] 
**targetIcan** | **Number** | The ican of your fire account that the money was taken from | [optional] 
**targetPayeeId** | **Number** | The payee that was created when the DD was processed | [optional] 
**type** | **String** | The type of the direct debit. | [optional] 



## Enum: SchemeRejectReasonCodeEnum


* `0` (value: `"0"`)

* `1` (value: `"1"`)

* `2` (value: `"2"`)

* `3` (value: `"3"`)

* `4` (value: `"4"`)

* `5` (value: `"5"`)

* `6` (value: `"6"`)

* `7` (value: `"7"`)

* `8` (value: `"8"`)

* `9` (value: `"9"`)

* `A` (value: `"A"`)

* `B` (value: `"B"`)





## Enum: StatusEnum


* `RECIEVED` (value: `"RECIEVED"`)

* `REJECT_REQUESTED` (value: `"REJECT_REQUESTED"`)

* `REJECT_READY_FOR_PROCESSING` (value: `"REJECT_READY_FOR_PROCESSING"`)

* `REJECT_RECORD_IN_PROGRESS` (value: `"REJECT_RECORD_IN_PROGRESS"`)

* `REJECT_RECORDED` (value: `"REJECT_RECORDED"`)

* `REJECT_FILE_CREATED` (value: `"REJECT_FILE_CREATED"`)

* `REJECT_FILE_SENT` (value: `"REJECT_FILE_SENT"`)

* `COLLECTED` (value: `"COLLECTED"`)

* `REFUND_REQUESTED` (value: `"REFUND_REQUESTED"`)

* `REFUND_RECORD_IN_PROGRESS` (value: `"REFUND_RECORD_IN_PROGRESS"`)

* `REFUND_RECORDED` (value: `"REFUND_RECORDED"`)

* `REFUND_FILE_CREATED` (value: `"REFUND_FILE_CREATED"`)

* `REFUND_FILE_SENT` (value: `"REFUND_FILE_SENT"`)





## Enum: TypeEnum


* `FIRST_COLLECTION` (value: `"FIRST_COLLECTION"`)

* `ONGOING_COLLECTION` (value: `"ONGOING_COLLECTION"`)

* `REPRESENTED_COLLECTION` (value: `"REPRESENTED_COLLECTION"`)

* `FINAL_COLLECTION` (value: `"FINAL_COLLECTION"`)




