# AmazonSimpleSystemsManagerSsm.UpdateMaintenanceWindowTaskRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**windowId** | **String** |  | 
**windowTaskId** | **String** |  | 
**targets** | **Array** |  | [optional] 
**taskArn** | **String** |  | [optional] 
**serviceRoleArn** | **String** |  | [optional] 
**taskParameters** | **Object** |  | [optional] 
**taskInvocationParameters** | [**UpdateMaintenanceWindowTaskRequestTaskInvocationParameters**](UpdateMaintenanceWindowTaskRequestTaskInvocationParameters.md) |  | [optional] 
**priority** | **Number** |  | [optional] 
**maxConcurrency** | **String** |  | [optional] 
**maxErrors** | **String** |  | [optional] 
**loggingInfo** | [**UpdateMaintenanceWindowTaskRequestLoggingInfo**](UpdateMaintenanceWindowTaskRequestLoggingInfo.md) |  | [optional] 
**name** | **String** |  | [optional] 
**description** | **String** |  | [optional] 
**replace** | **Boolean** |  | [optional] 
**cutoffBehavior** | [**MaintenanceWindowTaskCutoffBehavior**](MaintenanceWindowTaskCutoffBehavior.md) |  | [optional] 
**alarmConfiguration** | [**RegisterTaskWithMaintenanceWindowRequestAlarmConfiguration**](RegisterTaskWithMaintenanceWindowRequestAlarmConfiguration.md) |  | [optional] 


