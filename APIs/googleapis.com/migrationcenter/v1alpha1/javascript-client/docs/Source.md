# MigrationCenterApi.Source

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The timestamp when the source was created. | [optional] [readonly] 
**description** | **String** | Free-text description. | [optional] 
**displayName** | **String** | User-friendly display name. | [optional] 
**errorFrameCount** | **Number** | Output only. The number of frames that were reported by the source and contained errors. | [optional] [readonly] 
**isManaged** | **Boolean** | If &#x60;true&#x60;, the source is managed by other service(s). | [optional] 
**name** | **String** | Output only. The full name of the source. | [optional] [readonly] 
**pendingFrameCount** | **Number** | Output only. Number of frames that are still being processed. | [optional] [readonly] 
**priority** | **Number** | The information confidence of the source. The higher the value, the higher the confidence. | [optional] 
**state** | **String** | Output only. The state of the source. | [optional] [readonly] 
**type** | **String** | Data source type. | [optional] 
**updateTime** | **String** | Output only. The timestamp when the source was last updated. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DELETING` (value: `"DELETING"`)

* `INVALID` (value: `"INVALID"`)





## Enum: TypeEnum


* `UNKNOWN` (value: `"SOURCE_TYPE_UNKNOWN"`)

* `UPLOAD` (value: `"SOURCE_TYPE_UPLOAD"`)

* `GUEST_OS_SCAN` (value: `"SOURCE_TYPE_GUEST_OS_SCAN"`)

* `INVENTORY_SCAN` (value: `"SOURCE_TYPE_INVENTORY_SCAN"`)

* `CUSTOM` (value: `"SOURCE_TYPE_CUSTOM"`)




