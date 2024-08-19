# AdExchangeBuyerApiIi.Proposal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billedBuyer** | [**Buyer**](Buyer.md) |  | [optional] 
**buyer** | [**Buyer**](Buyer.md) |  | [optional] 
**buyerContacts** | [**[ContactInformation]**](ContactInformation.md) | Contact information for the buyer. | [optional] 
**buyerPrivateData** | [**PrivateData**](PrivateData.md) |  | [optional] 
**deals** | [**[Deal]**](Deal.md) | The deals associated with this proposal. For Private Auction proposals (whose deals have NonGuaranteedAuctionTerms), there will only be one deal. | [optional] 
**displayName** | **String** | The name for the proposal. | [optional] 
**isRenegotiating** | **Boolean** | Output only. True if the proposal is being renegotiated. | [optional] [readonly] 
**isSetupComplete** | **Boolean** | Output only. True, if the buyside inventory setup is complete for this proposal. | [optional] [readonly] 
**lastUpdaterOrCommentorRole** | **String** | Output only. The role of the last user that either updated the proposal or left a comment. | [optional] [readonly] 
**notes** | [**[Note]**](Note.md) | Output only. The notes associated with this proposal. | [optional] [readonly] 
**originatorRole** | **String** | Output only. Indicates whether the buyer/seller created the proposal. | [optional] [readonly] 
**privateAuctionId** | **String** | Output only. Private auction ID if this proposal is a private auction proposal. | [optional] [readonly] 
**proposalId** | **String** | Output only. The unique ID of the proposal. | [optional] [readonly] 
**proposalRevision** | **String** | Output only. The revision number for the proposal. Each update to the proposal or the deal causes the proposal revision number to auto-increment. The buyer keeps track of the last revision number they know of and pass it in when making an update. If the head revision number on the server has since incremented, then an ABORTED error is returned during the update operation to let the buyer know that a subsequent update was made. | [optional] [readonly] 
**proposalState** | **String** | Output only. The current state of the proposal. | [optional] [readonly] 
**seller** | [**Seller**](Seller.md) |  | [optional] 
**sellerContacts** | [**[ContactInformation]**](ContactInformation.md) | Output only. Contact information for the seller. | [optional] [readonly] 
**termsAndConditions** | **String** | Output only. The terms and conditions set by the publisher for this proposal. | [optional] [readonly] 
**updateTime** | **String** | Output only. The time when the proposal was last revised. | [optional] [readonly] 



## Enum: LastUpdaterOrCommentorRoleEnum


* `BUYER_SELLER_ROLE_UNSPECIFIED` (value: `"BUYER_SELLER_ROLE_UNSPECIFIED"`)

* `BUYER` (value: `"BUYER"`)

* `SELLER` (value: `"SELLER"`)





## Enum: OriginatorRoleEnum


* `BUYER_SELLER_ROLE_UNSPECIFIED` (value: `"BUYER_SELLER_ROLE_UNSPECIFIED"`)

* `BUYER` (value: `"BUYER"`)

* `SELLER` (value: `"SELLER"`)





## Enum: ProposalStateEnum


* `PROPOSAL_STATE_UNSPECIFIED` (value: `"PROPOSAL_STATE_UNSPECIFIED"`)

* `PROPOSED` (value: `"PROPOSED"`)

* `BUYER_ACCEPTED` (value: `"BUYER_ACCEPTED"`)

* `SELLER_ACCEPTED` (value: `"SELLER_ACCEPTED"`)

* `CANCELED` (value: `"CANCELED"`)

* `FINALIZED` (value: `"FINALIZED"`)




