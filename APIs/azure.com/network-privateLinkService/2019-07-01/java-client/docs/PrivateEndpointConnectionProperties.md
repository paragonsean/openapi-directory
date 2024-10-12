

# PrivateEndpointConnectionProperties

Properties of the PrivateEndpointConnectProperties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**privateEndpoint** | [**PrivateEndpointConnectionPropertiesPrivateEndpoint**](PrivateEndpointConnectionPropertiesPrivateEndpoint.md) |  |  [optional] |
|**privateLinkServiceConnectionState** | [**PrivateLinkServiceConnectionState**](PrivateLinkServiceConnectionState.md) |  |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



