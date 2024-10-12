

# PrivateEndpointConnectionProperties

Properties of a private endpoint connection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**privateEndpoint** | [**PrivateEndpoint**](PrivateEndpoint.md) |  |  [optional] |
|**privateLinkServiceConnectionState** | [**PrivateLinkServiceConnectionState**](PrivateLinkServiceConnectionState.md) |  |  |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning status of the private endpoint connection. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



