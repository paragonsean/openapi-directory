

# TransportOrangeSmsPut

The TransportOrangeSms resource is a collection of transports that carry dispatched alerts to the external Orange SMS service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**orangeSmsClientId** | **String** | The app client ID for the Orange SMS service. |  |
|**orangeSmsClientSecret** | **String** | The app client secret for the Orange SMS service. Stored in encrypted format. |  |
|**orangeSmsFrom** | **String** | The sender phone number for the Orange SMS service. |  |
|**orangeSmsSenderName** | **String** | The sender name for the Orange SMS service. |  |
|**transportName** | **String** | The name of the transport. |  |



