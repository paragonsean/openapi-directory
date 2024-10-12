# GkeHubApi.ConfigManagementOperatorState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploymentState** | **String** | The state of the Operator&#39;s deployment | [optional] 
**errors** | [**[ConfigManagementInstallError]**](ConfigManagementInstallError.md) | Install errors. | [optional] 
**version** | **String** | The semenatic version number of the operator | [optional] 



## Enum: DeploymentStateEnum


* `DEPLOYMENT_STATE_UNSPECIFIED` (value: `"DEPLOYMENT_STATE_UNSPECIFIED"`)

* `NOT_INSTALLED` (value: `"NOT_INSTALLED"`)

* `INSTALLED` (value: `"INSTALLED"`)

* `ERROR` (value: `"ERROR"`)

* `PENDING` (value: `"PENDING"`)




