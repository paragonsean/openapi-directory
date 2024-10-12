# ContentApiForShopping.CheckoutSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effectiveEnrollmentState** | **String** | Output only. The effective value of enrollment state for a given merchant ID. If account level settings are present then this value will be a copy of the account level settings. Otherwise, it will have the value of the parent account. | [optional] [readonly] 
**effectiveReviewState** | **String** | Output only. The effective value of review state for a given merchant ID. If account level settings are present then this value will be a copy of the account level settings. Otherwise, it will have the value of the parent account. | [optional] [readonly] 
**effectiveUriSettings** | [**UrlSettings**](UrlSettings.md) |  | [optional] 
**enrollmentState** | **String** | Output only. Reflects the merchant enrollment state in &#x60;Checkout&#x60; feature. | [optional] [readonly] 
**merchantId** | **String** | Required. The ID of the account. | [optional] 
**reviewState** | **String** | Output only. Reflects the merchant review state in &#x60;Checkout&#x60; feature. This is set based on the data quality reviews of the URL provided by the merchant. A merchant with enrollment state as &#x60;ENROLLED&#x60; can be in the following review states: &#x60;IN_REVIEW&#x60;, &#x60;APPROVED&#x60; or &#x60;DISAPPROVED&#x60;. A merchant must be in an enrollment_state of &#x60;ENROLLED&#x60; before a review can begin for the merchant. | [optional] [readonly] 
**uriSettings** | [**UrlSettings**](UrlSettings.md) |  | [optional] 



## Enum: EffectiveEnrollmentStateEnum


* `CHECKOUT_ON_MERCHANT_ENROLLMENT_STATE_UNSPECIFIED` (value: `"CHECKOUT_ON_MERCHANT_ENROLLMENT_STATE_UNSPECIFIED"`)

* `INACTIVE` (value: `"INACTIVE"`)

* `ENROLLED` (value: `"ENROLLED"`)

* `OPT_OUT` (value: `"OPT_OUT"`)





## Enum: EffectiveReviewStateEnum


* `CHECKOUT_ON_MERCHANT_REVIEW_STATE_UNSPECIFIED` (value: `"CHECKOUT_ON_MERCHANT_REVIEW_STATE_UNSPECIFIED"`)

* `IN_REVIEW` (value: `"IN_REVIEW"`)

* `APPROVED` (value: `"APPROVED"`)

* `DISAPPROVED` (value: `"DISAPPROVED"`)





## Enum: EnrollmentStateEnum


* `CHECKOUT_ON_MERCHANT_ENROLLMENT_STATE_UNSPECIFIED` (value: `"CHECKOUT_ON_MERCHANT_ENROLLMENT_STATE_UNSPECIFIED"`)

* `INACTIVE` (value: `"INACTIVE"`)

* `ENROLLED` (value: `"ENROLLED"`)

* `OPT_OUT` (value: `"OPT_OUT"`)





## Enum: ReviewStateEnum


* `CHECKOUT_ON_MERCHANT_REVIEW_STATE_UNSPECIFIED` (value: `"CHECKOUT_ON_MERCHANT_REVIEW_STATE_UNSPECIFIED"`)

* `IN_REVIEW` (value: `"IN_REVIEW"`)

* `APPROVED` (value: `"APPROVED"`)

* `DISAPPROVED` (value: `"DISAPPROVED"`)




