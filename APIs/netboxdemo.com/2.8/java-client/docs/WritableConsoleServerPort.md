

# WritableConsoleServerPort


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cable** | [**NestedCable**](NestedCable.md) |  |  [optional] |
|**connectedEndpoint** | **Map&lt;String, String&gt;** |  Return the appropriate serializer for the type of connected object.  |  [optional] [readonly] |
|**connectedEndpointType** | **String** |  |  [optional] [readonly] |
|**connectionStatus** | **Boolean** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**device** | **Integer** |  |  |
|**id** | **Integer** |  |  [optional] [readonly] |
|**name** | **String** |  |  |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Physical port type |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DE_9 | &quot;de-9&quot; |
| DB_25 | &quot;db-25&quot; |
| RJ_11 | &quot;rj-11&quot; |
| RJ_12 | &quot;rj-12&quot; |
| RJ_45 | &quot;rj-45&quot; |
| USB_A | &quot;usb-a&quot; |
| USB_B | &quot;usb-b&quot; |
| USB_C | &quot;usb-c&quot; |
| USB_MINI_A | &quot;usb-mini-a&quot; |
| USB_MINI_B | &quot;usb-mini-b&quot; |
| USB_MICRO_A | &quot;usb-micro-a&quot; |
| USB_MICRO_B | &quot;usb-micro-b&quot; |
| OTHER | &quot;other&quot; |



