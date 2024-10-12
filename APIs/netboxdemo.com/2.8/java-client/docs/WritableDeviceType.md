

# WritableDeviceType


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comments** | **String** |  |  [optional] |
|**created** | **LocalDate** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**deviceCount** | **Integer** |  |  [optional] [readonly] |
|**displayName** | **String** |  |  [optional] [readonly] |
|**frontImage** | **URI** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**isFullDepth** | **Boolean** | Device consumes both front and rear rack faces |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**manufacturer** | **Integer** |  |  |
|**model** | **String** |  |  |
|**partNumber** | **String** | Discrete part number (optional) |  [optional] |
|**rearImage** | **URI** |  |  [optional] [readonly] |
|**slug** | **String** |  |  |
|**subdeviceRole** | [**SubdeviceRoleEnum**](#SubdeviceRoleEnum) | Parent devices house child devices in device bays. Leave blank if this device type is neither a parent nor a child. |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**uHeight** | **Integer** |  |  [optional] |



## Enum: SubdeviceRoleEnum

| Name | Value |
|---- | -----|
| PARENT | &quot;parent&quot; |
| CHILD | &quot;child&quot; |



