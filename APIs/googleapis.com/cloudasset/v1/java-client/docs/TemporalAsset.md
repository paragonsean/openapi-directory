

# TemporalAsset

An asset in Google Cloud and its temporal metadata, including the time window when it was observed and its status during that window.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**asset** | [**Asset**](Asset.md) |  |  [optional] |
|**deleted** | **Boolean** | Whether the asset has been deleted or not. |  [optional] |
|**priorAsset** | [**Asset**](Asset.md) |  |  [optional] |
|**priorAssetState** | [**PriorAssetStateEnum**](#PriorAssetStateEnum) | State of prior_asset. |  [optional] |
|**window** | [**TimeWindow**](TimeWindow.md) |  |  [optional] |



## Enum: PriorAssetStateEnum

| Name | Value |
|---- | -----|
| PRIOR_ASSET_STATE_UNSPECIFIED | &quot;PRIOR_ASSET_STATE_UNSPECIFIED&quot; |
| PRESENT | &quot;PRESENT&quot; |
| INVALID | &quot;INVALID&quot; |
| DOES_NOT_EXIST | &quot;DOES_NOT_EXIST&quot; |
| DELETED | &quot;DELETED&quot; |



