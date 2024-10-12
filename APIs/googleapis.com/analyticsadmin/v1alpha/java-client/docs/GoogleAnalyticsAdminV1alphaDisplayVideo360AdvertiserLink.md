

# GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink

A link between a GA4 property and a Display & Video 360 advertiser.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adsPersonalizationEnabled** | **Boolean** | Enables personalized advertising features with this integration. If this field is not set on create/update, it will be defaulted to true. |  [optional] |
|**advertiserDisplayName** | **String** | Output only. The display name of the Display &amp; Video 360 Advertiser. |  [optional] [readonly] |
|**advertiserId** | **String** | Immutable. The Display &amp; Video 360 Advertiser&#39;s advertiser ID. |  [optional] |
|**campaignDataSharingEnabled** | **Boolean** | Immutable. Enables the import of campaign data from Display &amp; Video 360 into the GA4 property. After link creation, this can only be updated from the Display &amp; Video 360 product. If this field is not set on create, it will be defaulted to true. |  [optional] |
|**costDataSharingEnabled** | **Boolean** | Immutable. Enables the import of cost data from Display &amp; Video 360 into the GA4 property. This can only be enabled if campaign_data_sharing_enabled is enabled. After link creation, this can only be updated from the Display &amp; Video 360 product. If this field is not set on create, it will be defaulted to true. |  [optional] |
|**name** | **String** | Output only. The resource name for this DisplayVideo360AdvertiserLink resource. Format: properties/{propertyId}/displayVideo360AdvertiserLinks/{linkId} Note: linkId is not the Display &amp; Video 360 Advertiser ID |  [optional] [readonly] |



