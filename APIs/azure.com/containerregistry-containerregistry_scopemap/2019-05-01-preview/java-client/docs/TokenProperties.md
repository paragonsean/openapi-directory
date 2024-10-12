

# TokenProperties

The properties of a token.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationDate** | **OffsetDateTime** | The creation date of scope map. |  [optional] [readonly] |
|**credentials** | [**TokenCredentialsProperties**](TokenCredentialsProperties.md) |  |  [optional] |
|**objectId** | **String** | The user/group/application object ID for which the token has to be created. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the resource. |  [optional] [readonly] |
|**scopeMapId** | **String** | The resource ID of the scope map to which the token will be associated with. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the token example enabled or disabled. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;enabled&quot; |
| DISABLED | &quot;disabled&quot; |



