# NetBoxApi.WritableDeviceType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **String** |  | [optional] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**deviceCount** | **Number** |  | [optional] [readonly] 
**displayName** | **String** |  | [optional] [readonly] 
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
**tags** | **[String]** |  | [optional] 
**uHeight** | **Number** |  | [optional] 



## Enum: SubdeviceRoleEnum


* `parent` (value: `"parent"`)

* `child` (value: `"child"`)




