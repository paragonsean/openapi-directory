

# Device

Third-party device definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | **Map&lt;String, Object&gt;** | Attributes for the traits supported by the device. |  [optional] |
|**customData** | **Map&lt;String, Object&gt;** | Custom device attributes stored in Home Graph and provided to your smart home Action in each [QUERY](https://developers.home.google.com/cloud-to-cloud/intents/query) and [EXECUTE](https://developers.home.google.com/cloud-to-cloud/intents/execute) intent. Data in this object has a few constraints: No sensitive information, including but not limited to Personally Identifiable Information. |  [optional] |
|**deviceInfo** | [**DeviceInfo**](DeviceInfo.md) |  |  [optional] |
|**id** | **String** | Third-party device ID. |  [optional] |
|**name** | [**DeviceNames**](DeviceNames.md) |  |  [optional] |
|**notificationSupportedByAgent** | **Boolean** | Indicates whether your smart home Action will report notifications to Google for this device via ReportStateAndNotification. If your smart home Action enables users to control device notifications, you should update this field and call RequestSyncDevices. |  [optional] |
|**otherDeviceIds** | [**List&lt;AgentOtherDeviceId&gt;**](AgentOtherDeviceId.md) | Alternate IDs associated with this device. This is used to identify cloud synced devices enabled for [local fulfillment](https://developers.home.google.com/local-home/overview). |  [optional] |
|**roomHint** | **String** | Suggested name for the room where this device is installed. Google attempts to use this value during user setup. |  [optional] |
|**structureHint** | **String** | Suggested name for the structure where this device is installed. Google attempts to use this value during user setup. |  [optional] |
|**traits** | **List&lt;String&gt;** | Traits supported by the device. See [device traits](https://developers.home.google.com/cloud-to-cloud/traits). |  [optional] |
|**type** | **String** | Hardware type of the device. See [device types](https://developers.home.google.com/cloud-to-cloud/guides). |  [optional] |
|**willReportState** | **Boolean** | Indicates whether your smart home Action will report state of this device to Google via ReportStateAndNotification. |  [optional] |



