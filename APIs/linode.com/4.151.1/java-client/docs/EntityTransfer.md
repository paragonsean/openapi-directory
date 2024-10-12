

# EntityTransfer

An object representing an Entity Transfer. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **OffsetDateTime** | When this transfer was created.  |  [optional] |
|**entities** | [**EntityTransferEntities**](EntityTransferEntities.md) |  |  [optional] |
|**expiry** | **OffsetDateTime** | When this transfer expires. Transfers will automatically expire 24 hours after creation.  |  [optional] |
|**isSender** | **Boolean** | If the requesting account created this transfer.  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the transfer request.  &#x60;accepted&#x60;: The transfer has been accepted by another user and is currently in progress. Transfers can take up to 3 hours to complete.  &#x60;cancelled&#x60;: The transfer has been cancelled by the sender.  &#x60;completed&#x60;: The transfer has completed successfully.  &#x60;failed&#x60;: The transfer has failed after initiation.  &#x60;pending&#x60;: The transfer is ready to be accepted.  &#x60;stale&#x60;: The transfer has exceeded its expiration date. It can no longer be accepted or cancelled.  |  [optional] |
|**token** | **UUID** | The token used to identify and accept or cancel this transfer.  |  [optional] |
|**updated** | **OffsetDateTime** | When this transfer was last updated.  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACCEPTED | &quot;accepted&quot; |
| CANCELLED | &quot;cancelled&quot; |
| COMPLETED | &quot;completed&quot; |
| FAILED | &quot;failed&quot; |
| PENDING | &quot;pending&quot; |
| STALE | &quot;stale&quot; |



