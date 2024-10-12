# FireFinancialServicesBusinessApi.Batch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batchName** | **String** | An optional name you give to the batch at creation time | [optional] 
**batchUuid** | **String** | A UUID for this item. | [optional] 
**callbackUrl** | **String** | An optional POST URL that all events for this batch will be sent to. | [optional] 
**currency** | **String** | All payments in the batch must be the same currency. | [optional] 
**dateCreated** | **Date** | The datestamp the batch was created - ISO format - e.g. 2018-04-04T00:53:21.910Z | [optional] 
**jobNumber** | **String** | An optional job number you can give to the batch to help link it to your own system. | [optional] 
**lastUpdated** | **Date** | The datestamp of the last action on this batch - ISO format - e.g. 2018-04-04T10:48:53.540Z | [optional] 
**numberOfItemsFailed** | **Number** | Once processed, a count of the number of items that didn’t process successfully. | [optional] 
**numberOfItemsSubmitted** | **Number** | A count of the number of items in the batch | [optional] 
**numberOfItemsSucceeded** | **Number** | Once processed, a count of the number of items that processed successfully. | [optional] 
**sourceName** | **String** | A string describing where the batch originated - for instance the name of the API token that was used, or showing that the batch was automatically created by fire.com (in the case of a new payee batch). | [optional] 
**status** | **String** | status of the batch object | [optional] 
**type** | **String** | The type of the batch - can be one of the listed enums | [optional] 
**valueOfItemsFailed** | **Number** | Once processed, a sum of the value of items that didn’t process successfully. Specified in pence or cent. | [optional] 
**valueOfItemsSubmitted** | **Number** | A sum of the value of items in the batch. Specified in pence or cent. | [optional] 
**valueOfItemsSucceeded** | **Number** | Once processed, a sum of the value of items that processed successfully. Specified in pence or cent. | [optional] 



## Enum: StatusEnum


* `PENDING_APPROVAL` (value: `"PENDING_APPROVAL"`)

* `REJECTED` (value: `"REJECTED"`)

* `COMPLETE` (value: `"COMPLETE"`)

* `OPEN` (value: `"OPEN"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `PENDING_PARENT_BATCH_APPROVAL` (value: `"PENDING_PARENT_BATCH_APPROVAL"`)

* `READY_FOR_PROCESSING` (value: `"READY_FOR_PROCESSING"`)

* `PROCESSING` (value: `"PROCESSING"`)





## Enum: TypeEnum


* `INTERNAL_TRANSFER` (value: `"INTERNAL_TRANSFER"`)

* `BANK_TRANSFER` (value: `"BANK_TRANSFER"`)

* `INTERNATIONAL_TRANSFER` (value: `"INTERNATIONAL_TRANSFER"`)

* `NEW_PAYEE` (value: `"NEW_PAYEE"`)




