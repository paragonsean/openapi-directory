# ApigeeApi.GoogleCloudApigeeV1RatePlan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiproduct** | **String** | Name of the API product that the rate plan is associated with. | [optional] 
**billingPeriod** | **String** | Frequency at which the customer will be billed. | [optional] 
**consumptionPricingRates** | [**[GoogleCloudApigeeV1RateRange]**](GoogleCloudApigeeV1RateRange.md) | API call volume ranges and the fees charged when the total number of API calls is within a given range. The method used to calculate the final fee depends on the selected pricing model. For example, if the pricing model is &#x60;STAIRSTEP&#x60; and the ranges are defined as follows: &#x60;&#x60;&#x60; { \&quot;start\&quot;: 1, \&quot;end\&quot;: 100, \&quot;fee\&quot;: 75 }, { \&quot;start\&quot;: 101, \&quot;end\&quot;: 200, \&quot;fee\&quot;: 100 }, } &#x60;&#x60;&#x60; Then the following fees would be charged based on the total number of API calls (assuming the currency selected is &#x60;USD&#x60;): * 1 call costs $75 * 50 calls cost $75 * 150 calls cost $100 The number of API calls cannot exceed 200. | [optional] 
**consumptionPricingType** | **String** | Pricing model used for consumption-based charges. | [optional] 
**createdAt** | **String** | Output only. Time that the rate plan was created in milliseconds since epoch. | [optional] [readonly] 
**currencyCode** | **String** | Currency to be used for billing. Consists of a three-letter code as defined by the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) standard. | [optional] 
**description** | **String** | Description of the rate plan. | [optional] 
**displayName** | **String** | Display name of the rate plan. | [optional] 
**endTime** | **String** | Time when the rate plan will expire in milliseconds since epoch. Set to 0 or &#x60;null&#x60; to indicate that the rate plan should never expire. | [optional] 
**fixedFeeFrequency** | **Number** | Frequency at which the fixed fee is charged. | [optional] 
**fixedRecurringFee** | [**GoogleTypeMoney**](GoogleTypeMoney.md) |  | [optional] 
**lastModifiedAt** | **String** | Output only. Time the rate plan was last modified in milliseconds since epoch. | [optional] [readonly] 
**name** | **String** | Output only. Name of the rate plan. | [optional] [readonly] 
**paymentFundingModel** | **String** | DEPRECATED: This field is no longer supported and will eventually be removed when Apigee Hybrid 1.5/1.6 is no longer supported. Instead, use the &#x60;billingType&#x60; field inside &#x60;DeveloperMonetizationConfig&#x60; resource. Flag that specifies the billing account type, prepaid or postpaid. | [optional] 
**revenueShareRates** | [**[GoogleCloudApigeeV1RevenueShareRange]**](GoogleCloudApigeeV1RevenueShareRange.md) | Details of the revenue sharing model. | [optional] 
**revenueShareType** | **String** | Method used to calculate the revenue that is shared with developers. | [optional] 
**setupFee** | [**GoogleTypeMoney**](GoogleTypeMoney.md) |  | [optional] 
**startTime** | **String** | Time when the rate plan becomes active in milliseconds since epoch. | [optional] 
**state** | **String** | Current state of the rate plan (draft or published). | [optional] 



## Enum: BillingPeriodEnum


* `BILLING_PERIOD_UNSPECIFIED` (value: `"BILLING_PERIOD_UNSPECIFIED"`)

* `WEEKLY` (value: `"WEEKLY"`)

* `MONTHLY` (value: `"MONTHLY"`)





## Enum: ConsumptionPricingTypeEnum


* `CONSUMPTION_PRICING_TYPE_UNSPECIFIED` (value: `"CONSUMPTION_PRICING_TYPE_UNSPECIFIED"`)

* `FIXED_PER_UNIT` (value: `"FIXED_PER_UNIT"`)

* `BANDED` (value: `"BANDED"`)

* `TIERED` (value: `"TIERED"`)

* `STAIRSTEP` (value: `"STAIRSTEP"`)





## Enum: PaymentFundingModelEnum


* `PAYMENT_FUNDING_MODEL_UNSPECIFIED` (value: `"PAYMENT_FUNDING_MODEL_UNSPECIFIED"`)

* `PREPAID` (value: `"PREPAID"`)

* `POSTPAID` (value: `"POSTPAID"`)





## Enum: RevenueShareTypeEnum


* `REVENUE_SHARE_TYPE_UNSPECIFIED` (value: `"REVENUE_SHARE_TYPE_UNSPECIFIED"`)

* `FIXED` (value: `"FIXED"`)

* `VOLUME_BANDED` (value: `"VOLUME_BANDED"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `DRAFT` (value: `"DRAFT"`)

* `PUBLISHED` (value: `"PUBLISHED"`)




