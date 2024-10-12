

# Vault


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributeVersion** | **Integer** | The vault version |  [optional] |
|**contentVersion** | **Integer** | The version of the vault contents |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**description** | **String** |  |  [optional] |
|**id** | **String** |  |  [optional] |
|**items** | **Integer** | Number of active items in the vault |  [optional] |
|**name** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| USER_CREATED | &quot;USER_CREATED&quot; |
| PERSONAL | &quot;PERSONAL&quot; |
| EVERYONE | &quot;EVERYONE&quot; |
| TRANSFER | &quot;TRANSFER&quot; |



