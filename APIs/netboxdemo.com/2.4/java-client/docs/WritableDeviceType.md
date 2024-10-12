

# WritableDeviceType


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comments** | **String** |  |  [optional] |
|**created** | **LocalDate** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**instanceCount** | **Integer** |  |  [optional] [readonly] |
|**interfaceOrdering** | [**InterfaceOrderingEnum**](#InterfaceOrderingEnum) |  |  [optional] |
|**isConsoleServer** | **Boolean** | This type of device has console server ports |  [optional] |
|**isFullDepth** | **Boolean** | Device consumes both front and rear rack faces |  [optional] |
|**isNetworkDevice** | **Boolean** | This type of device has network interfaces |  [optional] |
|**isPdu** | **Boolean** | This type of device has power outlets |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**manufacturer** | **Integer** |  |  |
|**model** | **String** |  |  |
|**partNumber** | **String** | Discrete part number (optional) |  [optional] |
|**slug** | **String** |  |  |
|**subdeviceRole** | **Boolean** | Parent devices house child devices in device bays. Select \&quot;None\&quot; if this device type is neither a parent nor a child. |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**uHeight** | **Integer** |  |  [optional] |



## Enum: InterfaceOrderingEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |



