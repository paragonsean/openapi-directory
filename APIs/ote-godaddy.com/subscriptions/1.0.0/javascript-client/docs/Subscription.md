# OpenapiJsClient.Subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addons** | [**[SubscriptionAddon]**](SubscriptionAddon.md) | An array of additional products that have been purchased to augment this Subscription | [optional] 
**billing** | [**SubscriptionBilling**](SubscriptionBilling.md) |  | 
**cancelable** | **Boolean** | Whether or not the Subscription is allowed to be canceled | [optional] 
**createdAt** | **String** | When the Subscription was created | 
**expiresAt** | **String** | When the Subscription will expire | [optional] 
**label** | **String** | A human readable description of this Subscription | [optional] 
**launchUrl** | **String** | The url to use or manage this Subscription&#39;s active product | [optional] 
**paymentProfileId** | **Number** | Unique identifier of the payment profile that will be used to automatically renew this Subscription | [optional] 
**priceLocked** | **Boolean** | Whether the renewal price will be based from the list price or a locked-in price for this shopper | 
**product** | [**SubscriptionProduct**](SubscriptionProduct.md) |  | 
**relations** | [**SubscriptionRelations**](SubscriptionRelations.md) |  | [optional] 
**renewAuto** | **Boolean** | Whether or not the Subscription is set to be automatically renewed via the billing agent | 
**renewable** | **Boolean** | Whether or not the Subscription is allowed to be renewed | 
**status** | **String** | Whether the Subscription is active or the specific non-active state | 
**subscriptionId** | **String** | Unique identifier of the Subscription | 
**upgradeable** | **Boolean** | Whether or not the Subscription is allowed to be upgraded | 



## Enum: StatusEnum


* `ACTIVE` (value: `"ACTIVE"`)

* `PENDING` (value: `"PENDING"`)

* `CANCELED` (value: `"CANCELED"`)




