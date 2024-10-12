

# Product

A product is segment of inventory that a seller wishes to sell. It is associated with certain terms and targeting information which helps buyer know more about the inventory. Each field in a product can have one of the following setting:  (readonly) - It is an error to try and set this field. (buyer-readonly) - Only the seller can set this field. (seller-readonly) - Only the buyer can set this field. (updatable) - The field is updatable at all times by either buyer or the seller.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billedBuyer** | [**Buyer**](Buyer.md) |  |  [optional] |
|**buyer** | [**Buyer**](Buyer.md) |  |  [optional] |
|**creationTimeMs** | **String** | Creation time in ms. since epoch (readonly) |  [optional] |
|**creatorContacts** | [**List&lt;ContactInformation&gt;**](ContactInformation.md) | Optional contact information for the creator of this product. (buyer-readonly) |  [optional] |
|**creatorRole** | **String** | The role that created the offer. Set to BUYER for buyer initiated offers. |  [optional] |
|**deliveryControl** | [**DeliveryControl**](DeliveryControl.md) |  |  [optional] |
|**flightEndTimeMs** | **String** | The proposed end time for the deal (ms since epoch) (buyer-readonly) |  [optional] |
|**flightStartTimeMs** | **String** | Inventory availability dates. (times are in ms since epoch) The granularity is generally in the order of seconds. (buyer-readonly) |  [optional] |
|**hasCreatorSignedOff** | **Boolean** | If the creator has already signed off on the product, then the buyer can finalize the deal by accepting the product as is. When copying to a proposal, if any of the terms are changed, then auto_finalize is automatically set to false. |  [optional] |
|**inventorySource** | **String** | What exchange will provide this inventory (readonly, except on create). |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;adexchangebuyer#product\&quot;. |  [optional] |
|**labels** | [**List&lt;MarketplaceLabel&gt;**](MarketplaceLabel.md) | Optional List of labels for the product (optional, buyer-readonly). |  [optional] |
|**lastUpdateTimeMs** | **String** | Time of last update in ms. since epoch (readonly) |  [optional] |
|**legacyOfferId** | **String** | Optional legacy offer id if this offer is a preferred deal offer. |  [optional] |
|**marketplacePublisherProfileId** | **String** | Marketplace publisher profile Id. This Id differs from the regular publisher_profile_id in that 1. This is a new id, the old Id will be deprecated in 2017. 2. This id uniquely identifies a publisher profile by itself. |  [optional] |
|**name** | **String** | The name for this product as set by the seller. (buyer-readonly) |  [optional] |
|**privateAuctionId** | **String** | Optional private auction id if this offer is a private auction offer. |  [optional] |
|**productId** | **String** | The unique id for the product (readonly) |  [optional] |
|**publisherProfileId** | **String** | Id of the publisher profile for a given seller. A (seller.account_id, publisher_profile_id) pair uniquely identifies a publisher profile. Buyers can call the PublisherProfiles::List endpoint to get a list of publisher profiles for a given seller. |  [optional] |
|**publisherProvidedForecast** | [**PublisherProvidedForecast**](PublisherProvidedForecast.md) |  |  [optional] |
|**revisionNumber** | **String** | The revision number of the product. (readonly) |  [optional] |
|**seller** | [**Seller**](Seller.md) |  |  [optional] |
|**sharedTargetings** | [**List&lt;SharedTargeting&gt;**](SharedTargeting.md) | Targeting that is shared between the buyer and the seller. Each targeting criteria has a specified key and for each key there is a list of inclusion value or exclusion values. (buyer-readonly) |  [optional] |
|**state** | **String** | The state of the product. (buyer-readonly) |  [optional] |
|**syndicationProduct** | **String** | The syndication product associated with the deal. (readonly, except on create) |  [optional] |
|**terms** | [**DealTerms**](DealTerms.md) |  |  [optional] |
|**webPropertyCode** | **String** | The web property code for the seller. This field is meant to be copied over as is when creating deals. |  [optional] |



