

# ControllerProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataPlaneFqdn** | **String** | DNS name for accessing DataPlane services |  [optional] [readonly] |
|**hostSuffix** | **String** | DNS suffix for public endpoints running in the Azure Dev Spaces Controller. |  |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the Azure Dev Spaces Controller. |  [optional] [readonly] |
|**targetContainerHostCredentialsBase64** | **String** | Credentials of the target container host (base64). |  |
|**targetContainerHostResourceId** | **String** | Resource ID of the target container host |  |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |
| UPDATING | &quot;Updating&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| DELETED | &quot;Deleted&quot; |



