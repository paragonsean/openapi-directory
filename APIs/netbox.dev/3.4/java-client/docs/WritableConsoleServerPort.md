

# WritableConsoleServerPort


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**occupied** | **Boolean** |  |  [optional] [readonly] |
|**cable** | [**NestedCable**](NestedCable.md) |  |  [optional] |
|**cableEnd** | **String** |  |  [optional] [readonly] |
|**connectedEndpoints** | **List&lt;String&gt;** |  Return the appropriate serializer for the type of connected object.  |  [optional] [readonly] |
|**connectedEndpointsReachable** | **Boolean** |  |  [optional] [readonly] |
|**connectedEndpointsType** | **String** |  |  [optional] [readonly] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**device** | **Integer** |  |  |
|**display** | **String** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**label** | **String** | Physical label |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**linkPeers** | **List&lt;String&gt;** |  Return the appropriate serializer for the link termination model.  |  [optional] [readonly] |
|**linkPeersType** | **String** |  |  [optional] [readonly] |
|**markConnected** | **Boolean** | Treat as if a cable is connected |  [optional] |
|**module** | **Integer** |  |  [optional] |
|**name** | **String** |  |  |
|**speed** | [**SpeedEnum**](#SpeedEnum) | Port speed in bits per second |  [optional] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Physical port type |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |



## Enum: SpeedEnum

| Name | Value |
|---- | -----|
| NUMBER_1200 | 1200 |
| NUMBER_2400 | 2400 |
| NUMBER_4800 | 4800 |
| NUMBER_9600 | 9600 |
| NUMBER_19200 | 19200 |
| NUMBER_38400 | 38400 |
| NUMBER_57600 | 57600 |
| NUMBER_115200 | 115200 |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DE_9 | &quot;de-9&quot; |
| DB_25 | &quot;db-25&quot; |
| RJ_11 | &quot;rj-11&quot; |
| RJ_12 | &quot;rj-12&quot; |
| RJ_45 | &quot;rj-45&quot; |
| MINI_DIN_8 | &quot;mini-din-8&quot; |
| USB_A | &quot;usb-a&quot; |
| USB_B | &quot;usb-b&quot; |
| USB_C | &quot;usb-c&quot; |
| USB_MINI_A | &quot;usb-mini-a&quot; |
| USB_MINI_B | &quot;usb-mini-b&quot; |
| USB_MICRO_A | &quot;usb-micro-a&quot; |
| USB_MICRO_B | &quot;usb-micro-b&quot; |
| USB_MICRO_AB | &quot;usb-micro-ab&quot; |
| OTHER | &quot;other&quot; |



