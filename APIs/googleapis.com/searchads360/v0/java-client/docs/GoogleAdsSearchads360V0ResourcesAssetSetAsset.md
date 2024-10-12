

# GoogleAdsSearchads360V0ResourcesAssetSetAsset

AssetSetAsset is the link between an asset and an asset set. Adding an AssetSetAsset links an asset with an asset set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**asset** | **String** | Immutable. The asset which this asset set asset is linking to. |  [optional] |
|**assetSet** | **String** | Immutable. The asset set which this asset set asset is linking to. |  [optional] |
|**resourceName** | **String** | Immutable. The resource name of the asset set asset. Asset set asset resource names have the form: &#x60;customers/{customer_id}/assetSetAssets/{asset_set_id}~{asset_id}&#x60; |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Output only. The status of the asset set asset. Read-only. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ENABLED | &quot;ENABLED&quot; |
| REMOVED | &quot;REMOVED&quot; |



