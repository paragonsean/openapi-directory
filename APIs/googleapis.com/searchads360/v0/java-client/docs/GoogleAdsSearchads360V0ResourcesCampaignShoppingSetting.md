

# GoogleAdsSearchads360V0ResourcesCampaignShoppingSetting

The setting for Shopping campaigns. Defines the universe of products that can be advertised by the campaign, and how this campaign interacts with other Shopping campaigns.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**campaignPriority** | **Integer** | Priority of the campaign. Campaigns with numerically higher priorities take precedence over those with lower priorities. This field is required for Shopping campaigns, with values between 0 and 2, inclusive. This field is optional for Smart Shopping campaigns, but must be equal to 3 if set. |  [optional] |
|**enableLocal** | **Boolean** | Whether to include local products. |  [optional] |
|**feedLabel** | **String** | Feed label of products to include in the campaign. Only one of feed_label or sales_country can be set. If used instead of sales_country, the feed_label field accepts country codes in the same format for example: &#39;XX&#39;. Otherwise can be any string used for feed label in Google Merchant Center. |  [optional] |
|**merchantId** | **String** | Immutable. ID of the Merchant Center account. This field is required for create operations. This field is immutable for Shopping campaigns. |  [optional] |
|**salesCountry** | **String** | Sales country of products to include in the campaign.  |  [optional] |
|**useVehicleInventory** | **Boolean** | Immutable. Whether to target Vehicle Listing inventory. |  [optional] |



