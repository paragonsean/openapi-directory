

# GoogleCloudChannelV1ChannelPartnerRepricingConfig

Configuration for how a distributor will rebill a channel partner (also known as a distributor-authorized reseller).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Output only. Resource name of the ChannelPartnerRepricingConfig. Format: accounts/{account_id}/channelPartnerLinks/{channel_partner_id}/channelPartnerRepricingConfigs/{id}. |  [optional] [readonly] |
|**repricingConfig** | [**GoogleCloudChannelV1RepricingConfig**](GoogleCloudChannelV1RepricingConfig.md) |  |  [optional] |
|**updateTime** | **String** | Output only. Timestamp of an update to the repricing rule. If &#x60;update_time&#x60; is after RepricingConfig.effective_invoice_month then it indicates this was set mid-month. |  [optional] [readonly] |



