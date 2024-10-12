# SignalRManagementClient.SignalRFeature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flag** | **String** | FeatureFlags is the supported features of Azure SignalR service.  - ServiceMode: Flag for backend server for SignalR service. Values allowed: \&quot;Default\&quot;: have your own backend server; \&quot;Serverless\&quot;: your application doesn&#39;t have a backend server; \&quot;Classic\&quot;: for backward compatibility. Support both Default and Serverless mode but not recommended; \&quot;PredefinedOnly\&quot;: for future use.  - EnableConnectivityLogs: \&quot;true\&quot;/\&quot;false\&quot;, to enable/disable the connectivity log category respectively. | 
**properties** | **{String: String}** | Optional properties related to this feature. | [optional] 
**value** | **String** | Value of the feature flag. See Azure SignalR service document https://docs.microsoft.com/azure/azure-signalr/ for allowed values. | 



## Enum: FlagEnum


* `ServiceMode` (value: `"ServiceMode"`)

* `EnableConnectivityLogs` (value: `"EnableConnectivityLogs"`)




