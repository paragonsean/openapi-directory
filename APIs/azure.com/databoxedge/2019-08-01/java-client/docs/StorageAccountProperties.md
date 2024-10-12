

# StorageAccountProperties

The storage account properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blobEndpoint** | **String** | BlobEndpoint of Storage Account |  [optional] [readonly] |
|**containerCount** | **Integer** | The Container Count. Present only for Storage Accounts with DataPolicy set to Cloud. |  [optional] [readonly] |
|**dataPolicy** | [**DataPolicyEnum**](#DataPolicyEnum) | Data policy of the storage Account. |  [optional] |
|**description** | **String** | Description for the storage Account. |  [optional] |
|**storageAccountCredentialId** | **String** | Storage Account Credential Id |  [optional] |
|**storageAccountStatus** | [**StorageAccountStatusEnum**](#StorageAccountStatusEnum) | Current status of the storage account |  [optional] |



## Enum: DataPolicyEnum

| Name | Value |
|---- | -----|
| CLOUD | &quot;Cloud&quot; |
| LOCAL | &quot;Local&quot; |



## Enum: StorageAccountStatusEnum

| Name | Value |
|---- | -----|
| OK | &quot;OK&quot; |
| OFFLINE | &quot;Offline&quot; |
| UNKNOWN | &quot;Unknown&quot; |
| UPDATING | &quot;Updating&quot; |
| NEEDS_ATTENTION | &quot;NeedsAttention&quot; |



