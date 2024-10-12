

# ShoppingAdsProgramStatusRegionStatus

Status of program and region.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disapprovalDate** | **String** | Date by which eligibilityStatus will go from &#x60;WARNING&#x60; to &#x60;DISAPPROVED&#x60;. Only visible when your eligibilityStatus is WARNING. In [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DD&#x60;. |  [optional] |
|**eligibilityStatus** | [**EligibilityStatusEnum**](#EligibilityStatusEnum) | Eligibility status of the Shopping Ads program. |  [optional] |
|**onboardingIssues** | **List&lt;String&gt;** | Issues that must be fixed to be eligible for review. |  [optional] |
|**regionCodes** | **List&lt;String&gt;** | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) codes for all the regions with the same &#x60;eligibilityStatus&#x60; and &#x60;reviewEligibility&#x60;. |  [optional] |
|**reviewEligibilityStatus** | [**ReviewEligibilityStatusEnum**](#ReviewEligibilityStatusEnum) | If a program is eligible for review in a specific region. Only visible if &#x60;eligibilityStatus&#x60; is &#x60;DISAPPROVED&#x60;. |  [optional] |
|**reviewIneligibilityReason** | [**ReviewIneligibilityReasonEnum**](#ReviewIneligibilityReasonEnum) | Review ineligibility reason if account is not eligible for review. |  [optional] |
|**reviewIneligibilityReasonDescription** | **String** | Reason a program in a specific region isn’t eligible for review. Only visible if &#x60;reviewEligibilityStatus&#x60; is &#x60;INELIGIBLE&#x60;. |  [optional] |
|**reviewIneligibilityReasonDetails** | [**ShoppingAdsProgramStatusReviewIneligibilityReasonDetails**](ShoppingAdsProgramStatusReviewIneligibilityReasonDetails.md) |  |  [optional] |
|**reviewIssues** | **List&lt;String&gt;** | Issues evaluated in the review process. Fix all issues before requesting a review. |  [optional] |



## Enum: EligibilityStatusEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| APPROVED | &quot;APPROVED&quot; |
| DISAPPROVED | &quot;DISAPPROVED&quot; |
| WARNING | &quot;WARNING&quot; |
| UNDER_REVIEW | &quot;UNDER_REVIEW&quot; |
| PENDING_REVIEW | &quot;PENDING_REVIEW&quot; |
| ONBOARDING | &quot;ONBOARDING&quot; |



## Enum: ReviewEligibilityStatusEnum

| Name | Value |
|---- | -----|
| REVIEW_ELIGIBILITY_UNSPECIFIED | &quot;REVIEW_ELIGIBILITY_UNSPECIFIED&quot; |
| ELIGIBLE | &quot;ELIGIBLE&quot; |
| INELIGIBLE | &quot;INELIGIBLE&quot; |



## Enum: ReviewIneligibilityReasonEnum

| Name | Value |
|---- | -----|
| REVIEW_INELIGIBILITY_REASON_UNSPECIFIED | &quot;REVIEW_INELIGIBILITY_REASON_UNSPECIFIED&quot; |
| ONBOARDING_ISSUES | &quot;ONBOARDING_ISSUES&quot; |
| NOT_ENOUGH_OFFERS | &quot;NOT_ENOUGH_OFFERS&quot; |
| IN_COOLDOWN_PERIOD | &quot;IN_COOLDOWN_PERIOD&quot; |
| ALREADY_UNDER_REVIEW | &quot;ALREADY_UNDER_REVIEW&quot; |
| NO_REVIEW_REQUIRED | &quot;NO_REVIEW_REQUIRED&quot; |
| WILL_BE_REVIEWED_AUTOMATICALLY | &quot;WILL_BE_REVIEWED_AUTOMATICALLY&quot; |
| IS_RETIRED | &quot;IS_RETIRED&quot; |
| ALREADY_REVIEWED | &quot;ALREADY_REVIEWED&quot; |



