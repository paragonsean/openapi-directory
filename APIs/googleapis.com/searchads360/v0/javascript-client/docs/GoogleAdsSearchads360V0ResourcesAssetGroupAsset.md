# SearchAds360ReportingApi.GoogleAdsSearchads360V0ResourcesAssetGroupAsset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **String** | Immutable. The asset which this asset group asset is linking. | [optional] 
**assetGroup** | **String** | Immutable. The asset group which this asset group asset is linking. | [optional] 
**fieldType** | **String** | The description of the placement of the asset within the asset group. For example: HEADLINE, YOUTUBE_VIDEO etc | [optional] 
**resourceName** | **String** | Immutable. The resource name of the asset group asset. Asset group asset resource name have the form: &#x60;customers/{customer_id}/assetGroupAssets/{asset_group_id}~{asset_id}~{field_type}&#x60; | [optional] 
**status** | **String** | The status of the link between an asset and asset group. | [optional] 



## Enum: FieldTypeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `HEADLINE` (value: `"HEADLINE"`)

* `DESCRIPTION` (value: `"DESCRIPTION"`)

* `MANDATORY_AD_TEXT` (value: `"MANDATORY_AD_TEXT"`)

* `MARKETING_IMAGE` (value: `"MARKETING_IMAGE"`)

* `MEDIA_BUNDLE` (value: `"MEDIA_BUNDLE"`)

* `YOUTUBE_VIDEO` (value: `"YOUTUBE_VIDEO"`)

* `BOOK_ON_GOOGLE` (value: `"BOOK_ON_GOOGLE"`)

* `LEAD_FORM` (value: `"LEAD_FORM"`)

* `PROMOTION` (value: `"PROMOTION"`)

* `CALLOUT` (value: `"CALLOUT"`)

* `STRUCTURED_SNIPPET` (value: `"STRUCTURED_SNIPPET"`)

* `SITELINK` (value: `"SITELINK"`)

* `MOBILE_APP` (value: `"MOBILE_APP"`)

* `HOTEL_CALLOUT` (value: `"HOTEL_CALLOUT"`)

* `CALL` (value: `"CALL"`)

* `PRICE` (value: `"PRICE"`)

* `LONG_HEADLINE` (value: `"LONG_HEADLINE"`)

* `BUSINESS_NAME` (value: `"BUSINESS_NAME"`)

* `SQUARE_MARKETING_IMAGE` (value: `"SQUARE_MARKETING_IMAGE"`)

* `PORTRAIT_MARKETING_IMAGE` (value: `"PORTRAIT_MARKETING_IMAGE"`)

* `LOGO` (value: `"LOGO"`)

* `LANDSCAPE_LOGO` (value: `"LANDSCAPE_LOGO"`)

* `VIDEO` (value: `"VIDEO"`)

* `CALL_TO_ACTION_SELECTION` (value: `"CALL_TO_ACTION_SELECTION"`)

* `AD_IMAGE` (value: `"AD_IMAGE"`)

* `BUSINESS_LOGO` (value: `"BUSINESS_LOGO"`)

* `HOTEL_PROPERTY` (value: `"HOTEL_PROPERTY"`)





## Enum: StatusEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `ENABLED` (value: `"ENABLED"`)

* `REMOVED` (value: `"REMOVED"`)

* `PAUSED` (value: `"PAUSED"`)




