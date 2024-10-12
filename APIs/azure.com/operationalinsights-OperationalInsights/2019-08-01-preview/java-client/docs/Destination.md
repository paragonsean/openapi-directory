

# Destination

Destination properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metaData** | [**DestinationMetaData**](DestinationMetaData.md) |  |  [optional] |
|**resourceId** | **String** | The destination resource ID. This can be copied from the Properties entry of the destination resource in Azure. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the destination resource |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| STORAGE_ACCOUNT | &quot;StorageAccount&quot; |
| EVENT_HUB | &quot;EventHub&quot; |



