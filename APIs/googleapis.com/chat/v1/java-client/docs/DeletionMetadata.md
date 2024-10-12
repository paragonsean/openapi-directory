

# DeletionMetadata

Information about a deleted message. A message is deleted when `delete_time` is set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deletionType** | [**DeletionTypeEnum**](#DeletionTypeEnum) | Indicates who deleted the message. |  [optional] |



## Enum: DeletionTypeEnum

| Name | Value |
|---- | -----|
| DELETION_TYPE_UNSPECIFIED | &quot;DELETION_TYPE_UNSPECIFIED&quot; |
| CREATOR | &quot;CREATOR&quot; |
| SPACE_OWNER | &quot;SPACE_OWNER&quot; |
| ADMIN | &quot;ADMIN&quot; |
| APP_MESSAGE_EXPIRY | &quot;APP_MESSAGE_EXPIRY&quot; |
| CREATOR_VIA_APP | &quot;CREATOR_VIA_APP&quot; |
| SPACE_OWNER_VIA_APP | &quot;SPACE_OWNER_VIA_APP&quot; |



