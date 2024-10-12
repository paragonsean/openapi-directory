

# StorageCapability

The storage account type capability.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reason** | **String** | The reason for the capability not being available. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the capability. |  [optional] [readonly] |
|**storageAccountType** | [**StorageAccountTypeEnum**](#StorageAccountTypeEnum) | The storage account type for the database&#39;s backups. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| VISIBLE | &quot;Visible&quot; |
| AVAILABLE | &quot;Available&quot; |
| DEFAULT | &quot;Default&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: StorageAccountTypeEnum

| Name | Value |
|---- | -----|
| GRS | &quot;GRS&quot; |
| LRS | &quot;LRS&quot; |
| ZRS | &quot;ZRS&quot; |



