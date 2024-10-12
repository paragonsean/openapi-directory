# CampaignManager360Api.AdBlockingConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clickThroughUrl** | **String** | Click-through URL used by brand-neutral ads. This is a required field when overrideClickThroughUrl is set to true. | [optional] 
**creativeBundleId** | **String** | ID of a creative bundle to use for this campaign. If set, brand-neutral ads will select creatives from this bundle. Otherwise, a default transparent pixel will be used. | [optional] 
**enabled** | **Boolean** | Whether this campaign has enabled ad blocking. When true, ad blocking is enabled for placements in the campaign, but this may be overridden by site and placement settings. When false, ad blocking is disabled for all placements under the campaign, regardless of site and placement settings. | [optional] 
**overrideClickThroughUrl** | **Boolean** | Whether the brand-neutral ad&#39;s click-through URL comes from the campaign&#39;s creative bundle or the override URL. Must be set to true if ad blocking is enabled and no creative bundle is configured. | [optional] 


