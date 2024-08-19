

# GoogleAnalyticsAdminV1alphaLinkProposalStatusDetails

Status information for a link proposal.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**linkProposalInitiatingProduct** | [**LinkProposalInitiatingProductEnum**](#LinkProposalInitiatingProductEnum) | Output only. The source of this proposal. |  [optional] [readonly] |
|**linkProposalState** | [**LinkProposalStateEnum**](#LinkProposalStateEnum) | Output only. The state of this proposal. |  [optional] [readonly] |
|**requestorEmail** | **String** | Output only. The email address of the user that proposed this linkage. |  [optional] [readonly] |



## Enum: LinkProposalInitiatingProductEnum

| Name | Value |
|---- | -----|
| LINK_PROPOSAL_INITIATING_PRODUCT_UNSPECIFIED | &quot;LINK_PROPOSAL_INITIATING_PRODUCT_UNSPECIFIED&quot; |
| GOOGLE_ANALYTICS | &quot;GOOGLE_ANALYTICS&quot; |
| LINKED_PRODUCT | &quot;LINKED_PRODUCT&quot; |



## Enum: LinkProposalStateEnum

| Name | Value |
|---- | -----|
| LINK_PROPOSAL_STATE_UNSPECIFIED | &quot;LINK_PROPOSAL_STATE_UNSPECIFIED&quot; |
| AWAITING_REVIEW_FROM_GOOGLE_ANALYTICS | &quot;AWAITING_REVIEW_FROM_GOOGLE_ANALYTICS&quot; |
| AWAITING_REVIEW_FROM_LINKED_PRODUCT | &quot;AWAITING_REVIEW_FROM_LINKED_PRODUCT&quot; |
| WITHDRAWN | &quot;WITHDRAWN&quot; |
| DECLINED | &quot;DECLINED&quot; |
| EXPIRED | &quot;EXPIRED&quot; |
| OBSOLETE | &quot;OBSOLETE&quot; |



