# ContentApiForShopping.ShoppingAdsProgramStatusRegionStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disapprovalDate** | **String** | Date by which eligibilityStatus will go from &#x60;WARNING&#x60; to &#x60;DISAPPROVED&#x60;. Only visible when your eligibilityStatus is WARNING. In [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DD&#x60;. | [optional] 
**eligibilityStatus** | **String** | Eligibility status of the Shopping Ads program. | [optional] 
**onboardingIssues** | **[String]** | Issues that must be fixed to be eligible for review. | [optional] 
**regionCodes** | **[String]** | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) codes for all the regions with the same &#x60;eligibilityStatus&#x60; and &#x60;reviewEligibility&#x60;. | [optional] 
**reviewEligibilityStatus** | **String** | If a program is eligible for review in a specific region. Only visible if &#x60;eligibilityStatus&#x60; is &#x60;DISAPPROVED&#x60;. | [optional] 
**reviewIneligibilityReason** | **String** | Review ineligibility reason if account is not eligible for review. | [optional] 
**reviewIneligibilityReasonDescription** | **String** | Reason a program in a specific region isn’t eligible for review. Only visible if &#x60;reviewEligibilityStatus&#x60; is &#x60;INELIGIBLE&#x60;. | [optional] 
**reviewIneligibilityReasonDetails** | [**ShoppingAdsProgramStatusReviewIneligibilityReasonDetails**](ShoppingAdsProgramStatusReviewIneligibilityReasonDetails.md) |  | [optional] 
**reviewIssues** | **[String]** | Issues evaluated in the review process. Fix all issues before requesting a review. | [optional] 



## Enum: EligibilityStatusEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `APPROVED` (value: `"APPROVED"`)

* `DISAPPROVED` (value: `"DISAPPROVED"`)

* `WARNING` (value: `"WARNING"`)

* `UNDER_REVIEW` (value: `"UNDER_REVIEW"`)

* `PENDING_REVIEW` (value: `"PENDING_REVIEW"`)

* `ONBOARDING` (value: `"ONBOARDING"`)





## Enum: ReviewEligibilityStatusEnum


* `REVIEW_ELIGIBILITY_UNSPECIFIED` (value: `"REVIEW_ELIGIBILITY_UNSPECIFIED"`)

* `ELIGIBLE` (value: `"ELIGIBLE"`)

* `INELIGIBLE` (value: `"INELIGIBLE"`)





## Enum: ReviewIneligibilityReasonEnum


* `REVIEW_INELIGIBILITY_REASON_UNSPECIFIED` (value: `"REVIEW_INELIGIBILITY_REASON_UNSPECIFIED"`)

* `ONBOARDING_ISSUES` (value: `"ONBOARDING_ISSUES"`)

* `NOT_ENOUGH_OFFERS` (value: `"NOT_ENOUGH_OFFERS"`)

* `IN_COOLDOWN_PERIOD` (value: `"IN_COOLDOWN_PERIOD"`)

* `ALREADY_UNDER_REVIEW` (value: `"ALREADY_UNDER_REVIEW"`)

* `NO_REVIEW_REQUIRED` (value: `"NO_REVIEW_REQUIRED"`)

* `WILL_BE_REVIEWED_AUTOMATICALLY` (value: `"WILL_BE_REVIEWED_AUTOMATICALLY"`)

* `IS_RETIRED` (value: `"IS_RETIRED"`)

* `ALREADY_REVIEWED` (value: `"ALREADY_REVIEWED"`)




