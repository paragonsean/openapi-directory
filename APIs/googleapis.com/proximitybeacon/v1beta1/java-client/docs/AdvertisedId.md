

# AdvertisedId

Defines a unique identifier of a beacon as broadcast by the device.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **byte[]** | The actual beacon identifier, as broadcast by the beacon hardware. Must be [base64](http://tools.ietf.org/html/rfc4648#section-4) encoded in HTTP requests, and will be so encoded (with padding) in responses. The base64 encoding should be of the binary byte-stream and not any textual (such as hex) representation thereof. Required. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Specifies the identifier type. Required. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| EDDYSTONE | &quot;EDDYSTONE&quot; |
| IBEACON | &quot;IBEACON&quot; |
| ALTBEACON | &quot;ALTBEACON&quot; |
| EDDYSTONE_EID | &quot;EDDYSTONE_EID&quot; |



