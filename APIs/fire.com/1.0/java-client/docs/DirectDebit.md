

# DirectDebit


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Long** | Value of the payment |  [optional] |
|**currency** | [**Currency**](Currency.md) |  |  [optional] |
|**dateCreated** | **OffsetDateTime** | Date the direct debit was created. Milliseconds since the epoch (1970). |  [optional] |
|**directDebitReference** | **String** | The direct debit reference. |  [optional] |
|**directDebitUuid** | **String** | The UUID for the direct debit payment |  [optional] |
|**isDDIC** | **Boolean** | DDIC is a Direct Debit Indemnity Claim (i.e.a refund). If if the DD is requested to be refunded it is marked isDDIC true. |  [optional] |
|**lastUpdated** | **OffsetDateTime** | Date the direct debit was last updated. Milliseconds since the epoch (1970). |  [optional] |
|**mandateUUid** | **String** | The UUID for the mandate |  [optional] |
|**originatorAlias** | **String** | The Alias of the party who sets up the direct debit. |  [optional] |
|**originatorName** | **String** | The creator of the party who sets up the direct debit. |  [optional] |
|**originatorReference** | **String** | Set by party who sets up the direct debit. |  [optional] |
|**schemeRejectReason** | **String** | Reason why rejected |  [optional] |
|**schemeRejectReasonCode** | [**SchemeRejectReasonCodeEnum**](#SchemeRejectReasonCodeEnum) | The reject code returned by the bank indicating an issue with the direct debit. Each ARRUD code represents a rejection reason. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The statuses of the direct debit payments associated with the mandate. * &#39;RECIEVED&#39; - Direct Debit has been recieved * &#39;REJECT_REQUESTED&#39; - The direct debit has a rejected request associated with it * &#39;REJECT_READY_FOR_PROCESSING&#39;  * &#39;REJECT_RECORD_IN_PROGRESS&#39; * &#39;REJECT_RECORDED&#39; * &#39;REJECT_FILE_CREATED&#39; * &#39;REJECT_FILE_SENT&#39; * &#39;COLLECTED&#39; - Direct debit collected * &#39;REFUND_REQUESTED&#39; - Refund requested on direct debit * &#39;REFUND_RECORD_IN_PROGRESS&#39; - Refund in progress on direct debit * &#39;REFUND_RECORDED&#39; * &#39;REFUND_FILE_CREATED&#39; * &#39;REFUND_FILE_SENT&#39;   |  [optional] |
|**targetIcan** | **Long** | The ican of your fire account that the money was taken from |  [optional] |
|**targetPayeeId** | **Long** | The payee that was created when the DD was processed |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the direct debit. |  [optional] |



## Enum: SchemeRejectReasonCodeEnum

| Name | Value |
|---- | -----|
| _0 | &quot;0&quot; |
| _1 | &quot;1&quot; |
| _2 | &quot;2&quot; |
| _3 | &quot;3&quot; |
| _4 | &quot;4&quot; |
| _5 | &quot;5&quot; |
| _6 | &quot;6&quot; |
| _7 | &quot;7&quot; |
| _8 | &quot;8&quot; |
| _9 | &quot;9&quot; |
| A | &quot;A&quot; |
| B | &quot;B&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| RECIEVED | &quot;RECIEVED&quot; |
| REJECT_REQUESTED | &quot;REJECT_REQUESTED&quot; |
| REJECT_READY_FOR_PROCESSING | &quot;REJECT_READY_FOR_PROCESSING&quot; |
| REJECT_RECORD_IN_PROGRESS | &quot;REJECT_RECORD_IN_PROGRESS&quot; |
| REJECT_RECORDED | &quot;REJECT_RECORDED&quot; |
| REJECT_FILE_CREATED | &quot;REJECT_FILE_CREATED&quot; |
| REJECT_FILE_SENT | &quot;REJECT_FILE_SENT&quot; |
| COLLECTED | &quot;COLLECTED&quot; |
| REFUND_REQUESTED | &quot;REFUND_REQUESTED&quot; |
| REFUND_RECORD_IN_PROGRESS | &quot;REFUND_RECORD_IN_PROGRESS&quot; |
| REFUND_RECORDED | &quot;REFUND_RECORDED&quot; |
| REFUND_FILE_CREATED | &quot;REFUND_FILE_CREATED&quot; |
| REFUND_FILE_SENT | &quot;REFUND_FILE_SENT&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| FIRST_COLLECTION | &quot;FIRST_COLLECTION&quot; |
| ONGOING_COLLECTION | &quot;ONGOING_COLLECTION&quot; |
| REPRESENTED_COLLECTION | &quot;REPRESENTED_COLLECTION&quot; |
| FINAL_COLLECTION | &quot;FINAL_COLLECTION&quot; |



