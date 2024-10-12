# AwsIoTWireless.StartSingleWirelessDeviceImportTaskRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinationName** | **String** | The name of the Sidewalk destination that describes the IoT rule to route messages from the device in the import task that will be onboarded to AWS IoT Wireless. | 
**clientRequestToken** | **String** | Each resource must have a unique client request token. If you try to create a new resource with the same token as a resource that already exists, an exception occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. | [optional] 
**deviceName** | **String** | The name of the wireless device for which an import task is being started. | [optional] 
**tags** | [**[Tag]**](Tag.md) | The tag to attach to the specified resource. Tags are metadata that you can use to manage a resource. | [optional] 
**sidewalk** | [**StartSingleWirelessDeviceImportTaskRequestSidewalk**](StartSingleWirelessDeviceImportTaskRequestSidewalk.md) |  | 


