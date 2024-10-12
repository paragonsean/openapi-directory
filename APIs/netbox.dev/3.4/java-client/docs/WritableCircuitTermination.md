

# WritableCircuitTermination


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**occupied** | **Boolean** |  |  [optional] [readonly] |
|**cable** | [**NestedCable**](NestedCable.md) |  |  [optional] |
|**cableEnd** | **String** |  |  [optional] [readonly] |
|**circuit** | **Integer** |  |  |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**display** | **String** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**linkPeers** | **List&lt;String&gt;** |  Return the appropriate serializer for the link termination model.  |  [optional] [readonly] |
|**linkPeersType** | **String** |  |  [optional] [readonly] |
|**markConnected** | **Boolean** | Treat as if a cable is connected |  [optional] |
|**portSpeed** | **Integer** |  |  [optional] |
|**ppInfo** | **String** |  |  [optional] |
|**providerNetwork** | **Integer** |  |  [optional] |
|**site** | **Integer** |  |  [optional] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**termSide** | [**TermSideEnum**](#TermSideEnum) |  |  |
|**upstreamSpeed** | **Integer** | Upstream speed, if different from port speed |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |
|**xconnectId** | **String** |  |  [optional] |



## Enum: TermSideEnum

| Name | Value |
|---- | -----|
| A | &quot;A&quot; |
| Z | &quot;Z&quot; |



