

# TransportTurboSmsJsonldPut

The TransportTurboSms resource is a collection of transports that carry dispatched alerts to the external TurboSms service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**transportName** | **String** | The name of the transport. |  |
|**turboSmsAuthToken** | **String** | The auth token for the TurboSms service. Stored in encrypted format. |  |
|**turboSmsFrom** | **String** | The sender name (should be alphanumeric, max 20 characters and activated in your TurboSms account) for the TurboSms service. |  |



