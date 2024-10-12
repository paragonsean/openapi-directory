

# Ad

Contains properties of a Campaign Manager ad.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Account ID of this ad. This is a read-only field that can be left blank. |  [optional] |
|**active** | **Boolean** | Whether this ad is active. When true, archived must be false. |  [optional] |
|**advertiserId** | **String** | Advertiser ID of this ad. This is a required field on insertion. |  [optional] |
|**advertiserIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**archived** | **Boolean** | Whether this ad is archived. When true, active must be false. |  [optional] |
|**audienceSegmentId** | **String** | Audience segment ID that is being targeted for this ad. Applicable when type is AD_SERVING_STANDARD_AD. |  [optional] |
|**campaignId** | **String** | Campaign ID of this ad. This is a required field on insertion. |  [optional] |
|**campaignIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**clickThroughUrl** | [**ClickThroughUrl**](ClickThroughUrl.md) |  |  [optional] |
|**clickThroughUrlSuffixProperties** | [**ClickThroughUrlSuffixProperties**](ClickThroughUrlSuffixProperties.md) |  |  [optional] |
|**comments** | **String** | Comments for this ad. |  [optional] |
|**compatibility** | [**CompatibilityEnum**](#CompatibilityEnum) | Compatibility of this ad. Applicable when type is AD_SERVING_DEFAULT_AD. DISPLAY and DISPLAY_INTERSTITIAL refer to either rendering on desktop or on mobile devices or in mobile apps for regular or interstitial ads, respectively. APP and APP_INTERSTITIAL are only used for existing default ads. New mobile placements must be assigned DISPLAY or DISPLAY_INTERSTITIAL and default ads created for those placements will be limited to those compatibility types. IN_STREAM_VIDEO refers to rendering in-stream video ads developed with the VAST standard. |  [optional] |
|**createInfo** | [**LastModifiedInfo**](LastModifiedInfo.md) |  |  [optional] |
|**creativeGroupAssignments** | [**List&lt;CreativeGroupAssignment&gt;**](CreativeGroupAssignment.md) | Creative group assignments for this ad. Applicable when type is AD_SERVING_CLICK_TRACKER. Only one assignment per creative group number is allowed for a maximum of two assignments. |  [optional] |
|**creativeRotation** | [**CreativeRotation**](CreativeRotation.md) |  |  [optional] |
|**dayPartTargeting** | [**DayPartTargeting**](DayPartTargeting.md) |  |  [optional] |
|**defaultClickThroughEventTagProperties** | [**DefaultClickThroughEventTagProperties**](DefaultClickThroughEventTagProperties.md) |  |  [optional] |
|**deliverySchedule** | [**DeliverySchedule**](DeliverySchedule.md) |  |  [optional] |
|**dynamicClickTracker** | **Boolean** | Whether this ad is a dynamic click tracker. Applicable when type is AD_SERVING_CLICK_TRACKER. This is a required field on insert, and is read-only after insert. |  [optional] |
|**endTime** | **OffsetDateTime** |  |  [optional] |
|**eventTagOverrides** | [**List&lt;EventTagOverride&gt;**](EventTagOverride.md) | Event tag overrides for this ad. |  [optional] |
|**geoTargeting** | [**GeoTargeting**](GeoTargeting.md) |  |  [optional] |
|**id** | **String** | ID of this ad. This is a read-only, auto-generated field. |  [optional] |
|**idDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**keyValueTargetingExpression** | [**KeyValueTargetingExpression**](KeyValueTargetingExpression.md) |  |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#ad\&quot;. |  [optional] |
|**languageTargeting** | [**LanguageTargeting**](LanguageTargeting.md) |  |  [optional] |
|**lastModifiedInfo** | [**LastModifiedInfo**](LastModifiedInfo.md) |  |  [optional] |
|**name** | **String** | Name of this ad. This is a required field and must be less than 256 characters long. |  [optional] |
|**placementAssignments** | [**List&lt;PlacementAssignment&gt;**](PlacementAssignment.md) | Placement assignments for this ad. |  [optional] |
|**remarketingListExpression** | [**ListTargetingExpression**](ListTargetingExpression.md) |  |  [optional] |
|**size** | [**Size**](Size.md) |  |  [optional] |
|**sslCompliant** | **Boolean** | Whether this ad is ssl compliant. This is a read-only field that is auto-generated when the ad is inserted or updated. |  [optional] |
|**sslRequired** | **Boolean** | Whether this ad requires ssl. This is a read-only field that is auto-generated when the ad is inserted or updated. |  [optional] |
|**startTime** | **OffsetDateTime** |  |  [optional] |
|**subaccountId** | **String** | Subaccount ID of this ad. This is a read-only field that can be left blank. |  [optional] |
|**targetingTemplateId** | **String** | Targeting template ID, used to apply preconfigured targeting information to this ad. This cannot be set while any of dayPartTargeting, geoTargeting, keyValueTargetingExpression, languageTargeting, remarketingListExpression, or technologyTargeting are set. Applicable when type is AD_SERVING_STANDARD_AD. |  [optional] |
|**technologyTargeting** | [**TechnologyTargeting**](TechnologyTargeting.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of ad. This is a required field on insertion. Note that default ads ( AD_SERVING_DEFAULT_AD) cannot be created directly (see Creative resource). |  [optional] |



## Enum: CompatibilityEnum

| Name | Value |
|---- | -----|
| DISPLAY | &quot;DISPLAY&quot; |
| DISPLAY_INTERSTITIAL | &quot;DISPLAY_INTERSTITIAL&quot; |
| APP | &quot;APP&quot; |
| APP_INTERSTITIAL | &quot;APP_INTERSTITIAL&quot; |
| IN_STREAM_VIDEO | &quot;IN_STREAM_VIDEO&quot; |
| IN_STREAM_AUDIO | &quot;IN_STREAM_AUDIO&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| STANDARD_AD | &quot;AD_SERVING_STANDARD_AD&quot; |
| DEFAULT_AD | &quot;AD_SERVING_DEFAULT_AD&quot; |
| CLICK_TRACKER | &quot;AD_SERVING_CLICK_TRACKER&quot; |
| TRACKING | &quot;AD_SERVING_TRACKING&quot; |
| BRAND_SAFE_AD | &quot;AD_SERVING_BRAND_SAFE_AD&quot; |



