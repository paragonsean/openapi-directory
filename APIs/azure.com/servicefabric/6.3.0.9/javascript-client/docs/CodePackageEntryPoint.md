# ServiceFabricClientApis.CodePackageEntryPoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codePackageEntryPointStatistics** | [**CodePackageEntryPointStatistics**](CodePackageEntryPointStatistics.md) |  | [optional] 
**entryPointLocation** | **String** | The location of entry point executable on the node. | [optional] 
**instanceId** | **String** | The instance ID for current running entry point. For a code package setup entry point (if specified) runs first and after it finishes main entry point is started. Each time entry point executable is run, its instance id will change. | [optional] 
**nextActivationTime** | **Date** | The time (in UTC) when the entry point executable will be run next. | [optional] 
**processId** | **String** | The process ID of the entry point. | [optional] 
**runAsUserName** | **String** | The user name under which entry point executable is run on the node. | [optional] 
**status** | [**EntryPointStatus**](EntryPointStatus.md) |  | [optional] 


