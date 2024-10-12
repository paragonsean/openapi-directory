# CloudSpannerApi.CopyBackupMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelTime** | **String** | The time at which cancellation of CopyBackup operation was received. Operations.CancelOperation starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to &#x60;Code.CANCELLED&#x60;. | [optional] 
**name** | **String** | The name of the backup being created through the copy operation. Values are of the form &#x60;projects//instances//backups/&#x60;. | [optional] 
**progress** | [**OperationProgress**](OperationProgress.md) |  | [optional] 
**sourceBackup** | **String** | The name of the source backup that is being copied. Values are of the form &#x60;projects//instances//backups/&#x60;. | [optional] 


