

# APIPlanSubscriptionOut

The API Plan governing the subscription.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiKey** | **String** | User API Key. |  [optional] |
|**currency** | **String** | Current plan Currency for prices. |  [optional] |
|**currencyFactor** | **Double** | For USD, GBP, EUR - the factor is 1. |  [optional] |
|**planBaseFeesKey** | **String** | Current plan key (as in Stripe product). |  [optional] |
|**planEnded** | **Long** | Datetime when the user ended the plan. |  [optional] |
|**planName** | **String** | Current plan name. |  [optional] |
|**planQuota** | **Long** | Current plan quota in quantity of units (NB: some API use several units per name). |  [optional] |
|**planStarted** | **Long** | Datetime when the user subscribed to the current plan. |  [optional] |
|**planStatus** | **String** | Plan status. |  [optional] |
|**price** | **Double** | Current plan price for overages expressed in Currency (extra price per unit above the free quota). |  [optional] |
|**priceOverage** | **Double** | Current plan price for overages expressed in Currency (extra price per unit above the free quota). |  [optional] |
|**priceOverageUSD** | **Double** | Current plan price for overages expressed in USD (extra price per unit above the free quota). |  [optional] |
|**priceUSD** | **Double** | Current plan monthly price expressed in USD (includes a free quota). |  [optional] |
|**priorPlanStarted** | **Long** | Datetime when the user subscribed to the prior plan. |  [optional] |
|**stripeCustomerId** | **String** | Stripe customer identifier. |  [optional] |
|**stripeStatus** | **String** | Stripe status ex active. |  [optional] |
|**stripeSubscription** | **String** | Stripe subscription identifier. |  [optional] |
|**taxRate** | **Double** | Applicable tax rate for the plan. |  [optional] |
|**userId** | **String** | Internal user identifier. |  [optional] |



