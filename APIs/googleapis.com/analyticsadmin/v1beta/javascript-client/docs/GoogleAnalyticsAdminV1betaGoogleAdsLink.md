# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1betaGoogleAdsLink

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adsPersonalizationEnabled** | **Boolean** | Enable personalized advertising features with this integration. Automatically publish my Google Analytics audience lists and Google Analytics remarketing events/parameters to the linked Google Ads account. If this field is not set on create/update, it will be defaulted to true. | [optional] 
**canManageClients** | **Boolean** | Output only. If true, this link is for a Google Ads manager account. | [optional] [readonly] 
**createTime** | **String** | Output only. Time when this link was originally created. | [optional] [readonly] 
**creatorEmailAddress** | **String** | Output only. Email address of the user that created the link. An empty string will be returned if the email address can&#39;t be retrieved. | [optional] [readonly] 
**customerId** | **String** | Immutable. Google Ads customer ID. | [optional] 
**name** | **String** | Output only. Format: properties/{propertyId}/googleAdsLinks/{googleAdsLinkId} Note: googleAdsLinkId is not the Google Ads customer ID. | [optional] [readonly] 
**updateTime** | **String** | Output only. Time when this link was last updated. | [optional] [readonly] 


