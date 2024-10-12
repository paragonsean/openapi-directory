

# MaintenanceWindow

MaintenanceWindow defines the maintenance window to be used for the cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dailyMaintenanceWindow** | [**DailyMaintenanceWindow**](DailyMaintenanceWindow.md) |  |  [optional] |
|**maintenanceExclusions** | [**Map&lt;String, TimeWindow&gt;**](TimeWindow.md) | Exceptions to maintenance window. Non-emergency maintenance should not occur in these windows. |  [optional] |
|**recurringWindow** | [**RecurringTimeWindow**](RecurringTimeWindow.md) |  |  [optional] |



