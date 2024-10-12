

# NetworkConfigurationDiagnosticParameters

Parameters to get network configuration diagnostic.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profiles** | [**List&lt;NetworkConfigurationDiagnosticProfile&gt;**](NetworkConfigurationDiagnosticProfile.md) | List of network configuration diagnostic profiles. |  |
|**targetResourceId** | **String** | The ID of the target resource to perform network configuration diagnostic. Valid options are VM, NetworkInterface, VMSS/NetworkInterface and Application Gateway. |  |
|**verbosityLevel** | [**VerbosityLevelEnum**](#VerbosityLevelEnum) | Verbosity level. |  [optional] |



## Enum: VerbosityLevelEnum

| Name | Value |
|---- | -----|
| NORMAL | &quot;Normal&quot; |
| MINIMUM | &quot;Minimum&quot; |
| FULL | &quot;Full&quot; |



