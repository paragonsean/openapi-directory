

# WcfRelayProperties

Properties of the WcfRelay Properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | The time the WCFRelay was created. |  [optional] [readonly] |
|**isDynamic** | **Boolean** | true if the relay is dynamic; otherwise, false. |  [optional] [readonly] |
|**listenerCount** | **Integer** | The number of listeners for this relay. min : 1 and max:25 supported |  [optional] [readonly] |
|**relayType** | [**RelayTypeEnum**](#RelayTypeEnum) | WCFRelay Type. |  [optional] |
|**requiresClientAuthorization** | **Boolean** | true if client authorization is needed for this relay; otherwise, false. |  [optional] |
|**requiresTransportSecurity** | **Boolean** | true if transport security is needed for this relay; otherwise, false. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The time the namespace was updated. |  [optional] [readonly] |
|**userMetadata** | **String** | usermetadata is a placeholder to store user-defined string data for the HybridConnection endpoint.e.g. it can be used to store  descriptive data, such as list of teams and their contact information also user-defined configuration settings can be stored. |  [optional] |



## Enum: RelayTypeEnum

| Name | Value |
|---- | -----|
| NET_TCP | &quot;NetTcp&quot; |
| HTTP | &quot;Http&quot; |



