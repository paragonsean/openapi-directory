

# SubscriptionPlan

The `plan` property is required. In this version of the API, the G Suite plans are the flexible plan, annual commitment plan, and the 30-day free trial plan. For more information about the API\"s payment plans, see the API concepts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commitmentInterval** | [**SubscriptionPlanCommitmentInterval**](SubscriptionPlanCommitmentInterval.md) |  |  [optional] |
|**isCommitmentPlan** | **Boolean** | The &#x60;isCommitmentPlan&#x60; property&#39;s boolean value identifies the plan as an annual commitment plan: - &#x60;true&#x60; — The subscription&#39;s plan is an annual commitment plan. - &#x60;false&#x60; — The plan is not an annual commitment plan.  |  [optional] |
|**planName** | **String** | The &#x60;planName&#x60; property is required. This is the name of the subscription&#39;s plan. For more information about the Google payment plans, see the API concepts. Possible values are: - &#x60;ANNUAL_MONTHLY_PAY&#x60; — The annual commitment plan with monthly payments. *Caution: *&#x60;ANNUAL_MONTHLY_PAY&#x60; is returned as &#x60;ANNUAL&#x60; in all API responses. - &#x60;ANNUAL_YEARLY_PAY&#x60; — The annual commitment plan with yearly payments - &#x60;FLEXIBLE&#x60; — The flexible plan - &#x60;TRIAL&#x60; — The 30-day free trial plan. A subscription in trial will be suspended after the 30th free day if no payment plan is assigned. Calling &#x60;changePlan&#x60; will assign a payment plan to a trial but will not activate the plan. A trial will automatically begin its assigned payment plan after its 30th free day or immediately after calling &#x60;startPaidService&#x60;. - &#x60;FREE&#x60; — The free plan is exclusive to the Cloud Identity SKU and does not incur any billing.  |  [optional] |



