

# Batch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**batchName** | **String** | An optional name you give to the batch at creation time |  [optional] |
|**batchUuid** | **String** | A UUID for this item. |  [optional] |
|**callbackUrl** | **String** | An optional POST URL that all events for this batch will be sent to. |  [optional] |
|**currency** | **String** | All payments in the batch must be the same currency. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The datestamp the batch was created - ISO format - e.g. 2018-04-04T00:53:21.910Z |  [optional] |
|**jobNumber** | **String** | An optional job number you can give to the batch to help link it to your own system. |  [optional] |
|**lastUpdated** | **OffsetDateTime** | The datestamp of the last action on this batch - ISO format - e.g. 2018-04-04T10:48:53.540Z |  [optional] |
|**numberOfItemsFailed** | **Long** | Once processed, a count of the number of items that didn’t process successfully. |  [optional] |
|**numberOfItemsSubmitted** | **Long** | A count of the number of items in the batch |  [optional] |
|**numberOfItemsSucceeded** | **Long** | Once processed, a count of the number of items that processed successfully. |  [optional] |
|**sourceName** | **String** | A string describing where the batch originated - for instance the name of the API token that was used, or showing that the batch was automatically created by fire.com (in the case of a new payee batch). |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | status of the batch object |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the batch - can be one of the listed enums |  [optional] |
|**valueOfItemsFailed** | **Long** | Once processed, a sum of the value of items that didn’t process successfully. Specified in pence or cent. |  [optional] |
|**valueOfItemsSubmitted** | **Long** | A sum of the value of items in the batch. Specified in pence or cent. |  [optional] |
|**valueOfItemsSucceeded** | **Long** | Once processed, a sum of the value of items that processed successfully. Specified in pence or cent. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING_APPROVAL | &quot;PENDING_APPROVAL&quot; |
| REJECTED | &quot;REJECTED&quot; |
| COMPLETE | &quot;COMPLETE&quot; |
| OPEN | &quot;OPEN&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| PENDING_PARENT_BATCH_APPROVAL | &quot;PENDING_PARENT_BATCH_APPROVAL&quot; |
| READY_FOR_PROCESSING | &quot;READY_FOR_PROCESSING&quot; |
| PROCESSING | &quot;PROCESSING&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INTERNAL_TRANSFER | &quot;INTERNAL_TRANSFER&quot; |
| BANK_TRANSFER | &quot;BANK_TRANSFER&quot; |
| INTERNATIONAL_TRANSFER | &quot;INTERNATIONAL_TRANSFER&quot; |
| NEW_PAYEE | &quot;NEW_PAYEE&quot; |



