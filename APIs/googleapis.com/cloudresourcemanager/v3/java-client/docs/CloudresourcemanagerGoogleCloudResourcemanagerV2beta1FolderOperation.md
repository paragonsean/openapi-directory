

# CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperation

Metadata describing a long running folder operation

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destinationParent** | **String** | The resource name of the folder or organization we are either creating the folder under or moving the folder to. |  [optional] |
|**displayName** | **String** | The display name of the folder. |  [optional] |
|**operationType** | [**OperationTypeEnum**](#OperationTypeEnum) | The type of this operation. |  [optional] |
|**sourceParent** | **String** | The resource name of the folder&#39;s parent. Only applicable when the operation_type is MOVE. |  [optional] |



## Enum: OperationTypeEnum

| Name | Value |
|---- | -----|
| OPERATION_TYPE_UNSPECIFIED | &quot;OPERATION_TYPE_UNSPECIFIED&quot; |
| CREATE | &quot;CREATE&quot; |
| MOVE | &quot;MOVE&quot; |



