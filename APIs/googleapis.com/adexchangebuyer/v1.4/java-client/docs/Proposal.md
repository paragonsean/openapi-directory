

# Proposal

Represents a proposal in the marketplace. A proposal is the unit of negotiation between a seller and a buyer and contains deals which are served. Each field in a proposal can have one of the following setting:  (readonly) - It is an error to try and set this field. (buyer-readonly) - Only the seller can set this field. (seller-readonly) - Only the buyer can set this field. (updatable) - The field is updatable at all times by either buyer or the seller.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billedBuyer** | [**Buyer**](Buyer.md) |  |  [optional] |
|**buyer** | [**Buyer**](Buyer.md) |  |  [optional] |
|**buyerContacts** | [**List&lt;ContactInformation&gt;**](ContactInformation.md) | Optional contact information of the buyer. (seller-readonly) |  [optional] |
|**buyerPrivateData** | [**PrivateData**](PrivateData.md) |  |  [optional] |
|**dbmAdvertiserIds** | **List&lt;String&gt;** | IDs of DBM advertisers permission to this proposal. |  [optional] |
|**hasBuyerSignedOff** | **Boolean** | When an proposal is in an accepted state, indicates whether the buyer has signed off. Once both sides have signed off on a deal, the proposal can be finalized by the seller. (seller-readonly) |  [optional] |
|**hasSellerSignedOff** | **Boolean** | When an proposal is in an accepted state, indicates whether the buyer has signed off Once both sides have signed off on a deal, the proposal can be finalized by the seller. (buyer-readonly) |  [optional] |
|**inventorySource** | **String** | What exchange will provide this inventory (readonly, except on create). |  [optional] |
|**isRenegotiating** | **Boolean** | True if the proposal is being renegotiated (readonly). |  [optional] |
|**isSetupComplete** | **Boolean** | True, if the buyside inventory setup is complete for this proposal. (readonly, except via OrderSetupCompleted action) Deprecated in favor of deal level setup complete flag. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;adexchangebuyer#proposal\&quot;. |  [optional] |
|**labels** | [**List&lt;MarketplaceLabel&gt;**](MarketplaceLabel.md) | List of labels associated with the proposal. (readonly) |  [optional] |
|**lastUpdaterOrCommentorRole** | **String** | The role of the last user that either updated the proposal or left a comment. (readonly) |  [optional] |
|**name** | **String** | The name for the proposal (updatable) |  [optional] |
|**negotiationId** | **String** | Optional negotiation id if this proposal is a preferred deal proposal. |  [optional] |
|**originatorRole** | **String** | Indicates whether the buyer/seller created the proposal.(readonly) |  [optional] |
|**privateAuctionId** | **String** | Optional private auction id if this proposal is a private auction proposal. |  [optional] |
|**proposalId** | **String** | The unique id of the proposal. (readonly). |  [optional] |
|**proposalState** | **String** | The current state of the proposal. (readonly) |  [optional] |
|**revisionNumber** | **String** | The revision number for the proposal (readonly). |  [optional] |
|**revisionTimeMs** | **String** | The time (ms since epoch) when the proposal was last revised (readonly). |  [optional] |
|**seller** | [**Seller**](Seller.md) |  |  [optional] |
|**sellerContacts** | [**List&lt;ContactInformation&gt;**](ContactInformation.md) | Optional contact information of the seller (buyer-readonly). |  [optional] |



