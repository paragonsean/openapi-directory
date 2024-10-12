

# TransferError

Details for an invalid transfer or forward.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** | User&#39;s email address. This may be unavailable if the entity was deleted. |  [optional] |
|**entityType** | [**EntityTypeEnum**](#EntityTypeEnum) | Type of entity being transferred to. For ring group members, this should always be USER. |  [optional] |
|**id** | **String** | Ring group or auto attendant ID. Not set for users. |  [optional] |
|**invalidReason** | [**InvalidReasonEnum**](#InvalidReasonEnum) | Reason for the error. |  [optional] |
|**name** | **String** | User&#39;s full name, or the ring group / auto attendant name. This may be unavailable if the entity was deleted. |  [optional] |



## Enum: EntityTypeEnum

| Name | Value |
|---- | -----|
| ENTITY_TYPE_UNSPECIFIED | &quot;TRANSFER_ENTITY_TYPE_UNSPECIFIED&quot; |
| AUTO_ATTENDANT | &quot;TRANSFER_AUTO_ATTENDANT&quot; |
| RING_GROUP | &quot;TRANSFER_RING_GROUP&quot; |
| USER | &quot;TRANSFER_USER&quot; |



## Enum: InvalidReasonEnum

| Name | Value |
|---- | -----|
| TRANSFER_INVALID_REASON_UNSPECIFIED | &quot;TRANSFER_INVALID_REASON_UNSPECIFIED&quot; |
| TRANSFER_TARGET_DELETED | &quot;TRANSFER_TARGET_DELETED&quot; |
| UNLICENSED | &quot;UNLICENSED&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |
| NO_PHONE_NUMBER | &quot;NO_PHONE_NUMBER&quot; |



