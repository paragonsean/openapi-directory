# DisplayVideo360Api.ReviewStatusInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approvalStatus** | **String** | Represents the basic approval needed for a creative to begin serving. Summary of creative_and_landing_page_review_status and content_and_policy_review_status. | [optional] 
**contentAndPolicyReviewStatus** | **String** | Content and policy review status for the creative. | [optional] 
**creativeAndLandingPageReviewStatus** | **String** | Creative and landing page review status for the creative. | [optional] 
**exchangeReviewStatuses** | [**[ExchangeReviewStatus]**](ExchangeReviewStatus.md) | Exchange review statuses for the creative. | [optional] 
**publisherReviewStatuses** | [**[PublisherReviewStatus]**](PublisherReviewStatus.md) | Publisher review statuses for the creative. | [optional] 



## Enum: ApprovalStatusEnum


* `UNSPECIFIED` (value: `"APPROVAL_STATUS_UNSPECIFIED"`)

* `PENDING_NOT_SERVABLE` (value: `"APPROVAL_STATUS_PENDING_NOT_SERVABLE"`)

* `PENDING_SERVABLE` (value: `"APPROVAL_STATUS_PENDING_SERVABLE"`)

* `APPROVED_SERVABLE` (value: `"APPROVAL_STATUS_APPROVED_SERVABLE"`)

* `REJECTED_NOT_SERVABLE` (value: `"APPROVAL_STATUS_REJECTED_NOT_SERVABLE"`)





## Enum: ContentAndPolicyReviewStatusEnum


* `UNSPECIFIED` (value: `"REVIEW_STATUS_UNSPECIFIED"`)

* `APPROVED` (value: `"REVIEW_STATUS_APPROVED"`)

* `REJECTED` (value: `"REVIEW_STATUS_REJECTED"`)

* `PENDING` (value: `"REVIEW_STATUS_PENDING"`)





## Enum: CreativeAndLandingPageReviewStatusEnum


* `UNSPECIFIED` (value: `"REVIEW_STATUS_UNSPECIFIED"`)

* `APPROVED` (value: `"REVIEW_STATUS_APPROVED"`)

* `REJECTED` (value: `"REVIEW_STATUS_REJECTED"`)

* `PENDING` (value: `"REVIEW_STATUS_PENDING"`)




