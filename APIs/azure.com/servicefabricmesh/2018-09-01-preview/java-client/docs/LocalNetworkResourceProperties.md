

# LocalNetworkResourceProperties

Information about a Service Fabric container network local to a single Service Fabric cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**networkAddressPrefix** | **String** | Address space for a container network. This is expressed in CIDR notation. |  [optional] |
|**description** | **String** | User readable description of the network. |  [optional] |
|**status** | **ResourceStatus** |  |  [optional] |
|**statusDetails** | **String** | Gives additional information about the current status of the network. |  [optional] [readonly] |
|**kind** | **NetworkKind** |  |  |
|**provisioningState** | **String** | State of the resource. |  [optional] [readonly] |



