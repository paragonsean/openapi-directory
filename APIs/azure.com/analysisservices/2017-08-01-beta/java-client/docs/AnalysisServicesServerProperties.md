

# AnalysisServicesServerProperties

Properties of Analysis Services resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current deployment state of Analysis Services resource. The provisioningState is to indicate states for resource provisioning. |  [optional] [readonly] |
|**serverFullName** | **String** | The full name of the Analysis Services resource. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | The current state of Analysis Services resource. The state is to indicate more states outside of resource provisioning. |  [optional] [readonly] |
|**asAdministrators** | [**ServerAdministrators**](ServerAdministrators.md) |  |  [optional] |
|**backupBlobContainerUri** | **String** | The SAS container URI to the backup container. |  [optional] |
|**gatewayDetails** | [**GatewayDetails**](GatewayDetails.md) |  |  [optional] |
|**ipV4FirewallSettings** | [**IPv4FirewallSettings**](IPv4FirewallSettings.md) |  |  [optional] |
|**querypoolConnectionMode** | [**QuerypoolConnectionModeEnum**](#QuerypoolConnectionModeEnum) | How the read-write server&#39;s participation in the query pool is controlled.&lt;br/&gt;It can have the following values: &lt;ul&gt;&lt;li&gt;readOnly - indicates that the read-write server is intended not to participate in query operations&lt;/li&gt;&lt;li&gt;all - indicates that the read-write server can participate in query operations&lt;/li&gt;&lt;/ul&gt;Specifying readOnly when capacity is 1 results in error. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| PAUSED | &quot;Paused&quot; |
| SUSPENDED | &quot;Suspended&quot; |
| PROVISIONING | &quot;Provisioning&quot; |
| UPDATING | &quot;Updating&quot; |
| SUSPENDING | &quot;Suspending&quot; |
| PAUSING | &quot;Pausing&quot; |
| RESUMING | &quot;Resuming&quot; |
| PREPARING | &quot;Preparing&quot; |
| SCALING | &quot;Scaling&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| PAUSED | &quot;Paused&quot; |
| SUSPENDED | &quot;Suspended&quot; |
| PROVISIONING | &quot;Provisioning&quot; |
| UPDATING | &quot;Updating&quot; |
| SUSPENDING | &quot;Suspending&quot; |
| PAUSING | &quot;Pausing&quot; |
| RESUMING | &quot;Resuming&quot; |
| PREPARING | &quot;Preparing&quot; |
| SCALING | &quot;Scaling&quot; |



## Enum: QuerypoolConnectionModeEnum

| Name | Value |
|---- | -----|
| ALL | &quot;All&quot; |
| READ_ONLY | &quot;ReadOnly&quot; |



