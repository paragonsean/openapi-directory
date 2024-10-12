

# ProvisioningError


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | Verbose error message about the provisioning failure |  [optional] |
|**provisioningErrorCode** | [**ProvisioningErrorCodeEnum**](#ProvisioningErrorCodeEnum) | Error code of the provisioning failure |  [optional] |



## Enum: ProvisioningErrorCodeEnum

| Name | Value |
|---- | -----|
| BAD_SOURCE_TYPE | &quot;BadSourceType&quot; |
| BAD_PIR_SOURCE | &quot;BadPIRSource&quot; |
| BAD_ISO_SOURCE | &quot;BadISOSource&quot; |
| BAD_CUSTOMIZER_TYPE | &quot;BadCustomizerType&quot; |
| NO_CUSTOMIZER_SHELL_SCRIPT | &quot;NoCustomizerShellScript&quot; |
| SERVER_ERROR | &quot;ServerError&quot; |
| OTHER | &quot;Other&quot; |



