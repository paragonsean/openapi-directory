

# TransportSinchJsonldPost

The TransportSinch resource is a collection of transports that carry dispatched alerts to the external Sinch service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**sinchAuthToken** | **String** | The auth token for the Sinch service. Stored in encrypted format. |  |
|**sinchFrom** | **String** | The sender for the Sinch service. |  |
|**sinchServicePlanId** | **String** | The service plan ID for the Sinch service. |  |
|**transportName** | **String** | The name of the transport. |  |



