# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1alphaSearchAds360Link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adsPersonalizationEnabled** | **Boolean** | Enables personalized advertising features with this integration. If this field is not set on create, it will be defaulted to true. | [optional] 
**advertiserDisplayName** | **String** | Output only. The display name of the Search Ads 360 Advertiser. Allows users to easily identify the linked resource. | [optional] [readonly] 
**advertiserId** | **String** | Immutable. This field represents the Advertiser ID of the Search Ads 360 Advertiser. that has been linked. | [optional] 
**campaignDataSharingEnabled** | **Boolean** | Immutable. Enables the import of campaign data from Search Ads 360 into the GA4 property. After link creation, this can only be updated from the Search Ads 360 product. If this field is not set on create, it will be defaulted to true. | [optional] 
**costDataSharingEnabled** | **Boolean** | Immutable. Enables the import of cost data from Search Ads 360 to the GA4 property. This can only be enabled if campaign_data_sharing_enabled is enabled. After link creation, this can only be updated from the Search Ads 360 product. If this field is not set on create, it will be defaulted to true. | [optional] 
**name** | **String** | Output only. The resource name for this SearchAds360Link resource. Format: properties/{propertyId}/searchAds360Links/{linkId} Note: linkId is not the Search Ads 360 advertiser ID | [optional] [readonly] 
**siteStatsSharingEnabled** | **Boolean** | Enables export of site stats with this integration. If this field is not set on create, it will be defaulted to true. | [optional] 


