

# CreateWirelessDeviceRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | The wireless device type. |  |
|**name** | **String** | The name of the new resource. |  [optional] |
|**description** | **String** | The description of the new resource. |  [optional] |
|**destinationName** | **String** | The name of the destination to assign to the new wireless device. |  |
|**clientRequestToken** | **String** | Each resource must have a unique client request token. If you try to create a new resource with the same token as a resource that already exists, an exception occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. |  [optional] |
|**loRaWAN** | [**CreateWirelessDeviceRequestLoRaWAN**](CreateWirelessDeviceRequestLoRaWAN.md) |  |  [optional] |
|**tags** | [**List&lt;Tag&gt;**](Tag.md) | The tag to attach to the specified resource. Tags are metadata that you can use to manage a resource. |  [optional] |
|**positioning** | [**PositioningEnum**](#PositioningEnum) | FPort values for the GNSS, stream, and ClockSync functions of the positioning information. |  [optional] |
|**sidewalk** | [**CreateWirelessDeviceRequestSidewalk**](CreateWirelessDeviceRequestSidewalk.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SIDEWALK | &quot;Sidewalk&quot; |
| LO_RA_WAN | &quot;LoRaWAN&quot; |



## Enum: PositioningEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



