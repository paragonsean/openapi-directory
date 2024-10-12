

# ReviewStatusInfo

Review statuses for the creative.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**approvalStatus** | [**ApprovalStatusEnum**](#ApprovalStatusEnum) | Represents the basic approval needed for a creative to begin serving. Summary of creative_and_landing_page_review_status and content_and_policy_review_status. |  [optional] |
|**contentAndPolicyReviewStatus** | [**ContentAndPolicyReviewStatusEnum**](#ContentAndPolicyReviewStatusEnum) | Content and policy review status for the creative. |  [optional] |
|**creativeAndLandingPageReviewStatus** | [**CreativeAndLandingPageReviewStatusEnum**](#CreativeAndLandingPageReviewStatusEnum) | Creative and landing page review status for the creative. |  [optional] |
|**exchangeReviewStatuses** | [**List&lt;ExchangeReviewStatus&gt;**](ExchangeReviewStatus.md) | Exchange review statuses for the creative. |  [optional] |
|**publisherReviewStatuses** | [**List&lt;PublisherReviewStatus&gt;**](PublisherReviewStatus.md) | Publisher review statuses for the creative. |  [optional] |



## Enum: ApprovalStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;APPROVAL_STATUS_UNSPECIFIED&quot; |
| PENDING_NOT_SERVABLE | &quot;APPROVAL_STATUS_PENDING_NOT_SERVABLE&quot; |
| PENDING_SERVABLE | &quot;APPROVAL_STATUS_PENDING_SERVABLE&quot; |
| APPROVED_SERVABLE | &quot;APPROVAL_STATUS_APPROVED_SERVABLE&quot; |
| REJECTED_NOT_SERVABLE | &quot;APPROVAL_STATUS_REJECTED_NOT_SERVABLE&quot; |



## Enum: ContentAndPolicyReviewStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;REVIEW_STATUS_UNSPECIFIED&quot; |
| APPROVED | &quot;REVIEW_STATUS_APPROVED&quot; |
| REJECTED | &quot;REVIEW_STATUS_REJECTED&quot; |
| PENDING | &quot;REVIEW_STATUS_PENDING&quot; |



## Enum: CreativeAndLandingPageReviewStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;REVIEW_STATUS_UNSPECIFIED&quot; |
| APPROVED | &quot;REVIEW_STATUS_APPROVED&quot; |
| REJECTED | &quot;REVIEW_STATUS_REJECTED&quot; |
| PENDING | &quot;REVIEW_STATUS_PENDING&quot; |



