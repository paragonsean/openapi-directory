# KubernetesEngineApi.MaintenanceWindow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dailyMaintenanceWindow** | [**DailyMaintenanceWindow**](DailyMaintenanceWindow.md) |  | [optional] 
**maintenanceExclusions** | [**{String: TimeWindow}**](TimeWindow.md) | Exceptions to maintenance window. Non-emergency maintenance should not occur in these windows. | [optional] 
**recurringWindow** | [**RecurringTimeWindow**](RecurringTimeWindow.md) |  | [optional] 


