

# DiagnosticSettings

The diagnostic settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventHubAuthorizationRuleId** | **String** | The resource Id for the event hub authorization rule. |  [optional] |
|**eventHubName** | **String** | The name of the event hub. If none is specified, the default event hub will be selected. |  [optional] |
|**logAnalyticsDestinationType** | **String** | A string indicating whether the export to Log Analytics should use the default destination type, i.e. AzureDiagnostics, or use a destination type constructed as follows: &lt;normalized service identity&gt;_&lt;normalized category name&gt;. Possible values are: Dedicated and null (null is default.) |  [optional] |
|**logs** | [**List&lt;LogSettings&gt;**](LogSettings.md) | The list of logs settings. |  [optional] |
|**metrics** | [**List&lt;MetricSettings&gt;**](MetricSettings.md) | The list of metric settings. |  [optional] |
|**serviceBusRuleId** | **String** | The service bus rule Id of the diagnostic setting. This is here to maintain backwards compatibility. |  [optional] |
|**storageAccountId** | **String** | The resource ID of the storage account to which you would like to send Diagnostic Logs. |  [optional] |
|**workspaceId** | **String** | The full ARM resource ID of the Log Analytics workspace to which you would like to send Diagnostic Logs. Example: /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2 |  [optional] |



