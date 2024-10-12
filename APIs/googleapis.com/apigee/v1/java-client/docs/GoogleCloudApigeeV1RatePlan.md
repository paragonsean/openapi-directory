

# GoogleCloudApigeeV1RatePlan

Rate plan details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiproduct** | **String** | Name of the API product that the rate plan is associated with. |  [optional] |
|**billingPeriod** | [**BillingPeriodEnum**](#BillingPeriodEnum) | Frequency at which the customer will be billed. |  [optional] |
|**consumptionPricingRates** | [**List&lt;GoogleCloudApigeeV1RateRange&gt;**](GoogleCloudApigeeV1RateRange.md) | API call volume ranges and the fees charged when the total number of API calls is within a given range. The method used to calculate the final fee depends on the selected pricing model. For example, if the pricing model is &#x60;STAIRSTEP&#x60; and the ranges are defined as follows: &#x60;&#x60;&#x60; { \&quot;start\&quot;: 1, \&quot;end\&quot;: 100, \&quot;fee\&quot;: 75 }, { \&quot;start\&quot;: 101, \&quot;end\&quot;: 200, \&quot;fee\&quot;: 100 }, } &#x60;&#x60;&#x60; Then the following fees would be charged based on the total number of API calls (assuming the currency selected is &#x60;USD&#x60;): * 1 call costs $75 * 50 calls cost $75 * 150 calls cost $100 The number of API calls cannot exceed 200. |  [optional] |
|**consumptionPricingType** | [**ConsumptionPricingTypeEnum**](#ConsumptionPricingTypeEnum) | Pricing model used for consumption-based charges. |  [optional] |
|**createdAt** | **String** | Output only. Time that the rate plan was created in milliseconds since epoch. |  [optional] [readonly] |
|**currencyCode** | **String** | Currency to be used for billing. Consists of a three-letter code as defined by the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) standard. |  [optional] |
|**description** | **String** | Description of the rate plan. |  [optional] |
|**displayName** | **String** | Display name of the rate plan. |  [optional] |
|**endTime** | **String** | Time when the rate plan will expire in milliseconds since epoch. Set to 0 or &#x60;null&#x60; to indicate that the rate plan should never expire. |  [optional] |
|**fixedFeeFrequency** | **Integer** | Frequency at which the fixed fee is charged. |  [optional] |
|**fixedRecurringFee** | [**GoogleTypeMoney**](GoogleTypeMoney.md) |  |  [optional] |
|**lastModifiedAt** | **String** | Output only. Time the rate plan was last modified in milliseconds since epoch. |  [optional] [readonly] |
|**name** | **String** | Output only. Name of the rate plan. |  [optional] [readonly] |
|**paymentFundingModel** | [**PaymentFundingModelEnum**](#PaymentFundingModelEnum) | DEPRECATED: This field is no longer supported and will eventually be removed when Apigee Hybrid 1.5/1.6 is no longer supported. Instead, use the &#x60;billingType&#x60; field inside &#x60;DeveloperMonetizationConfig&#x60; resource. Flag that specifies the billing account type, prepaid or postpaid. |  [optional] |
|**revenueShareRates** | [**List&lt;GoogleCloudApigeeV1RevenueShareRange&gt;**](GoogleCloudApigeeV1RevenueShareRange.md) | Details of the revenue sharing model. |  [optional] |
|**revenueShareType** | [**RevenueShareTypeEnum**](#RevenueShareTypeEnum) | Method used to calculate the revenue that is shared with developers. |  [optional] |
|**setupFee** | [**GoogleTypeMoney**](GoogleTypeMoney.md) |  |  [optional] |
|**startTime** | **String** | Time when the rate plan becomes active in milliseconds since epoch. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Current state of the rate plan (draft or published). |  [optional] |



## Enum: BillingPeriodEnum

| Name | Value |
|---- | -----|
| BILLING_PERIOD_UNSPECIFIED | &quot;BILLING_PERIOD_UNSPECIFIED&quot; |
| WEEKLY | &quot;WEEKLY&quot; |
| MONTHLY | &quot;MONTHLY&quot; |



## Enum: ConsumptionPricingTypeEnum

| Name | Value |
|---- | -----|
| CONSUMPTION_PRICING_TYPE_UNSPECIFIED | &quot;CONSUMPTION_PRICING_TYPE_UNSPECIFIED&quot; |
| FIXED_PER_UNIT | &quot;FIXED_PER_UNIT&quot; |
| BANDED | &quot;BANDED&quot; |
| TIERED | &quot;TIERED&quot; |
| STAIRSTEP | &quot;STAIRSTEP&quot; |



## Enum: PaymentFundingModelEnum

| Name | Value |
|---- | -----|
| PAYMENT_FUNDING_MODEL_UNSPECIFIED | &quot;PAYMENT_FUNDING_MODEL_UNSPECIFIED&quot; |
| PREPAID | &quot;PREPAID&quot; |
| POSTPAID | &quot;POSTPAID&quot; |



## Enum: RevenueShareTypeEnum

| Name | Value |
|---- | -----|
| REVENUE_SHARE_TYPE_UNSPECIFIED | &quot;REVENUE_SHARE_TYPE_UNSPECIFIED&quot; |
| FIXED | &quot;FIXED&quot; |
| VOLUME_BANDED | &quot;VOLUME_BANDED&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| DRAFT | &quot;DRAFT&quot; |
| PUBLISHED | &quot;PUBLISHED&quot; |



