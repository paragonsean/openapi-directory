

# WritableDeviceType


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**airflow** | [**AirflowEnum**](#AirflowEnum) |  |  [optional] |
|**comments** | **String** |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**deviceCount** | **Integer** |  |  [optional] [readonly] |
|**display** | **String** |  |  [optional] [readonly] |
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
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**uHeight** | **BigDecimal** |  |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |
|**weight** | **BigDecimal** |  |  [optional] |
|**weightUnit** | [**WeightUnitEnum**](#WeightUnitEnum) |  |  [optional] |



## Enum: AirflowEnum

| Name | Value |
|---- | -----|
| FRONT_TO_REAR | &quot;front-to-rear&quot; |
| REAR_TO_FRONT | &quot;rear-to-front&quot; |
| LEFT_TO_RIGHT | &quot;left-to-right&quot; |
| RIGHT_TO_LEFT | &quot;right-to-left&quot; |
| SIDE_TO_REAR | &quot;side-to-rear&quot; |
| PASSIVE | &quot;passive&quot; |
| MIXED | &quot;mixed&quot; |



## Enum: SubdeviceRoleEnum

| Name | Value |
|---- | -----|
| PARENT | &quot;parent&quot; |
| CHILD | &quot;child&quot; |



## Enum: WeightUnitEnum

| Name | Value |
|---- | -----|
| KG | &quot;kg&quot; |
| G | &quot;g&quot; |
| LB | &quot;lb&quot; |
| OZ | &quot;oz&quot; |



