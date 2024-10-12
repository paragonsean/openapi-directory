

# AuthorizationPropertiesFormat

Properties of ExpressRouteCircuitAuthorization.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationKey** | **String** | The authorization key. |  [optional] |
|**authorizationUseStatus** | [**AuthorizationUseStatusEnum**](#AuthorizationUseStatusEnum) | The authorization use status. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |



## Enum: AuthorizationUseStatusEnum

| Name | Value |
|---- | -----|
| AVAILABLE | &quot;Available&quot; |
| IN_USE | &quot;InUse&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



