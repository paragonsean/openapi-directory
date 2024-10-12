# DisplayVideo360Api.CreateSdfDownloadTaskRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiserId** | **String** | The ID of the advertiser to download SDF for. | [optional] 
**idFilter** | [**IdFilter**](IdFilter.md) |  | [optional] 
**inventorySourceFilter** | [**InventorySourceFilter**](InventorySourceFilter.md) |  | [optional] 
**parentEntityFilter** | [**ParentEntityFilter**](ParentEntityFilter.md) |  | [optional] 
**partnerId** | **String** | The ID of the partner to download SDF for. | [optional] 
**version** | **String** | Required. The SDF version of the downloaded file. If set to &#x60;SDF_VERSION_UNSPECIFIED&#x60;, this will default to the version specified by the advertiser or partner identified by &#x60;root_id&#x60;. An advertiser inherits its SDF version from its partner unless configured otherwise. | [optional] 



## Enum: VersionEnum


* `UNSPECIFIED` (value: `"SDF_VERSION_UNSPECIFIED"`)

* `3_1` (value: `"SDF_VERSION_3_1"`)

* `4` (value: `"SDF_VERSION_4"`)

* `4_1` (value: `"SDF_VERSION_4_1"`)

* `4_2` (value: `"SDF_VERSION_4_2"`)

* `5` (value: `"SDF_VERSION_5"`)

* `5_1` (value: `"SDF_VERSION_5_1"`)

* `5_2` (value: `"SDF_VERSION_5_2"`)

* `5_3` (value: `"SDF_VERSION_5_3"`)

* `5_4` (value: `"SDF_VERSION_5_4"`)

* `5_5` (value: `"SDF_VERSION_5_5"`)

* `6` (value: `"SDF_VERSION_6"`)

* `7` (value: `"SDF_VERSION_7"`)




