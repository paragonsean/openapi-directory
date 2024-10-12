

# OptimizeRestoredDatabaseMetadata

Metadata type for the long-running operation used to track the progress of optimizations performed on a newly restored database. This long-running operation is automatically created by the system after the successful completion of a database restore, and cannot be cancelled.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Name of the restored database being optimized. |  [optional] |
|**progress** | [**OperationProgress**](OperationProgress.md) |  |  [optional] |



