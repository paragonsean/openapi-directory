

# RepairTaskUpdateHealthPolicyDescription

Describes a request to update the health policy of a repair task.  This type supports the Service Fabric platform; it is not meant to be used directly from your code.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**performPreparingHealthCheck** | **Boolean** | A boolean indicating if health check is to be performed in the Preparing stage of the repair task. If not specified the existing value should not be altered. Otherwise, specify the desired new value. |  [optional] |
|**performRestoringHealthCheck** | **Boolean** | A boolean indicating if health check is to be performed in the Restoring stage of the repair task. If not specified the existing value should not be altered. Otherwise, specify the desired new value. |  [optional] |
|**taskId** | **String** | The ID of the repair task to be updated. |  |
|**version** | **String** | The current version number of the repair task. If non-zero, then the request will only succeed if this value matches the actual current value of the repair task. If zero, then no version check is performed. |  [optional] |



