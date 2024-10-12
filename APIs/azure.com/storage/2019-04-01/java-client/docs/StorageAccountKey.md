

# StorageAccountKey

An access key for the storage account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keyName** | **String** | Name of the key. |  [optional] [readonly] |
|**permissions** | [**PermissionsEnum**](#PermissionsEnum) | Permissions for the key -- read-only or full permissions. |  [optional] [readonly] |
|**value** | **String** | Base 64-encoded value of the key. |  [optional] [readonly] |



## Enum: PermissionsEnum

| Name | Value |
|---- | -----|
| READ | &quot;Read&quot; |
| FULL | &quot;Full&quot; |



