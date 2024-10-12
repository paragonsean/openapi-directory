# CampaignManager360Api.SiteSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeViewOptOut** | **Boolean** | Whether active view creatives are disabled for this site. | [optional] 
**adBlockingOptOut** | **Boolean** | Whether this site opts out of ad blocking. When true, ad blocking is disabled for all placements under the site, regardless of the individual placement settings. When false, the campaign and placement settings take effect. | [optional] 
**disableNewCookie** | **Boolean** | Whether new cookies are disabled for this site. | [optional] 
**tagSetting** | [**TagSetting**](TagSetting.md) |  | [optional] 
**videoActiveViewOptOutTemplate** | **Boolean** | Whether Verification and ActiveView for in-stream video creatives are disabled by default for new placements created under this site. This value will be used to populate the placement.videoActiveViewOptOut field, when no value is specified for the new placement. | [optional] 
**vpaidAdapterChoiceTemplate** | **String** | Default VPAID adapter setting for new placements created under this site. This value will be used to populate the placements.vpaidAdapterChoice field, when no value is specified for the new placement. Controls which VPAID format the measurement adapter will use for in-stream video creatives assigned to the placement. The publisher&#39;s specifications will typically determine this setting. For VPAID creatives, the adapter format will match the VPAID format (HTML5 VPAID creatives use the HTML5 adapter). *Note:* Flash is no longer supported. This field now defaults to HTML5 when the following values are provided: FLASH, BOTH. | [optional] 



## Enum: VpaidAdapterChoiceTemplateEnum


* `DEFAULT` (value: `"DEFAULT"`)

* `FLASH` (value: `"FLASH"`)

* `HTML5` (value: `"HTML5"`)

* `BOTH` (value: `"BOTH"`)




