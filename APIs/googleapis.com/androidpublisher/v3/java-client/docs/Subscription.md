

# Subscription

A single subscription for an app.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**archived** | **Boolean** | Output only. Deprecated: subscription archiving is not supported. |  [optional] [readonly] |
|**basePlans** | [**List&lt;BasePlan&gt;**](BasePlan.md) | The set of base plans for this subscription. Represents the prices and duration of the subscription if no other offers apply. |  [optional] |
|**listings** | [**List&lt;SubscriptionListing&gt;**](SubscriptionListing.md) | Required. List of localized listings for this subscription. Must contain at least an entry for the default language of the parent app. |  [optional] |
|**packageName** | **String** | Immutable. Package name of the parent app. |  [optional] |
|**productId** | **String** | Immutable. Unique product ID of the product. Unique within the parent app. Product IDs must be composed of lower-case letters (a-z), numbers (0-9), underscores (_) and dots (.). It must start with a lower-case letter or number, and be between 1 and 40 (inclusive) characters in length. |  [optional] |
|**taxAndComplianceSettings** | [**SubscriptionTaxAndComplianceSettings**](SubscriptionTaxAndComplianceSettings.md) |  |  [optional] |



