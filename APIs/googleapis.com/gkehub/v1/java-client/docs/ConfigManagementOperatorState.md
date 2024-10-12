

# ConfigManagementOperatorState

State information for an ACM's Operator

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deploymentState** | [**DeploymentStateEnum**](#DeploymentStateEnum) | The state of the Operator&#39;s deployment |  [optional] |
|**errors** | [**List&lt;ConfigManagementInstallError&gt;**](ConfigManagementInstallError.md) | Install errors. |  [optional] |
|**version** | **String** | The semenatic version number of the operator |  [optional] |



## Enum: DeploymentStateEnum

| Name | Value |
|---- | -----|
| DEPLOYMENT_STATE_UNSPECIFIED | &quot;DEPLOYMENT_STATE_UNSPECIFIED&quot; |
| NOT_INSTALLED | &quot;NOT_INSTALLED&quot; |
| INSTALLED | &quot;INSTALLED&quot; |
| ERROR | &quot;ERROR&quot; |
| PENDING | &quot;PENDING&quot; |



