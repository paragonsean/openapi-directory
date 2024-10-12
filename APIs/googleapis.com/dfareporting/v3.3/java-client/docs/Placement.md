

# Placement

Contains properties of a placement.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Account ID of this placement. This field can be left blank. |  [optional] |
|**adBlockingOptOut** | **Boolean** | Whether this placement opts out of ad blocking. When true, ad blocking is disabled for this placement. When false, the campaign and site settings take effect. |  [optional] |
|**additionalSizes** | [**List&lt;Size&gt;**](Size.md) | Additional sizes associated with this placement. When inserting or updating a placement, only the size ID field is used. |  [optional] |
|**advertiserId** | **String** | Advertiser ID of this placement. This field can be left blank. |  [optional] |
|**advertiserIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**archived** | **Boolean** | Whether this placement is archived. |  [optional] |
|**campaignId** | **String** | Campaign ID of this placement. This field is a required field on insertion. |  [optional] |
|**campaignIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**comment** | **String** | Comments for this placement. |  [optional] |
|**compatibility** | [**CompatibilityEnum**](#CompatibilityEnum) | Placement compatibility. DISPLAY and DISPLAY_INTERSTITIAL refer to rendering on desktop, on mobile devices or in mobile apps for regular or interstitial ads respectively. APP and APP_INTERSTITIAL are no longer allowed for new placement insertions. Instead, use DISPLAY or DISPLAY_INTERSTITIAL. IN_STREAM_VIDEO refers to rendering in in-stream video ads developed with the VAST standard. This field is required on insertion. |  [optional] |
|**contentCategoryId** | **String** | ID of the content category assigned to this placement. |  [optional] |
|**createInfo** | [**LastModifiedInfo**](LastModifiedInfo.md) |  |  [optional] |
|**directorySiteId** | **String** | Directory site ID of this placement. On insert, you must set either this field or the siteId field to specify the site associated with this placement. This is a required field that is read-only after insertion. |  [optional] |
|**directorySiteIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**externalId** | **String** | External ID for this placement. |  [optional] |
|**id** | **String** | ID of this placement. This is a read-only, auto-generated field. |  [optional] |
|**idDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**keyName** | **String** | Key name of this placement. This is a read-only, auto-generated field. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#placement\&quot;. |  [optional] |
|**lastModifiedInfo** | [**LastModifiedInfo**](LastModifiedInfo.md) |  |  [optional] |
|**lookbackConfiguration** | [**LookbackConfiguration**](LookbackConfiguration.md) |  |  [optional] |
|**name** | **String** | Name of this placement.This is a required field and must be less than or equal to 256 characters long. |  [optional] |
|**paymentApproved** | **Boolean** | Whether payment was approved for this placement. This is a read-only field relevant only to publisher-paid placements. |  [optional] |
|**paymentSource** | [**PaymentSourceEnum**](#PaymentSourceEnum) | Payment source for this placement. This is a required field that is read-only after insertion. |  [optional] |
|**placementGroupId** | **String** | ID of this placement&#39;s group, if applicable. |  [optional] |
|**placementGroupIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**placementStrategyId** | **String** | ID of the placement strategy assigned to this placement. |  [optional] |
|**pricingSchedule** | [**PricingSchedule**](PricingSchedule.md) |  |  [optional] |
|**primary** | **Boolean** | Whether this placement is the primary placement of a roadblock (placement group). You cannot change this field from true to false. Setting this field to true will automatically set the primary field on the original primary placement of the roadblock to false, and it will automatically set the roadblock&#39;s primaryPlacementId field to the ID of this placement. |  [optional] |
|**publisherUpdateInfo** | [**LastModifiedInfo**](LastModifiedInfo.md) |  |  [optional] |
|**siteId** | **String** | Site ID associated with this placement. On insert, you must set either this field or the directorySiteId field to specify the site associated with this placement. This is a required field that is read-only after insertion. |  [optional] |
|**siteIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**size** | [**Size**](Size.md) |  |  [optional] |
|**sslRequired** | **Boolean** | Whether creatives assigned to this placement must be SSL-compliant. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Third-party placement status. |  [optional] |
|**subaccountId** | **String** | Subaccount ID of this placement. This field can be left blank. |  [optional] |
|**tagFormats** | [**List&lt;TagFormatsEnum&gt;**](#List&lt;TagFormatsEnum&gt;) | Tag formats to generate for this placement. This field is required on insertion. Acceptable values are: - \&quot;PLACEMENT_TAG_STANDARD\&quot; - \&quot;PLACEMENT_TAG_IFRAME_JAVASCRIPT\&quot; - \&quot;PLACEMENT_TAG_IFRAME_ILAYER\&quot; - \&quot;PLACEMENT_TAG_INTERNAL_REDIRECT\&quot; - \&quot;PLACEMENT_TAG_JAVASCRIPT\&quot; - \&quot;PLACEMENT_TAG_INTERSTITIAL_IFRAME_JAVASCRIPT\&quot; - \&quot;PLACEMENT_TAG_INTERSTITIAL_INTERNAL_REDIRECT\&quot; - \&quot;PLACEMENT_TAG_INTERSTITIAL_JAVASCRIPT\&quot; - \&quot;PLACEMENT_TAG_CLICK_COMMANDS\&quot; - \&quot;PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH\&quot; - \&quot;PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH_VAST_3\&quot; - \&quot;PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH_VAST_4\&quot; - \&quot;PLACEMENT_TAG_TRACKING\&quot; - \&quot;PLACEMENT_TAG_TRACKING_IFRAME\&quot; - \&quot;PLACEMENT_TAG_TRACKING_JAVASCRIPT\&quot;  |  [optional] |
|**tagSetting** | [**TagSetting**](TagSetting.md) |  |  [optional] |
|**videoActiveViewOptOut** | **Boolean** | Whether Verification and ActiveView are disabled for in-stream video creatives for this placement. The same setting videoActiveViewOptOut exists on the site level -- the opt out occurs if either of these settings are true. These settings are distinct from DirectorySites.settings.activeViewOptOut or Sites.siteSettings.activeViewOptOut which only apply to display ads. However, Accounts.activeViewOptOut opts out both video traffic, as well as display ads, from Verification and ActiveView. |  [optional] |
|**videoSettings** | [**VideoSettings**](VideoSettings.md) |  |  [optional] |
|**vpaidAdapterChoice** | [**VpaidAdapterChoiceEnum**](#VpaidAdapterChoiceEnum) | VPAID adapter setting for this placement. Controls which VPAID format the measurement adapter will use for in-stream video creatives assigned to this placement. *Note:* Flash is no longer supported. This field now defaults to HTML5 when the following values are provided: FLASH, BOTH. |  [optional] |



## Enum: CompatibilityEnum

| Name | Value |
|---- | -----|
| DISPLAY | &quot;DISPLAY&quot; |
| DISPLAY_INTERSTITIAL | &quot;DISPLAY_INTERSTITIAL&quot; |
| APP | &quot;APP&quot; |
| APP_INTERSTITIAL | &quot;APP_INTERSTITIAL&quot; |
| IN_STREAM_VIDEO | &quot;IN_STREAM_VIDEO&quot; |
| IN_STREAM_AUDIO | &quot;IN_STREAM_AUDIO&quot; |



## Enum: PaymentSourceEnum

| Name | Value |
|---- | -----|
| AGENCY_PAID | &quot;PLACEMENT_AGENCY_PAID&quot; |
| PUBLISHER_PAID | &quot;PLACEMENT_PUBLISHER_PAID&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING_REVIEW | &quot;PENDING_REVIEW&quot; |
| PAYMENT_ACCEPTED | &quot;PAYMENT_ACCEPTED&quot; |
| PAYMENT_REJECTED | &quot;PAYMENT_REJECTED&quot; |
| ACKNOWLEDGE_REJECTION | &quot;ACKNOWLEDGE_REJECTION&quot; |
| ACKNOWLEDGE_ACCEPTANCE | &quot;ACKNOWLEDGE_ACCEPTANCE&quot; |
| DRAFT | &quot;DRAFT&quot; |



## Enum: List&lt;TagFormatsEnum&gt;

| Name | Value |
|---- | -----|
| STANDARD | &quot;PLACEMENT_TAG_STANDARD&quot; |
| IFRAME_JAVASCRIPT | &quot;PLACEMENT_TAG_IFRAME_JAVASCRIPT&quot; |
| IFRAME_ILAYER | &quot;PLACEMENT_TAG_IFRAME_ILAYER&quot; |
| INTERNAL_REDIRECT | &quot;PLACEMENT_TAG_INTERNAL_REDIRECT&quot; |
| JAVASCRIPT | &quot;PLACEMENT_TAG_JAVASCRIPT&quot; |
| INTERSTITIAL_IFRAME_JAVASCRIPT | &quot;PLACEMENT_TAG_INTERSTITIAL_IFRAME_JAVASCRIPT&quot; |
| INTERSTITIAL_INTERNAL_REDIRECT | &quot;PLACEMENT_TAG_INTERSTITIAL_INTERNAL_REDIRECT&quot; |
| INTERSTITIAL_JAVASCRIPT | &quot;PLACEMENT_TAG_INTERSTITIAL_JAVASCRIPT&quot; |
| CLICK_COMMANDS | &quot;PLACEMENT_TAG_CLICK_COMMANDS&quot; |
| INSTREAM_VIDEO_PREFETCH | &quot;PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH&quot; |
| TRACKING | &quot;PLACEMENT_TAG_TRACKING&quot; |
| TRACKING_IFRAME | &quot;PLACEMENT_TAG_TRACKING_IFRAME&quot; |
| TRACKING_JAVASCRIPT | &quot;PLACEMENT_TAG_TRACKING_JAVASCRIPT&quot; |
| INSTREAM_VIDEO_PREFETCH_VAST_3 | &quot;PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH_VAST_3&quot; |
| IFRAME_JAVASCRIPT_LEGACY | &quot;PLACEMENT_TAG_IFRAME_JAVASCRIPT_LEGACY&quot; |
| JAVASCRIPT_LEGACY | &quot;PLACEMENT_TAG_JAVASCRIPT_LEGACY&quot; |
| INTERSTITIAL_IFRAME_JAVASCRIPT_LEGACY | &quot;PLACEMENT_TAG_INTERSTITIAL_IFRAME_JAVASCRIPT_LEGACY&quot; |
| INTERSTITIAL_JAVASCRIPT_LEGACY | &quot;PLACEMENT_TAG_INTERSTITIAL_JAVASCRIPT_LEGACY&quot; |
| INSTREAM_VIDEO_PREFETCH_VAST_4 | &quot;PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH_VAST_4&quot; |
| TRACKING_THIRD_PARTY_MEASUREMENT | &quot;PLACEMENT_TAG_TRACKING_THIRD_PARTY_MEASUREMENT&quot; |



## Enum: VpaidAdapterChoiceEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;DEFAULT&quot; |
| FLASH | &quot;FLASH&quot; |
| HTML5 | &quot;HTML5&quot; |
| BOTH | &quot;BOTH&quot; |



