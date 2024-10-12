

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
| BAD_MANAGED_IMAGE_SOURCE | &quot;BadManagedImageSource&quot; |
| BAD_CUSTOMIZER_TYPE | &quot;BadCustomizerType&quot; |
| UNSUPPORTED_CUSTOMIZER_TYPE | &quot;UnsupportedCustomizerType&quot; |
| NO_CUSTOMIZER_SCRIPT | &quot;NoCustomizerScript&quot; |
| BAD_DISTRIBUTE_TYPE | &quot;BadDistributeType&quot; |
| BAD_SHARED_IMAGE_DISTRIBUTE | &quot;BadSharedImageDistribute&quot; |
| SERVER_ERROR | &quot;ServerError&quot; |
| OTHER | &quot;Other&quot; |



