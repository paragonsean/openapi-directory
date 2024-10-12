

# AzureFileShareProtectableItem

Protectable item for Azure Fileshare workloads.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**azureFileShareType** | [**AzureFileShareTypeEnum**](#AzureFileShareTypeEnum) | File Share type XSync or XSMB. |  [optional] |
|**parentContainerFabricId** | **String** | Full Fabric ID of container to which this protectable item belongs. For example, ARM ID. |  [optional] |
|**parentContainerFriendlyName** | **String** | Friendly name of container to which this protectable item belongs. |  [optional] |



## Enum: AzureFileShareTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| XSMB | &quot;XSMB&quot; |
| X_SYNC | &quot;XSync&quot; |



