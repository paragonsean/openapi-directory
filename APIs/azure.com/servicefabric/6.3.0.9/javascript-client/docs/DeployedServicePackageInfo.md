# ServiceFabricClientApis.DeployedServicePackageInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the service manifest. | [optional] 
**servicePackageActivationId** | **String** | The ActivationId of a deployed service package. If ServicePackageActivationMode specified at the time of creating the service is &#39;SharedProcess&#39; (or if it is not specified, in which case it defaults to &#39;SharedProcess&#39;), then value of ServicePackageActivationId is always an empty string. | [optional] 
**status** | [**DeploymentStatus**](DeploymentStatus.md) |  | [optional] 
**version** | **String** | The version of the service package specified in service manifest. | [optional] 


