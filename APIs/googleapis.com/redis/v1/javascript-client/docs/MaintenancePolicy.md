# GoogleCloudMemorystoreForRedisApi.MaintenancePolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time when the policy was created. | [optional] [readonly] 
**description** | **String** | Optional. Description of what this policy is for. Create/Update methods return INVALID_ARGUMENT if the length is greater than 512. | [optional] 
**updateTime** | **String** | Output only. The time when the policy was last updated. | [optional] [readonly] 
**weeklyMaintenanceWindow** | [**[WeeklyMaintenanceWindow]**](WeeklyMaintenanceWindow.md) | Optional. Maintenance window that is applied to resources covered by this policy. Minimum 1. For the current version, the maximum number of weekly_window is expected to be one. | [optional] 


