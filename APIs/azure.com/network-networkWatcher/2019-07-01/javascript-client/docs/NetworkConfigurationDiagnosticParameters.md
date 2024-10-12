# NetworkManagementClient.NetworkConfigurationDiagnosticParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profiles** | [**[NetworkConfigurationDiagnosticProfile]**](NetworkConfigurationDiagnosticProfile.md) | List of network configuration diagnostic profiles. | 
**targetResourceId** | **String** | The ID of the target resource to perform network configuration diagnostic. Valid options are VM, NetworkInterface, VMSS/NetworkInterface and Application Gateway. | 
**verbosityLevel** | **String** | Verbosity level. | [optional] 



## Enum: VerbosityLevelEnum


* `Normal` (value: `"Normal"`)

* `Minimum` (value: `"Minimum"`)

* `Full` (value: `"Full"`)




