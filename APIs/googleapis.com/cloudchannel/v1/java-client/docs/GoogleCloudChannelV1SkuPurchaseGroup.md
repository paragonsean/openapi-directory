

# GoogleCloudChannelV1SkuPurchaseGroup

Represents a set of SKUs that must be purchased using the same billing account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAccountPurchaseInfos** | [**List&lt;GoogleCloudChannelV1BillingAccountPurchaseInfo&gt;**](GoogleCloudChannelV1BillingAccountPurchaseInfo.md) | List of billing accounts that are eligible to purhcase these SKUs. |  [optional] |
|**skus** | **List&lt;String&gt;** | Resource names of the SKUs included in this group. Format: products/{product_id}/skus/{sku_id}. |  [optional] |



