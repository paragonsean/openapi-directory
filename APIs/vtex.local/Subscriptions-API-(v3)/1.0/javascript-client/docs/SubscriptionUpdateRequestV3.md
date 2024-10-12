# SubscriptionsApiV3.SubscriptionUpdateRequestV3

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isSkipped** | **Boolean** | When set as &#x60;true&#x60;, it means the shopper asked to skip the next subscription order, and when set as &#x60;false&#x60;, no subscription order is going to be skipped. | [optional] 
**plan** | [**PlanThinRequest**](PlanThinRequest.md) |  | [optional] 
**purchaseSettings** | [**PurchaseSettingsThinRequest**](PurchaseSettingsThinRequest.md) |  | [optional] 
**shippingAddress** | [**ShippingAddress**](ShippingAddress.md) |  | [optional] 
**status** | **String** | Status to which you wish to update the subscription. The accepted values are:   - &#x60;ACTIVE&#x60;   - &#x60;PAUSED&#x60;   - &#x60;CANCELLED&#x60;   - &#x60;EXPIRED&#x60;   - &#x60;MISSING&#x60; | [optional] 
**title** | **String** | Name of the subscription. | [optional] 


