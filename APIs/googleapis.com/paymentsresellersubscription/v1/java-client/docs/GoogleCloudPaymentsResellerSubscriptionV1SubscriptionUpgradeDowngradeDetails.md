

# GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetails

Details about the previous subscription that this new subscription upgrades/downgrades from.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingCycleSpec** | [**BillingCycleSpecEnum**](#BillingCycleSpecEnum) | Required. Specifies the billing cycle spec for the new upgraded/downgraded subscription. |  [optional] |
|**previousSubscriptionId** | **String** | Required. The previous subscription id to be replaced. This is not the full resource name, use the subscription_id segment only. |  [optional] |



## Enum: BillingCycleSpecEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;BILLING_CYCLE_SPEC_UNSPECIFIED&quot; |
| ALIGN_WITH_PREVIOUS_SUBSCRIPTION | &quot;BILLING_CYCLE_SPEC_ALIGN_WITH_PREVIOUS_SUBSCRIPTION&quot; |
| START_IMMEDIATELY | &quot;BILLING_CYCLE_SPEC_START_IMMEDIATELY&quot; |



