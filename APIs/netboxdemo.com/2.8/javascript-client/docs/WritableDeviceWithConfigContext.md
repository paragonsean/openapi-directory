# NetBoxApi.WritableDeviceWithConfigContext

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assetTag** | **String** | A unique tag used to identify this device | [optional] 
**cluster** | **Number** |  | [optional] 
**comments** | **String** |  | [optional] 
**configContext** | **{String: String}** |  | [optional] [readonly] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**deviceRole** | **Number** |  | 
**deviceType** | **Number** |  | 
**displayName** | **String** |  | [optional] [readonly] 
**face** | **String** |  | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**localContextData** | **String** |  | [optional] 
**name** | **String** |  | [optional] 
**parentDevice** | [**NestedDevice**](NestedDevice.md) |  | [optional] 
**platform** | **Number** |  | [optional] 
**position** | **Number** | The lowest-numbered unit occupied by the device | [optional] 
**primaryIp** | **String** |  | [optional] [readonly] 
**primaryIp4** | **Number** |  | [optional] 
**primaryIp6** | **Number** |  | [optional] 
**rack** | **Number** |  | [optional] 
**serial** | **String** |  | [optional] 
**site** | **Number** |  | 
**status** | **String** |  | [optional] 
**tags** | **[String]** |  | [optional] 
**tenant** | **Number** |  | [optional] 
**vcPosition** | **Number** |  | [optional] 
**vcPriority** | **Number** |  | [optional] 
**virtualChassis** | **Number** |  | [optional] 



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




