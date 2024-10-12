

# RollbackStatusInfo

Information about rollback on failed VM instances after a OS Upgrade operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**failedRolledbackInstanceCount** | **Integer** | The number of instances which failed to rollback. |  [optional] [readonly] |
|**rollbackError** | [**ApiError**](ApiError.md) |  |  [optional] |
|**successfullyRolledbackInstanceCount** | **Integer** | The number of instances which have been successfully rolled back. |  [optional] [readonly] |



