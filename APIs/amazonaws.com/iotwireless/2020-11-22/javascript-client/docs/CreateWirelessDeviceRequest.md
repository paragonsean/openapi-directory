# AwsIoTWireless.CreateWirelessDeviceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **String** | The wireless device type. | 
**name** | **String** | The name of the new resource. | [optional] 
**description** | **String** | The description of the new resource. | [optional] 
**destinationName** | **String** | The name of the destination to assign to the new wireless device. | 
**clientRequestToken** | **String** | Each resource must have a unique client request token. If you try to create a new resource with the same token as a resource that already exists, an exception occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. | [optional] 
**loRaWAN** | [**CreateWirelessDeviceRequestLoRaWAN**](CreateWirelessDeviceRequestLoRaWAN.md) |  | [optional] 
**tags** | [**[Tag]**](Tag.md) | The tag to attach to the specified resource. Tags are metadata that you can use to manage a resource. | [optional] 
**positioning** | **String** | FPort values for the GNSS, stream, and ClockSync functions of the positioning information. | [optional] 
**sidewalk** | [**CreateWirelessDeviceRequestSidewalk**](CreateWirelessDeviceRequestSidewalk.md) |  | [optional] 



## Enum: TypeEnum


* `Sidewalk` (value: `"Sidewalk"`)

* `LoRaWAN` (value: `"LoRaWAN"`)





## Enum: PositioningEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




