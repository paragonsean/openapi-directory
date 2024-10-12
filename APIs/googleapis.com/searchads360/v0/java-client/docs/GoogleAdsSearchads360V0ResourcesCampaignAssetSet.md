

# GoogleAdsSearchads360V0ResourcesCampaignAssetSet

CampaignAssetSet is the linkage between a campaign and an asset set. Adding a CampaignAssetSet links an asset set with a campaign.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetSet** | **String** | Immutable. The asset set which is linked to the campaign. |  [optional] |
|**campaign** | **String** | Immutable. The campaign to which this asset set is linked. |  [optional] |
|**resourceName** | **String** | Immutable. The resource name of the campaign asset set. Asset set asset resource names have the form: &#x60;customers/{customer_id}/campaignAssetSets/{campaign_id}~{asset_set_id}&#x60; |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Output only. The status of the campaign asset set asset. Read-only. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ENABLED | &quot;ENABLED&quot; |
| REMOVED | &quot;REMOVED&quot; |



