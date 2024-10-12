

# GoogleAdsSearchads360V0ResourcesAssetGroupAsset

AssetGroupAsset is the link between an asset and an asset group. Adding an AssetGroupAsset links an asset with an asset group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**asset** | **String** | Immutable. The asset which this asset group asset is linking. |  [optional] |
|**assetGroup** | **String** | Immutable. The asset group which this asset group asset is linking. |  [optional] |
|**fieldType** | [**FieldTypeEnum**](#FieldTypeEnum) | The description of the placement of the asset within the asset group. For example: HEADLINE, YOUTUBE_VIDEO etc |  [optional] |
|**resourceName** | **String** | Immutable. The resource name of the asset group asset. Asset group asset resource name have the form: &#x60;customers/{customer_id}/assetGroupAssets/{asset_group_id}~{asset_id}~{field_type}&#x60; |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the link between an asset and asset group. |  [optional] |



## Enum: FieldTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| HEADLINE | &quot;HEADLINE&quot; |
| DESCRIPTION | &quot;DESCRIPTION&quot; |
| MANDATORY_AD_TEXT | &quot;MANDATORY_AD_TEXT&quot; |
| MARKETING_IMAGE | &quot;MARKETING_IMAGE&quot; |
| MEDIA_BUNDLE | &quot;MEDIA_BUNDLE&quot; |
| YOUTUBE_VIDEO | &quot;YOUTUBE_VIDEO&quot; |
| BOOK_ON_GOOGLE | &quot;BOOK_ON_GOOGLE&quot; |
| LEAD_FORM | &quot;LEAD_FORM&quot; |
| PROMOTION | &quot;PROMOTION&quot; |
| CALLOUT | &quot;CALLOUT&quot; |
| STRUCTURED_SNIPPET | &quot;STRUCTURED_SNIPPET&quot; |
| SITELINK | &quot;SITELINK&quot; |
| MOBILE_APP | &quot;MOBILE_APP&quot; |
| HOTEL_CALLOUT | &quot;HOTEL_CALLOUT&quot; |
| CALL | &quot;CALL&quot; |
| PRICE | &quot;PRICE&quot; |
| LONG_HEADLINE | &quot;LONG_HEADLINE&quot; |
| BUSINESS_NAME | &quot;BUSINESS_NAME&quot; |
| SQUARE_MARKETING_IMAGE | &quot;SQUARE_MARKETING_IMAGE&quot; |
| PORTRAIT_MARKETING_IMAGE | &quot;PORTRAIT_MARKETING_IMAGE&quot; |
| LOGO | &quot;LOGO&quot; |
| LANDSCAPE_LOGO | &quot;LANDSCAPE_LOGO&quot; |
| VIDEO | &quot;VIDEO&quot; |
| CALL_TO_ACTION_SELECTION | &quot;CALL_TO_ACTION_SELECTION&quot; |
| AD_IMAGE | &quot;AD_IMAGE&quot; |
| BUSINESS_LOGO | &quot;BUSINESS_LOGO&quot; |
| HOTEL_PROPERTY | &quot;HOTEL_PROPERTY&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ENABLED | &quot;ENABLED&quot; |
| REMOVED | &quot;REMOVED&quot; |
| PAUSED | &quot;PAUSED&quot; |



