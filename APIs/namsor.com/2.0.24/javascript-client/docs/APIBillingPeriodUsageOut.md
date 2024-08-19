# NamSorApiV2.APIBillingPeriodUsageOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiKey** | **String** | User API Key. | [optional] 
**billingStatus** | **String** | Current period billing status ex OPEN. | [optional] 
**hardLimit** | **Number** | Current period hard limit (reaching the limit sends an email notification and blocks the API Key). | [optional] 
**periodEnded** | **Number** | Datetime when the the plan&#39;s current period endend. | [optional] 
**periodStarted** | **Number** | Datetime when the the plan&#39;s current period started. | [optional] 
**softLimit** | **Number** | Current period soft limit (reaching the limit sends an email notification). | [optional] 
**stripeCurrentPeriodEnd** | **Number** | Datetime when the the plan&#39;s current period endend (in Stripe). Internal and Stripe periodicity should ~coincide. | [optional] 
**stripeCurrentPeriodStart** | **Number** | Datetime when the the plan&#39;s current period started (in Stripe). Internal and Stripe periodicity should ~coincide. | [optional] 
**subscriptionStarted** | **Number** | Datetime when the user subscribed to the plan. | [optional] 
**usage** | **Number** | Current period usage in units (NB some API endpoints use more than one unit). | [optional] 


