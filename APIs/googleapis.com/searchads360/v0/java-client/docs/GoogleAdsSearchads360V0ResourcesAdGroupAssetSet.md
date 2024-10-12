

# GoogleAdsSearchads360V0ResourcesAdGroupAssetSet

AdGroupAssetSet is the linkage between an ad group and an asset set. Creating an AdGroupAssetSet links an asset set with an ad group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adGroup** | **String** | Immutable. The ad group to which this asset set is linked. |  [optional] |
|**assetSet** | **String** | Immutable. The asset set which is linked to the ad group. |  [optional] |
|**resourceName** | **String** | Immutable. The resource name of the ad group asset set. Ad group asset set resource names have the form: &#x60;customers/{customer_id}/adGroupAssetSets/{ad_group_id}~{asset_set_id}&#x60; |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Output only. The status of the ad group asset set. Read-only. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ENABLED | &quot;ENABLED&quot; |
| REMOVED | &quot;REMOVED&quot; |



