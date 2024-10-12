

# WritablePowerFeed


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**occupied** | **Boolean** |  |  [optional] [readonly] |
|**amperage** | **Integer** |  |  [optional] |
|**cable** | [**NestedCable**](NestedCable.md) |  |  [optional] |
|**cableEnd** | **String** |  |  [optional] [readonly] |
|**comments** | **String** |  |  [optional] |
|**connectedEndpoints** | **List&lt;String&gt;** |  Return the appropriate serializer for the type of connected object.  |  [optional] [readonly] |
|**connectedEndpointsReachable** | **Boolean** |  |  [optional] [readonly] |
|**connectedEndpointsType** | **String** |  |  [optional] [readonly] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**display** | **String** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**linkPeers** | **List&lt;String&gt;** |  Return the appropriate serializer for the link termination model.  |  [optional] [readonly] |
|**linkPeersType** | **String** |  |  [optional] [readonly] |
|**markConnected** | **Boolean** | Treat as if a cable is connected |  [optional] |
|**maxUtilization** | **Integer** | Maximum permissible draw (percentage) |  [optional] |
|**name** | **String** |  |  |
|**phase** | [**PhaseEnum**](#PhaseEnum) |  |  [optional] |
|**powerPanel** | **Integer** |  |  |
|**rack** | **Integer** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**supply** | [**SupplyEnum**](#SupplyEnum) |  |  [optional] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |
|**voltage** | **Integer** |  |  [optional] |



## Enum: PhaseEnum

| Name | Value |
|---- | -----|
| SINGLE_PHASE | &quot;single-phase&quot; |
| THREE_PHASE | &quot;three-phase&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OFFLINE | &quot;offline&quot; |
| ACTIVE | &quot;active&quot; |
| PLANNED | &quot;planned&quot; |
| FAILED | &quot;failed&quot; |



## Enum: SupplyEnum

| Name | Value |
|---- | -----|
| AC | &quot;ac&quot; |
| DC | &quot;dc&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PRIMARY | &quot;primary&quot; |
| REDUNDANT | &quot;redundant&quot; |



