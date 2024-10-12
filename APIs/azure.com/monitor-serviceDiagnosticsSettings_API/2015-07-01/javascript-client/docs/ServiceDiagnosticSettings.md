# MonitorManagementClient.ServiceDiagnosticSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**[LogSettings]**](LogSettings.md) | the list of logs settings. | [optional] 
**metrics** | [**[MetricSettings]**](MetricSettings.md) | the list of metric settings. | [optional] 
**serviceBusRuleId** | **String** | The service bus rule ID of the service bus namespace in which you would like to have Event Hubs created for streaming Diagnostic Logs. The rule ID is of the format: &#39;{service bus resource ID}/authorizationrules/{key name}&#39;. | [optional] 
**storageAccountId** | **String** | The resource ID of the storage account to which you would like to send Diagnostic Logs. | [optional] 
**workspaceId** | **String** | The workspace ID (resource ID of a Log Analytics workspace) for a Log Analytics workspace to which you would like to send Diagnostic Logs. Example: /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2 | [optional] 


