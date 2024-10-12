# CloudAssetApi.TemporalAsset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | [**Asset**](Asset.md) |  | [optional] 
**deleted** | **Boolean** | Whether the asset has been deleted or not. | [optional] 
**priorAsset** | [**Asset**](Asset.md) |  | [optional] 
**priorAssetState** | **String** | State of prior_asset. | [optional] 
**window** | [**TimeWindow**](TimeWindow.md) |  | [optional] 



## Enum: PriorAssetStateEnum


* `PRIOR_ASSET_STATE_UNSPECIFIED` (value: `"PRIOR_ASSET_STATE_UNSPECIFIED"`)

* `PRESENT` (value: `"PRESENT"`)

* `INVALID` (value: `"INVALID"`)

* `DOES_NOT_EXIST` (value: `"DOES_NOT_EXIST"`)

* `DELETED` (value: `"DELETED"`)




