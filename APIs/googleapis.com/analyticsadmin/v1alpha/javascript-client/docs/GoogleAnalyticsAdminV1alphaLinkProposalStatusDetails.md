# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1alphaLinkProposalStatusDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linkProposalInitiatingProduct** | **String** | Output only. The source of this proposal. | [optional] [readonly] 
**linkProposalState** | **String** | Output only. The state of this proposal. | [optional] [readonly] 
**requestorEmail** | **String** | Output only. The email address of the user that proposed this linkage. | [optional] [readonly] 



## Enum: LinkProposalInitiatingProductEnum


* `LINK_PROPOSAL_INITIATING_PRODUCT_UNSPECIFIED` (value: `"LINK_PROPOSAL_INITIATING_PRODUCT_UNSPECIFIED"`)

* `GOOGLE_ANALYTICS` (value: `"GOOGLE_ANALYTICS"`)

* `LINKED_PRODUCT` (value: `"LINKED_PRODUCT"`)





## Enum: LinkProposalStateEnum


* `LINK_PROPOSAL_STATE_UNSPECIFIED` (value: `"LINK_PROPOSAL_STATE_UNSPECIFIED"`)

* `AWAITING_REVIEW_FROM_GOOGLE_ANALYTICS` (value: `"AWAITING_REVIEW_FROM_GOOGLE_ANALYTICS"`)

* `AWAITING_REVIEW_FROM_LINKED_PRODUCT` (value: `"AWAITING_REVIEW_FROM_LINKED_PRODUCT"`)

* `WITHDRAWN` (value: `"WITHDRAWN"`)

* `DECLINED` (value: `"DECLINED"`)

* `EXPIRED` (value: `"EXPIRED"`)

* `OBSOLETE` (value: `"OBSOLETE"`)




