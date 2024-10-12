

# GoogleAdsSearchads360V0ResourcesAssetGroup

An asset group. AssetGroupAsset is used to link an asset to the asset group. AssetGroupSignal is used to associate a signal to an asset group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adStrength** | [**AdStrengthEnum**](#AdStrengthEnum) | Output only. Overall ad strength of this asset group. |  [optional] [readonly] |
|**campaign** | **String** | Immutable. The campaign with which this asset group is associated. The asset which is linked to the asset group. |  [optional] |
|**finalMobileUrls** | **List&lt;String&gt;** | A list of final mobile URLs after all cross domain redirects. In performance max, by default, the urls are eligible for expansion unless opted out. |  [optional] |
|**finalUrls** | **List&lt;String&gt;** | A list of final URLs after all cross domain redirects. In performance max, by default, the urls are eligible for expansion unless opted out. |  [optional] |
|**id** | **String** | Output only. The ID of the asset group. |  [optional] [readonly] |
|**name** | **String** | Required. Name of the asset group. Required. It must have a minimum length of 1 and maximum length of 128. It must be unique under a campaign. |  [optional] |
|**path1** | **String** | First part of text that may appear appended to the url displayed in the ad. |  [optional] |
|**path2** | **String** | Second part of text that may appear appended to the url displayed in the ad. This field can only be set when path1 is set. |  [optional] |
|**resourceName** | **String** | Immutable. The resource name of the asset group. Asset group resource names have the form: &#x60;customers/{customer_id}/assetGroups/{asset_group_id}&#x60; |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the asset group. |  [optional] |



## Enum: AdStrengthEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| PENDING | &quot;PENDING&quot; |
| NO_ADS | &quot;NO_ADS&quot; |
| POOR | &quot;POOR&quot; |
| AVERAGE | &quot;AVERAGE&quot; |
| GOOD | &quot;GOOD&quot; |
| EXCELLENT | &quot;EXCELLENT&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ENABLED | &quot;ENABLED&quot; |
| PAUSED | &quot;PAUSED&quot; |
| REMOVED | &quot;REMOVED&quot; |



