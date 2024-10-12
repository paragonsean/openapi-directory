# ResourceManagementClient.OnErrorDeploymentExtended

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploymentName** | **String** | The deployment to be used on error case. | [optional] 
**provisioningState** | **String** | The state of the provisioning for the on error deployment. | [optional] [readonly] 
**type** | **String** | The deployment on error behavior type. Possible values are LastSuccessful and SpecificDeployment. | [optional] 



## Enum: TypeEnum


* `LastSuccessful` (value: `"LastSuccessful"`)

* `SpecificDeployment` (value: `"SpecificDeployment"`)




