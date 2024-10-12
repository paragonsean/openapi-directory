# GooglePlayAndroidDeveloperApi.AutoRenewingBasePlanType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountHoldDuration** | **String** | Optional. Account hold period of the subscription, specified in ISO 8601 format. Acceptable values must be in DAYS and in the range P0D (zero days) to P30D (30 days). If not specified, the default value is P30D (30 days). | [optional] 
**billingPeriodDuration** | **String** | Required. Subscription period, specified in ISO 8601 format. For a list of acceptable billing periods, refer to the help center. | [optional] 
**gracePeriodDuration** | **String** | Grace period of the subscription, specified in ISO 8601 format. Acceptable values are P0D (zero days), P3D (3 days), P7D (7 days), P14D (14 days), and P30D (30 days). If not specified, a default value will be used based on the recurring period duration. | [optional] 
**legacyCompatible** | **Boolean** | Whether the renewing base plan is backward compatible. The backward compatible base plan is returned by the Google Play Billing Library deprecated method querySkuDetailsAsync(). Only one renewing base plan can be marked as legacy compatible for a given subscription. | [optional] 
**legacyCompatibleSubscriptionOfferId** | **String** | Subscription offer id which is legacy compatible. The backward compatible subscription offer is returned by the Google Play Billing Library deprecated method querySkuDetailsAsync(). Only one subscription offer can be marked as legacy compatible for a given renewing base plan. To have no Subscription offer as legacy compatible set this field as empty string. | [optional] 
**prorationMode** | **String** | The proration mode for the base plan determines what happens when a user switches to this plan from another base plan. If unspecified, defaults to CHARGE_ON_NEXT_BILLING_DATE. | [optional] 
**resubscribeState** | **String** | Whether users should be able to resubscribe to this base plan in Google Play surfaces. Defaults to RESUBSCRIBE_STATE_ACTIVE if not specified. | [optional] 



## Enum: ProrationModeEnum


* `UNSPECIFIED` (value: `"SUBSCRIPTION_PRORATION_MODE_UNSPECIFIED"`)

* `CHARGE_ON_NEXT_BILLING_DATE` (value: `"SUBSCRIPTION_PRORATION_MODE_CHARGE_ON_NEXT_BILLING_DATE"`)

* `CHARGE_FULL_PRICE_IMMEDIATELY` (value: `"SUBSCRIPTION_PRORATION_MODE_CHARGE_FULL_PRICE_IMMEDIATELY"`)





## Enum: ResubscribeStateEnum


* `UNSPECIFIED` (value: `"RESUBSCRIBE_STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"RESUBSCRIBE_STATE_ACTIVE"`)

* `INACTIVE` (value: `"RESUBSCRIBE_STATE_INACTIVE"`)




