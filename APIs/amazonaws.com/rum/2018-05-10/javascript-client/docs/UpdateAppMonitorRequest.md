# CloudWatchRum.UpdateAppMonitorRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appMonitorConfiguration** | [**CreateAppMonitorRequestAppMonitorConfiguration**](CreateAppMonitorRequestAppMonitorConfiguration.md) |  | [optional] 
**customEvents** | [**CreateAppMonitorRequestCustomEvents**](CreateAppMonitorRequestCustomEvents.md) |  | [optional] 
**cwLogEnabled** | **Boolean** | Data collected by RUM is kept by RUM for 30 days and then deleted. This parameter specifies whether RUM sends a copy of this telemetry data to Amazon CloudWatch Logs in your account. This enables you to keep the telemetry data for more than 30 days, but it does incur Amazon CloudWatch Logs charges. | [optional] 
**domain** | **String** | The top-level internet domain name for which your application has administrative authority. | [optional] 


