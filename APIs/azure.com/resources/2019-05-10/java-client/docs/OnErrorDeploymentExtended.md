

# OnErrorDeploymentExtended

Deployment on error behavior with additional details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deploymentName** | **String** | The deployment to be used on error case. |  [optional] |
|**provisioningState** | **String** | The state of the provisioning for the on error deployment. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The deployment on error behavior type. Possible values are LastSuccessful and SpecificDeployment. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| LAST_SUCCESSFUL | &quot;LastSuccessful&quot; |
| SPECIFIC_DEPLOYMENT | &quot;SpecificDeployment&quot; |



