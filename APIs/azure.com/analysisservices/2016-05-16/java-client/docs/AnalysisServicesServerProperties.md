

# AnalysisServicesServerProperties

Properties of Analysis Services resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current deployment state of Analysis Services resource. The provisioningState is to indicate states for resource provisioning. |  [optional] [readonly] |
|**serverFullName** | **String** | The full name of the Analysis Services resource. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | The current state of Analysis Services resource. The state is to indicate more states outside of resource provisioning. |  [optional] [readonly] |
|**asAdministrators** | [**ServerAdministrators**](ServerAdministrators.md) |  |  [optional] |
|**backupBlobContainerUri** | **String** | The container URI of backup blob. |  [optional] |



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



