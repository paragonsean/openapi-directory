# FireFinancialServicesBusinessApi.BatchItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The amount of funds to send. In cent or pence | [optional] 
**amountAfterCharges** | **Number** | The amount of the transfer after fees and taxes. in pence or cent. | [optional] 
**batchItemUuid** | **String** | A UUID for this item. | [optional] 
**dateCreated** | **Date** | The datestamp the batch was created - ISO format - e.g. 2018-04-04T00:53:21.910Z | [optional] 
**feeAmount** | **Number** | The fee charged by fire.com for the payment. In pence or cent. | [optional] 
**icanFrom** | **Number** | The Fire account ID of the source account. | [optional] 
**icanTo** | **Number** | The Fire account ID for the fire.com account the funds are sent to. | [optional] 
**lastUpdated** | **Date** | The datestamp of the last action on this batch - ISO format - e.g. 2018-04-04T10:48:53.540Z | [optional] 
**ref** | **String** | The reference on the transaction. | [optional] 
**refId** | **Number** | The ID of the resulting payment in your account. Can be used to retrieve the transaction using the https://api.fire.com/business/v1/accounts/{accountId}/transactions/{refId} endpoint. | [optional] 
**result** | [**BatchItemResult**](BatchItemResult.md) |  | [optional] 
**status** | **String** | status of the batch if internal trasnfer | [optional] 
**taxAmount** | **Number** | Any taxes/duty collected by fire.com for this payments (e.g. stamp duty etc). In pence or cent. | [optional] 



## Enum: StatusEnum


* `SUBMITTED` (value: `"SUBMITTED"`)

* `REMOVED` (value: `"REMOVED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)




