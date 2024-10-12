# NetBoxApi.WritableDeviceType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**airflow** | **String** |  | [optional] 
**comments** | **String** |  | [optional] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**deviceCount** | **Number** |  | [optional] [readonly] 
**display** | **String** |  | [optional] [readonly] 
**frontImage** | **String** |  | [optional] [readonly] 
**id** | **Number** |  | [optional] [readonly] 
**isFullDepth** | **Boolean** | Device consumes both front and rear rack faces | [optional] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**manufacturer** | **Number** |  | 
**model** | **String** |  | 
**partNumber** | **String** | Discrete part number (optional) | [optional] 
**rearImage** | **String** |  | [optional] [readonly] 
**slug** | **String** |  | 
**subdeviceRole** | **String** | Parent devices house child devices in device bays. Leave blank if this device type is neither a parent nor a child. | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**uHeight** | **Number** |  | [optional] [default to 1]
**url** | **String** |  | [optional] [readonly] 
**weight** | **Number** |  | [optional] 
**weightUnit** | **String** |  | [optional] 



## Enum: AirflowEnum


* `front-to-rear` (value: `"front-to-rear"`)

* `rear-to-front` (value: `"rear-to-front"`)

* `left-to-right` (value: `"left-to-right"`)

* `right-to-left` (value: `"right-to-left"`)

* `side-to-rear` (value: `"side-to-rear"`)

* `passive` (value: `"passive"`)

* `mixed` (value: `"mixed"`)





## Enum: SubdeviceRoleEnum


* `parent` (value: `"parent"`)

* `child` (value: `"child"`)





## Enum: WeightUnitEnum


* `kg` (value: `"kg"`)

* `g` (value: `"g"`)

* `lb` (value: `"lb"`)

* `oz` (value: `"oz"`)




