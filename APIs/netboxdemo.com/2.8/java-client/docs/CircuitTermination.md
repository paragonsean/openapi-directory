

# CircuitTermination


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cable** | [**NestedCable**](NestedCable.md) |  |  [optional] |
|**circuit** | [**NestedCircuit**](NestedCircuit.md) |  |  |
|**connectedEndpoint** | **Map&lt;String, String&gt;** |  Return the appropriate serializer for the type of connected object.  |  [optional] [readonly] |
|**connectedEndpointType** | **String** |  |  [optional] [readonly] |
|**connectionStatus** | [**ConnectionStatus**](ConnectionStatus.md) |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**portSpeed** | **Integer** |  |  |
|**ppInfo** | **String** |  |  [optional] |
|**site** | [**NestedSite**](NestedSite.md) |  |  |
|**termSide** | [**TermSideEnum**](#TermSideEnum) |  |  |
|**upstreamSpeed** | **Integer** | Upstream speed, if different from port speed |  [optional] |
|**xconnectId** | **String** |  |  [optional] |



## Enum: TermSideEnum

| Name | Value |
|---- | -----|
| A | &quot;A&quot; |
| Z | &quot;Z&quot; |



