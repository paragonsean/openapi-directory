# AmazonSimpleSystemsManagerSsm.RegisterTaskWithMaintenanceWindowRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**windowId** | **String** |  | 
**targets** | **Array** |  | [optional] 
**taskArn** | **String** |  | 
**serviceRoleArn** | **String** |  | [optional] 
**taskType** | [**MaintenanceWindowTaskType**](MaintenanceWindowTaskType.md) |  | 
**taskParameters** | **Object** |  | [optional] 
**taskInvocationParameters** | [**RegisterTaskWithMaintenanceWindowRequestTaskInvocationParameters**](RegisterTaskWithMaintenanceWindowRequestTaskInvocationParameters.md) |  | [optional] 
**priority** | **Number** |  | [optional] 
**maxConcurrency** | **String** |  | [optional] 
**maxErrors** | **String** |  | [optional] 
**loggingInfo** | [**RegisterTaskWithMaintenanceWindowRequestLoggingInfo**](RegisterTaskWithMaintenanceWindowRequestLoggingInfo.md) |  | [optional] 
**name** | **String** |  | [optional] 
**description** | **String** |  | [optional] 
**clientToken** | **String** |  | [optional] 
**cutoffBehavior** | [**MaintenanceWindowTaskCutoffBehavior**](MaintenanceWindowTaskCutoffBehavior.md) |  | [optional] 
**alarmConfiguration** | [**RegisterTaskWithMaintenanceWindowRequestAlarmConfiguration**](RegisterTaskWithMaintenanceWindowRequestAlarmConfiguration.md) |  | [optional] 


