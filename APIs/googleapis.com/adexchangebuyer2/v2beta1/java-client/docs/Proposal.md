

# Proposal

Represents a proposal in the Marketplace. A proposal is the unit of negotiation between a seller and a buyer and contains deals which are served. Note: You can't update, create, or otherwise modify Private Auction deals through the API. Fields are updatable unless noted otherwise.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billedBuyer** | [**Buyer**](Buyer.md) |  |  [optional] |
|**buyer** | [**Buyer**](Buyer.md) |  |  [optional] |
|**buyerContacts** | [**List&lt;ContactInformation&gt;**](ContactInformation.md) | Contact information for the buyer. |  [optional] |
|**buyerPrivateData** | [**PrivateData**](PrivateData.md) |  |  [optional] |
|**deals** | [**List&lt;Deal&gt;**](Deal.md) | The deals associated with this proposal. For Private Auction proposals (whose deals have NonGuaranteedAuctionTerms), there will only be one deal. |  [optional] |
|**displayName** | **String** | The name for the proposal. |  [optional] |
|**isRenegotiating** | **Boolean** | Output only. True if the proposal is being renegotiated. |  [optional] [readonly] |
|**isSetupComplete** | **Boolean** | Output only. True, if the buyside inventory setup is complete for this proposal. |  [optional] [readonly] |
|**lastUpdaterOrCommentorRole** | [**LastUpdaterOrCommentorRoleEnum**](#LastUpdaterOrCommentorRoleEnum) | Output only. The role of the last user that either updated the proposal or left a comment. |  [optional] [readonly] |
|**notes** | [**List&lt;Note&gt;**](Note.md) | Output only. The notes associated with this proposal. |  [optional] [readonly] |
|**originatorRole** | [**OriginatorRoleEnum**](#OriginatorRoleEnum) | Output only. Indicates whether the buyer/seller created the proposal. |  [optional] [readonly] |
|**privateAuctionId** | **String** | Output only. Private auction ID if this proposal is a private auction proposal. |  [optional] [readonly] |
|**proposalId** | **String** | Output only. The unique ID of the proposal. |  [optional] [readonly] |
|**proposalRevision** | **String** | Output only. The revision number for the proposal. Each update to the proposal or the deal causes the proposal revision number to auto-increment. The buyer keeps track of the last revision number they know of and pass it in when making an update. If the head revision number on the server has since incremented, then an ABORTED error is returned during the update operation to let the buyer know that a subsequent update was made. |  [optional] [readonly] |
|**proposalState** | [**ProposalStateEnum**](#ProposalStateEnum) | Output only. The current state of the proposal. |  [optional] [readonly] |
|**seller** | [**Seller**](Seller.md) |  |  [optional] |
|**sellerContacts** | [**List&lt;ContactInformation&gt;**](ContactInformation.md) | Output only. Contact information for the seller. |  [optional] [readonly] |
|**termsAndConditions** | **String** | Output only. The terms and conditions set by the publisher for this proposal. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The time when the proposal was last revised. |  [optional] [readonly] |



## Enum: LastUpdaterOrCommentorRoleEnum

| Name | Value |
|---- | -----|
| BUYER_SELLER_ROLE_UNSPECIFIED | &quot;BUYER_SELLER_ROLE_UNSPECIFIED&quot; |
| BUYER | &quot;BUYER&quot; |
| SELLER | &quot;SELLER&quot; |



## Enum: OriginatorRoleEnum

| Name | Value |
|---- | -----|
| BUYER_SELLER_ROLE_UNSPECIFIED | &quot;BUYER_SELLER_ROLE_UNSPECIFIED&quot; |
| BUYER | &quot;BUYER&quot; |
| SELLER | &quot;SELLER&quot; |



## Enum: ProposalStateEnum

| Name | Value |
|---- | -----|
| PROPOSAL_STATE_UNSPECIFIED | &quot;PROPOSAL_STATE_UNSPECIFIED&quot; |
| PROPOSED | &quot;PROPOSED&quot; |
| BUYER_ACCEPTED | &quot;BUYER_ACCEPTED&quot; |
| SELLER_ACCEPTED | &quot;SELLER_ACCEPTED&quot; |
| CANCELED | &quot;CANCELED&quot; |
| FINALIZED | &quot;FINALIZED&quot; |



