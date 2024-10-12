

# GetNetworkEvents200ResponseEventsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | **String** | The category that the event type belongs to |  [optional] |
|**clientDescription** | **String** | A description of the client. This is usually the client&#39;s device name. |  [optional] |
|**clientId** | **String** | A string identifying the client. This could be a client&#39;s MAC or IP address |  [optional] |
|**clientMac** | **String** | The client&#39;s MAC address. |  [optional] |
|**description** | **String** | A description of the event the happened. |  [optional] |
|**deviceName** | **String** | The name of the device. Only shown if the device is an access point. |  [optional] |
|**deviceSerial** | **String** | The serial number of the device. Only shown if the device is an access point. |  [optional] |
|**eventData** | [**GetNetworkEvents200ResponseEventsInnerEventData**](GetNetworkEvents200ResponseEventsInnerEventData.md) |  |  [optional] |
|**networkId** | **String** | The ID of the network. |  [optional] |
|**occurredAt** | **String** | An UTC ISO8601 string of the time the event occurred at. |  [optional] |
|**ssidNumber** | **Integer** | The SSID number of the device. |  [optional] |
|**type** | **String** | The type of event being listed. |  [optional] |



