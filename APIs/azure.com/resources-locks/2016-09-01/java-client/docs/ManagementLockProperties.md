

# ManagementLockProperties

The lock properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**level** | [**LevelEnum**](#LevelEnum) | The level of the lock. Possible values are: NotSpecified, CanNotDelete, ReadOnly. CanNotDelete means authorized users are able to read and modify the resources, but not delete. ReadOnly means authorized users can only read from a resource, but they can&#39;t modify or delete it. |  |
|**notes** | **String** | Notes about the lock. Maximum of 512 characters. |  [optional] |
|**owners** | [**List&lt;ManagementLockOwner&gt;**](ManagementLockOwner.md) | The owners of the lock. |  [optional] |



## Enum: LevelEnum

| Name | Value |
|---- | -----|
| NOT_SPECIFIED | &quot;NotSpecified&quot; |
| CAN_NOT_DELETE | &quot;CanNotDelete&quot; |
| READ_ONLY | &quot;ReadOnly&quot; |



