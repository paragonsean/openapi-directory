

# RestartDeployedCodePackageDescription

Defines description for restarting a deloyed code package on Service Fabric node. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**codePackageInstanceId** | **String** | The instance id for current running entry point. For a code package setup entry point (if specified) runs first and after it finishes main entry point is started. Each time entry point executable is run, its instance id will change. |  |
|**codePackageName** | **String** | The name of the code package defined in the service manifest. |  |
|**serviceManifestName** | **String** | The name of the service manifest. |  |
|**servicePackageActivationId** | **String** | The ActivationId of a deployed service package. If ServicePackageActivationMode specified at the time of creating the service is &#39;SharedProcess&#39; (or if it is not specified, in which case it defaults to &#39;SharedProcess&#39;), then value of ServicePackageActivationId is always an empty string.  |  [optional] |



