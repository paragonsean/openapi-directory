

# IoTSpacesProperties

The properties of an IoTSpaces instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**managementApiUrl** | **String** | The management Api endpoint. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state. |  [optional] [readonly] |
|**storageContainer** | [**StorageContainerProperties**](StorageContainerProperties.md) |  |  [optional] |
|**webPortalUrl** | **String** | The management UI endpoint. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| PROVISIONING | &quot;Provisioning&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



