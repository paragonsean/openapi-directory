

# DiscoveredService

DiscoveredService is a network/api interface that exposes some functionality to clients for consumption over the network. A discovered service can be registered to a App Hub service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Identifier. The resource name of the discovered service. Format: \&quot;projects/{host-project-id}/locations/{location}/discoveredServices/{uuid}\&quot;\&quot; |  [optional] |
|**serviceProperties** | [**ServiceProperties**](ServiceProperties.md) |  |  [optional] |
|**serviceReference** | [**ServiceReference**](ServiceReference.md) |  |  [optional] |



