

# DeployedServicePackageHealthState

Represents the health state of a deployed service package, containing the entity identifier and the aggregated health state.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationName** | **String** | The name of the application, including the &#39;fabric:&#39; URI scheme. |  [optional] |
|**nodeName** | **String** | The name of a Service Fabric node. |  [optional] |
|**serviceManifestName** | **String** | The name of the service manifest. |  [optional] |
|**servicePackageActivationId** | **String** | The ActivationId of a deployed service package. If ServicePackageActivationMode specified at the time of creating the service is &#39;SharedProcess&#39; (or if it is not specified, in which case it defaults to &#39;SharedProcess&#39;), then value of ServicePackageActivationId is always an empty string. |  [optional] |
|**aggregatedHealthState** | **HealthState** |  |  [optional] |



