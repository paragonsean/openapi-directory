

# TransportTwilioJsonldPost

The TransportTwilio resource is a collection of transports that carry dispatched alerts to the external Twilio service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**transportName** | **String** | The name of the transport. |  |
|**twilioFrom** | **String** | The sender for the Twilio service. |  |
|**twilioSid** | **String** | The SID for the Twilio service. |  |
|**twilioToken** | **String** | The token for the Twilio service. Stored in encrypted format. |  |



