

# DeploymentOccurrence

The period during which some deployable was active in a runtime.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | Address of the runtime element hosting this deployment. |  [optional] |
|**config** | **String** | Configuration used to create this deployment. |  [optional] |
|**deployTime** | **String** | Required. Beginning of the lifetime of this deployment. |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) | Platform hosting this deployment. |  [optional] |
|**resourceUri** | **List&lt;String&gt;** | Output only. Resource URI for the artifact being deployed taken from the deployable field with the same name. |  [optional] |
|**undeployTime** | **String** | End of the lifetime of this deployment. |  [optional] |
|**userEmail** | **String** | Identity of the user that triggered this deployment. |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| PLATFORM_UNSPECIFIED | &quot;PLATFORM_UNSPECIFIED&quot; |
| GKE | &quot;GKE&quot; |
| FLEX | &quot;FLEX&quot; |
| CUSTOM | &quot;CUSTOM&quot; |



