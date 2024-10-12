

# GoogleCloudChannelV1CustomerRepricingConfig

Configuration for how a reseller will reprice a Customer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Output only. Resource name of the CustomerRepricingConfig. Format: accounts/{account_id}/customers/{customer_id}/customerRepricingConfigs/{id}. |  [optional] [readonly] |
|**repricingConfig** | [**GoogleCloudChannelV1RepricingConfig**](GoogleCloudChannelV1RepricingConfig.md) |  |  [optional] |
|**updateTime** | **String** | Output only. Timestamp of an update to the repricing rule. If &#x60;update_time&#x60; is after RepricingConfig.effective_invoice_month then it indicates this was set mid-month. |  [optional] [readonly] |



