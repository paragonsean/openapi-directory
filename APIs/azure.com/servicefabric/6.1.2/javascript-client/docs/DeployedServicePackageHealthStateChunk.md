# ServiceFabricClientApis.DeployedServicePackageHealthStateChunk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**healthState** | [**HealthState**](HealthState.md) |  | [optional] 
**serviceManifestName** | **String** | The name of the service manifest. | [optional] 
**servicePackageActivationId** | **String** | The ActivationId of a deployed service package. If ServicePackageActivationMode specified at the time of creating the service is &#39;SharedProcess&#39; (or if it is not specified, in which case it defaults to &#39;SharedProcess&#39;), then value of ServicePackageActivationId is always an empty string.  | [optional] 


