# AzureAnalysisServices.AnalysisServicesServerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provisioningState** | **String** | The current deployment state of Analysis Services resource. The provisioningState is to indicate states for resource provisioning. | [optional] [readonly] 
**serverFullName** | **String** | The full name of the Analysis Services resource. | [optional] [readonly] 
**state** | **String** | The current state of Analysis Services resource. The state is to indicate more states outside of resource provisioning. | [optional] [readonly] 
**asAdministrators** | [**ServerAdministrators**](ServerAdministrators.md) |  | [optional] 
**backupBlobContainerUri** | **String** | The SAS container URI to the backup container. | [optional] 
**gatewayDetails** | [**GatewayDetails**](GatewayDetails.md) |  | [optional] 
**ipV4FirewallSettings** | [**IPv4FirewallSettings**](IPv4FirewallSettings.md) |  | [optional] 
**querypoolConnectionMode** | **String** | How the read-write server&#39;s participation in the query pool is controlled.&lt;br/&gt;It can have the following values: &lt;ul&gt;&lt;li&gt;readOnly - indicates that the read-write server is intended not to participate in query operations&lt;/li&gt;&lt;li&gt;all - indicates that the read-write server can participate in query operations&lt;/li&gt;&lt;/ul&gt;Specifying readOnly when capacity is 1 results in error. | [optional] [default to &#39;All&#39;]



## Enum: ProvisioningStateEnum


* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Paused` (value: `"Paused"`)

* `Suspended` (value: `"Suspended"`)

* `Provisioning` (value: `"Provisioning"`)

* `Updating` (value: `"Updating"`)

* `Suspending` (value: `"Suspending"`)

* `Pausing` (value: `"Pausing"`)

* `Resuming` (value: `"Resuming"`)

* `Preparing` (value: `"Preparing"`)

* `Scaling` (value: `"Scaling"`)





## Enum: StateEnum


* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Paused` (value: `"Paused"`)

* `Suspended` (value: `"Suspended"`)

* `Provisioning` (value: `"Provisioning"`)

* `Updating` (value: `"Updating"`)

* `Suspending` (value: `"Suspending"`)

* `Pausing` (value: `"Pausing"`)

* `Resuming` (value: `"Resuming"`)

* `Preparing` (value: `"Preparing"`)

* `Scaling` (value: `"Scaling"`)





## Enum: QuerypoolConnectionModeEnum


* `All` (value: `"All"`)

* `ReadOnly` (value: `"ReadOnly"`)




