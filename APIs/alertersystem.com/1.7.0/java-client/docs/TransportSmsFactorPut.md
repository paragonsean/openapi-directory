

# TransportSmsFactorPut

The TransportSmsFactor resource is a collection of transports that carry dispatched alerts to the external SMSFactor service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**smsFactorPushType** | **String** | The push type for the SMSFactor service. |  |
|**smsFactorSender** | **String** | The sender value for the SMSFactor service. |  |
|**smsFactorToken** | **String** | The token for the SMSFactor service. Stored in encrypted format. |  |
|**transportName** | **String** | The name of the transport. |  |



