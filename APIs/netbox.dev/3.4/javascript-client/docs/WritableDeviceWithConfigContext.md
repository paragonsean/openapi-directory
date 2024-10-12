# NetBoxApi.WritableDeviceWithConfigContext

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**airflow** | **String** |  | [optional] 
**assetTag** | **String** | A unique tag used to identify this device | [optional] 
**cluster** | **Number** |  | [optional] 
**comments** | **String** |  | [optional] 
**configContext** | **Object** |  | [optional] [readonly] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**deviceRole** | **Number** |  | 
**deviceType** | **Number** |  | 
**display** | **String** |  | [optional] [readonly] 
**face** | **String** |  | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**localContextData** | **Object** |  | [optional] 
**location** | **Number** |  | [optional] 
**name** | **String** |  | [optional] 
**parentDevice** | [**NestedDevice**](NestedDevice.md) |  | [optional] 
**platform** | **Number** |  | [optional] 
**position** | **Number** |  | [optional] 
**primaryIp** | **String** |  | [optional] [readonly] 
**primaryIp4** | **Number** |  | [optional] 
**primaryIp6** | **Number** |  | [optional] 
**rack** | **Number** |  | [optional] 
**serial** | **String** |  | [optional] 
**site** | **Number** |  | 
**status** | **String** |  | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**tenant** | **Number** |  | [optional] 
**url** | **String** |  | [optional] [readonly] 
**vcPosition** | **Number** |  | [optional] 
**vcPriority** | **Number** |  | [optional] 
**virtualChassis** | **Number** |  | [optional] 



## Enum: AirflowEnum


* `front-to-rear` (value: `"front-to-rear"`)

* `rear-to-front` (value: `"rear-to-front"`)

* `left-to-right` (value: `"left-to-right"`)

* `right-to-left` (value: `"right-to-left"`)

* `side-to-rear` (value: `"side-to-rear"`)

* `passive` (value: `"passive"`)

* `mixed` (value: `"mixed"`)





## Enum: FaceEnum


* `front` (value: `"front"`)

* `rear` (value: `"rear"`)





## Enum: StatusEnum


* `offline` (value: `"offline"`)

* `active` (value: `"active"`)

* `planned` (value: `"planned"`)

* `staged` (value: `"staged"`)

* `failed` (value: `"failed"`)

* `inventory` (value: `"inventory"`)

* `decommissioning` (value: `"decommissioning"`)




