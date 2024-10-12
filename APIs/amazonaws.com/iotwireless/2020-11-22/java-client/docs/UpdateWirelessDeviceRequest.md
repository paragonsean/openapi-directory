

# UpdateWirelessDeviceRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destinationName** | **String** | The name of the new destination for the device. |  [optional] |
|**name** | **String** | The new name of the resource. |  [optional] |
|**description** | **String** | The description of the new resource. |  [optional] |
|**loRaWAN** | [**UpdateWirelessDeviceRequestLoRaWAN**](UpdateWirelessDeviceRequestLoRaWAN.md) |  |  [optional] |
|**positioning** | [**PositioningEnum**](#PositioningEnum) | FPort values for the GNSS, stream, and ClockSync functions of the positioning information. |  [optional] |



## Enum: PositioningEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



