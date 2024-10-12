# SearchAds360ReportingApi.GoogleAdsSearchads360V0ResourcesAssetGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adStrength** | **String** | Output only. Overall ad strength of this asset group. | [optional] [readonly] 
**campaign** | **String** | Immutable. The campaign with which this asset group is associated. The asset which is linked to the asset group. | [optional] 
**finalMobileUrls** | **[String]** | A list of final mobile URLs after all cross domain redirects. In performance max, by default, the urls are eligible for expansion unless opted out. | [optional] 
**finalUrls** | **[String]** | A list of final URLs after all cross domain redirects. In performance max, by default, the urls are eligible for expansion unless opted out. | [optional] 
**id** | **String** | Output only. The ID of the asset group. | [optional] [readonly] 
**name** | **String** | Required. Name of the asset group. Required. It must have a minimum length of 1 and maximum length of 128. It must be unique under a campaign. | [optional] 
**path1** | **String** | First part of text that may appear appended to the url displayed in the ad. | [optional] 
**path2** | **String** | Second part of text that may appear appended to the url displayed in the ad. This field can only be set when path1 is set. | [optional] 
**resourceName** | **String** | Immutable. The resource name of the asset group. Asset group resource names have the form: &#x60;customers/{customer_id}/assetGroups/{asset_group_id}&#x60; | [optional] 
**status** | **String** | The status of the asset group. | [optional] 



## Enum: AdStrengthEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `PENDING` (value: `"PENDING"`)

* `NO_ADS` (value: `"NO_ADS"`)

* `POOR` (value: `"POOR"`)

* `AVERAGE` (value: `"AVERAGE"`)

* `GOOD` (value: `"GOOD"`)

* `EXCELLENT` (value: `"EXCELLENT"`)





## Enum: StatusEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `ENABLED` (value: `"ENABLED"`)

* `PAUSED` (value: `"PAUSED"`)

* `REMOVED` (value: `"REMOVED"`)




