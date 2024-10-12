

# RepairTaskApproveDescription

Describes a request for forced approval of a repair task.  This type supports the Service Fabric platform; it is not meant to be used directly from your code. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**taskId** | **String** | The ID of the repair task. |  |
|**version** | **String** | The current version number of the repair task. If non-zero, then the request will only succeed if this value matches the actual current version of the repair task. If zero, then no version check is performed. |  [optional] |



