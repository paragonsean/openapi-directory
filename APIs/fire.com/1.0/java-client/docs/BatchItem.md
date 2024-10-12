

# BatchItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Long** | The amount of funds to send. In cent or pence |  [optional] |
|**amountAfterCharges** | **Long** | The amount of the transfer after fees and taxes. in pence or cent. |  [optional] |
|**batchItemUuid** | **String** | A UUID for this item. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The datestamp the batch was created - ISO format - e.g. 2018-04-04T00:53:21.910Z |  [optional] |
|**feeAmount** | **Long** | The fee charged by fire.com for the payment. In pence or cent. |  [optional] |
|**icanFrom** | **Long** | The Fire account ID of the source account. |  [optional] |
|**icanTo** | **Long** | The Fire account ID for the fire.com account the funds are sent to. |  [optional] |
|**lastUpdated** | **OffsetDateTime** | The datestamp of the last action on this batch - ISO format - e.g. 2018-04-04T10:48:53.540Z |  [optional] |
|**ref** | **String** | The reference on the transaction. |  [optional] |
|**refId** | **Long** | The ID of the resulting payment in your account. Can be used to retrieve the transaction using the https://api.fire.com/business/v1/accounts/{accountId}/transactions/{refId} endpoint. |  [optional] |
|**result** | [**BatchItemResult**](BatchItemResult.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | status of the batch if internal trasnfer |  [optional] |
|**taxAmount** | **Long** | Any taxes/duty collected by fire.com for this payments (e.g. stamp duty etc). In pence or cent. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUBMITTED | &quot;SUBMITTED&quot; |
| REMOVED | &quot;REMOVED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |



