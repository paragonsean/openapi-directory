

# DeviceType


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comments** | **String** |  |  [optional] |
|**created** | **LocalDate** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**instanceCount** | **Integer** |  |  [optional] [readonly] |
|**interfaceOrdering** | [**InterfaceOrdering**](InterfaceOrdering.md) |  |  [optional] |
|**isConsoleServer** | **Boolean** | This type of device has console server ports |  [optional] |
|**isFullDepth** | **Boolean** | Device consumes both front and rear rack faces |  [optional] |
|**isNetworkDevice** | **Boolean** | This type of device has network interfaces |  [optional] |
|**isPdu** | **Boolean** | This type of device has power outlets |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**manufacturer** | [**NestedManufacturer**](NestedManufacturer.md) |  |  |
|**model** | **String** |  |  |
|**partNumber** | **String** | Discrete part number (optional) |  [optional] |
|**slug** | **String** |  |  |
|**subdeviceRole** | [**SubdeviceRole**](SubdeviceRole.md) |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**uHeight** | **Integer** |  |  [optional] |



