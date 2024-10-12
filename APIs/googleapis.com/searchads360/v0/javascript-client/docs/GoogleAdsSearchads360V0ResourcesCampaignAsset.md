# SearchAds360ReportingApi.GoogleAdsSearchads360V0ResourcesCampaignAsset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **String** | Immutable. The asset which is linked to the campaign. | [optional] 
**campaign** | **String** | Immutable. The campaign to which the asset is linked. | [optional] 
**resourceName** | **String** | Immutable. The resource name of the campaign asset. CampaignAsset resource names have the form: &#x60;customers/{customer_id}/campaignAssets/{campaign_id}~{asset_id}~{field_type}&#x60; | [optional] 
**status** | **String** | Output only. Status of the campaign asset. | [optional] [readonly] 



## Enum: StatusEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `ENABLED` (value: `"ENABLED"`)

* `REMOVED` (value: `"REMOVED"`)

* `PAUSED` (value: `"PAUSED"`)




