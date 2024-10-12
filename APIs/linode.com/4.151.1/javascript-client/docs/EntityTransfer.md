# LinodeApi.EntityTransfer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Date** | When this transfer was created.  | [optional] 
**entities** | [**EntityTransferEntities**](EntityTransferEntities.md) |  | [optional] 
**expiry** | **Date** | When this transfer expires. Transfers will automatically expire 24 hours after creation.  | [optional] 
**isSender** | **Boolean** | If the requesting account created this transfer.  | [optional] 
**status** | **String** | The status of the transfer request.  &#x60;accepted&#x60;: The transfer has been accepted by another user and is currently in progress. Transfers can take up to 3 hours to complete.  &#x60;cancelled&#x60;: The transfer has been cancelled by the sender.  &#x60;completed&#x60;: The transfer has completed successfully.  &#x60;failed&#x60;: The transfer has failed after initiation.  &#x60;pending&#x60;: The transfer is ready to be accepted.  &#x60;stale&#x60;: The transfer has exceeded its expiration date. It can no longer be accepted or cancelled.  | [optional] 
**token** | **String** | The token used to identify and accept or cancel this transfer.  | [optional] 
**updated** | **Date** | When this transfer was last updated.  | [optional] 



## Enum: StatusEnum


* `accepted` (value: `"accepted"`)

* `cancelled` (value: `"cancelled"`)

* `completed` (value: `"completed"`)

* `failed` (value: `"failed"`)

* `pending` (value: `"pending"`)

* `stale` (value: `"stale"`)




