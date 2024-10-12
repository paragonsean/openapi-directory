

# ItemUsage

A single item usage object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) |  |  [optional] |
|**client** | [**Client**](Client.md) |  |  [optional] |
|**itemUuid** | **String** |  |  [optional] |
|**location** | [**Location**](Location.md) |  |  [optional] |
|**timestamp** | **OffsetDateTime** |  |  [optional] |
|**usedVersion** | **Integer** |  |  [optional] |
|**user** | [**User**](User.md) |  |  [optional] |
|**uuid** | **String** |  |  [optional] |
|**vaultUuid** | **String** |  |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| FILL | &quot;fill&quot; |
| SELECT_SSO_PROVIDER | &quot;select-sso-provider&quot; |
| ENTER_ITEM_EDIT_MODE | &quot;enter-item-edit-mode&quot; |
| EXPORT | &quot;export&quot; |
| SHARE | &quot;share&quot; |
| SECURE_COPY | &quot;secure-copy&quot; |
| REVEAL | &quot;reveal&quot; |
| SERVER_CREATE | &quot;server-create&quot; |
| SERVER_UPDATE | &quot;server-update&quot; |
| SERVER_FETCH | &quot;server-fetch&quot; |



