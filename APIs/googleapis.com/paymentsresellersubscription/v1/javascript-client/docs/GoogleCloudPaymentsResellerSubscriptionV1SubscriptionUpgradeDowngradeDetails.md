# PaymentsResellerSubscriptionApi.GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingCycleSpec** | **String** | Required. Specifies the billing cycle spec for the new upgraded/downgraded subscription. | [optional] 
**previousSubscriptionId** | **String** | Required. The previous subscription id to be replaced. This is not the full resource name, use the subscription_id segment only. | [optional] 



## Enum: BillingCycleSpecEnum


* `UNSPECIFIED` (value: `"BILLING_CYCLE_SPEC_UNSPECIFIED"`)

* `ALIGN_WITH_PREVIOUS_SUBSCRIPTION` (value: `"BILLING_CYCLE_SPEC_ALIGN_WITH_PREVIOUS_SUBSCRIPTION"`)

* `START_IMMEDIATELY` (value: `"BILLING_CYCLE_SPEC_START_IMMEDIATELY"`)




