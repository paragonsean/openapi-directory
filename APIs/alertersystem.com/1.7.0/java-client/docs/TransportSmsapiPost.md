

# TransportSmsapiPost

The TransportSmsapi resource is a collection of transports that carry dispatched alerts to the external SMS API service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**smsapiFrom** | **String** | The sender name for the SMS API service. |  |
|**smsapiToken** | **String** | The API token for the SMS API service. Stored in encrypted format. |  |
|**transportName** | **String** | The name of the transport. |  |



