

# DestinationAccountDetails

Details of the destination of the data

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Arm Id of the destination where the data has to be moved. |  [optional] |
|**dataDestinationType** | [**DataDestinationTypeEnum**](#DataDestinationTypeEnum) | Data Destination Type. |  |



## Enum: DataDestinationTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN_TYPE | &quot;UnknownType&quot; |
| STORAGE_ACCOUNT | &quot;StorageAccount&quot; |
| MANAGED_DISK | &quot;ManagedDisk&quot; |



