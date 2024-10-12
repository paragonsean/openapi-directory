

# AccountCredentialDetails

Credential details of the account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountConnectionString** | **String** | Connection string of the account endpoint to use the account as a storage endpoint on the device. |  [optional] [readonly] |
|**accountName** | **String** | Name of the account. |  [optional] [readonly] |
|**dataDestinationType** | [**DataDestinationTypeEnum**](#DataDestinationTypeEnum) | Data Destination Type. |  [optional] [readonly] |
|**shareCredentialDetails** | [**List&lt;ShareCredentialDetails&gt;**](ShareCredentialDetails.md) | Per share level unencrypted access credentials. |  [optional] [readonly] |



## Enum: DataDestinationTypeEnum

| Name | Value |
|---- | -----|
| STORAGE_ACCOUNT | &quot;StorageAccount&quot; |
| MANAGED_DISK | &quot;ManagedDisk&quot; |



