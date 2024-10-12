

# TransportGatewayApiPost

The TransportGatewayApi resource is a collection of transports that carry dispatched alerts to the external GatewayAPI service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**gatewayApiFrom** | **String** | The sender name for the Gateway API service. |  |
|**gatewayApiToken** | **String** | The token for the Gateway API service. Stored in encrypted format. |  |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**transportName** | **String** | The name of the transport. |  |



