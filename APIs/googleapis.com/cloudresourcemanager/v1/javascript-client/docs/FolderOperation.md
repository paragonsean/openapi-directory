# CloudResourceManagerApi.FolderOperation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinationParent** | **String** | The resource name of the folder or organization we are either creating the folder under or moving the folder to. | [optional] 
**displayName** | **String** | The display name of the folder. | [optional] 
**operationType** | **String** | The type of this operation. | [optional] 
**sourceParent** | **String** | The resource name of the folder&#39;s parent. Only applicable when the operation_type is MOVE. | [optional] 



## Enum: OperationTypeEnum


* `OPERATION_TYPE_UNSPECIFIED` (value: `"OPERATION_TYPE_UNSPECIFIED"`)

* `CREATE` (value: `"CREATE"`)

* `MOVE` (value: `"MOVE"`)




