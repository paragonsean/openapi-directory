

# GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal

A proposal for a link between a GA4 property and a Display & Video 360 advertiser. A proposal is converted to a DisplayVideo360AdvertiserLink once approved. Google Analytics admins approve inbound proposals while Display & Video 360 admins approve outbound proposals.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adsPersonalizationEnabled** | **Boolean** | Immutable. Enables personalized advertising features with this integration. If this field is not set on create, it will be defaulted to true. |  [optional] |
|**advertiserDisplayName** | **String** | Output only. The display name of the Display &amp; Video Advertiser. Only populated for proposals that originated from Display &amp; Video 360. |  [optional] [readonly] |
|**advertiserId** | **String** | Immutable. The Display &amp; Video 360 Advertiser&#39;s advertiser ID. |  [optional] |
|**campaignDataSharingEnabled** | **Boolean** | Immutable. Enables the import of campaign data from Display &amp; Video 360. If this field is not set on create, it will be defaulted to true. |  [optional] |
|**costDataSharingEnabled** | **Boolean** | Immutable. Enables the import of cost data from Display &amp; Video 360. This can only be enabled if campaign_data_sharing_enabled is enabled. If this field is not set on create, it will be defaulted to true. |  [optional] |
|**linkProposalStatusDetails** | [**GoogleAnalyticsAdminV1alphaLinkProposalStatusDetails**](GoogleAnalyticsAdminV1alphaLinkProposalStatusDetails.md) |  |  [optional] |
|**name** | **String** | Output only. The resource name for this DisplayVideo360AdvertiserLinkProposal resource. Format: properties/{propertyId}/displayVideo360AdvertiserLinkProposals/{proposalId} Note: proposalId is not the Display &amp; Video 360 Advertiser ID |  [optional] [readonly] |
|**validationEmail** | **String** | Input only. On a proposal being sent to Display &amp; Video 360, this field must be set to the email address of an admin on the target advertiser. This is used to verify that the Google Analytics admin is aware of at least one admin on the Display &amp; Video 360 Advertiser. This does not restrict approval of the proposal to a single user. Any admin on the Display &amp; Video 360 Advertiser may approve the proposal. |  [optional] |



