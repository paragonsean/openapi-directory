

# DestinationAccountDetails

Details of the destination storage accounts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Arm Id of the destination where the data has to be moved. |  [optional] |
|**dataDestinationType** | [**DataDestinationTypeEnum**](#DataDestinationTypeEnum) | Data Destination Type. |  |
|**sharePassword** | **String** | Share password to be shared by all shares in SA. |  [optional] |



## Enum: DataDestinationTypeEnum

| Name | Value |
|---- | -----|
| STORAGE_ACCOUNT | &quot;StorageAccount&quot; |
| MANAGED_DISK | &quot;ManagedDisk&quot; |



