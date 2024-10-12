

# GoogleAdsSearchads360V0ResourcesAdGroupAsset

A link between an ad group and an asset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adGroup** | **String** | Required. Immutable. The ad group to which the asset is linked. |  [optional] |
|**asset** | **String** | Required. Immutable. The asset which is linked to the ad group. |  [optional] |
|**resourceName** | **String** | Immutable. The resource name of the ad group asset. AdGroupAsset resource names have the form: &#x60;customers/{customer_id}/adGroupAssets/{ad_group_id}~{asset_id}~{field_type}&#x60; |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the ad group asset. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ENABLED | &quot;ENABLED&quot; |
| REMOVED | &quot;REMOVED&quot; |
| PAUSED | &quot;PAUSED&quot; |



