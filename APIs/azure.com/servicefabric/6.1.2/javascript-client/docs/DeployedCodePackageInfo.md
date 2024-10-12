# ServiceFabricClientApis.DeployedCodePackageInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostIsolationMode** | [**HostIsolationMode**](HostIsolationMode.md) |  | [optional] 
**hostType** | [**HostType**](HostType.md) |  | [optional] 
**mainEntryPoint** | [**CodePackageEntryPoint**](CodePackageEntryPoint.md) |  | [optional] 
**name** | **String** | The name of the code package defined in the service manifest. | [optional] 
**runFrequencyInterval** | **String** | The interval at which code package is run. This is used for periodic code package. | [optional] 
**serviceManifestName** | **String** | The name of the service manifest. | [optional] 
**servicePackageActivationId** | **String** | The ActivationId of a deployed service package. If ServicePackageActivationMode specified at the time of creating the service is &#39;SharedProcess&#39; (or if it is not specified, in which case it defaults to &#39;SharedProcess&#39;), then value of ServicePackageActivationId is always an empty string.  | [optional] 
**setupEntryPoint** | [**CodePackageEntryPoint**](CodePackageEntryPoint.md) |  | [optional] 
**status** | [**DeploymentStatus**](DeploymentStatus.md) |  | [optional] 
**version** | **String** | The version of the code package specified in service manifest. | [optional] 


