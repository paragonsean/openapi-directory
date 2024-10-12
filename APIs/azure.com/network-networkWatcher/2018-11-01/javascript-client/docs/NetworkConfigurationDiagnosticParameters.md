# NetworkManagementClient.NetworkConfigurationDiagnosticParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profiles** | [**[NetworkConfigurationDiagnosticProfile]**](NetworkConfigurationDiagnosticProfile.md) | List of network configuration diagnostic profiles. | 
**targetResourceId** | **String** | The ID of the target resource to perform network configuration diagnostic. Valid options are VM, NetworkInterface, VMSS/NetworkInterface and Application Gateway. | 
**verbosityLevel** | **String** | Verbosity level. Accepted values are &#39;Normal&#39;, &#39;Minimum&#39;, &#39;Full&#39;. | [optional] 



## Enum: VerbosityLevelEnum


* `Normal` (value: `"Normal"`)

* `Minimum` (value: `"Minimum"`)

* `Full` (value: `"Full"`)




