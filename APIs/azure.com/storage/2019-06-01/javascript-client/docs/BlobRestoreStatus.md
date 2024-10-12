# StorageManagementClient.BlobRestoreStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failureReason** | **String** | Failure reason when blob restore is failed. | [optional] [readonly] 
**parameters** | [**BlobRestoreParameters**](BlobRestoreParameters.md) |  | [optional] 
**restoreId** | **String** | Id for tracking blob restore request. | [optional] [readonly] 
**status** | **String** | The status of blob restore progress. Possible values are: - InProgress: Indicates that blob restore is ongoing. - Complete: Indicates that blob restore has been completed successfully. - Failed: Indicates that blob restore is failed. | [optional] [readonly] 



## Enum: StatusEnum


* `InProgress` (value: `"InProgress"`)

* `Complete` (value: `"Complete"`)

* `Failed` (value: `"Failed"`)




