# GoogleWorkspaceAlertCenterApi.TransferError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **String** | User&#39;s email address. This may be unavailable if the entity was deleted. | [optional] 
**entityType** | **String** | Type of entity being transferred to. For ring group members, this should always be USER. | [optional] 
**id** | **String** | Ring group or auto attendant ID. Not set for users. | [optional] 
**invalidReason** | **String** | Reason for the error. | [optional] 
**name** | **String** | User&#39;s full name, or the ring group / auto attendant name. This may be unavailable if the entity was deleted. | [optional] 



## Enum: EntityTypeEnum


* `ENTITY_TYPE_UNSPECIFIED` (value: `"TRANSFER_ENTITY_TYPE_UNSPECIFIED"`)

* `AUTO_ATTENDANT` (value: `"TRANSFER_AUTO_ATTENDANT"`)

* `RING_GROUP` (value: `"TRANSFER_RING_GROUP"`)

* `USER` (value: `"TRANSFER_USER"`)





## Enum: InvalidReasonEnum


* `TRANSFER_INVALID_REASON_UNSPECIFIED` (value: `"TRANSFER_INVALID_REASON_UNSPECIFIED"`)

* `TRANSFER_TARGET_DELETED` (value: `"TRANSFER_TARGET_DELETED"`)

* `UNLICENSED` (value: `"UNLICENSED"`)

* `SUSPENDED` (value: `"SUSPENDED"`)

* `NO_PHONE_NUMBER` (value: `"NO_PHONE_NUMBER"`)




