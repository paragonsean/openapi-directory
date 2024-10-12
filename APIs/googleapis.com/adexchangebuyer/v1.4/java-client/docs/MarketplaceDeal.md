

# MarketplaceDeal

A proposal can contain multiple deals. A deal contains the terms and targeting information that is used for serving.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**buyerPrivateData** | [**PrivateData**](PrivateData.md) |  |  [optional] |
|**creationTimeMs** | **String** | The time (ms since epoch) of the deal creation. (readonly) |  [optional] |
|**creativePreApprovalPolicy** | **String** | Specifies the creative pre-approval policy (buyer-readonly) |  [optional] |
|**creativeSafeFrameCompatibility** | **String** | Specifies whether the creative is safeFrame compatible (buyer-readonly) |  [optional] |
|**dealId** | **String** | A unique deal-id for the deal (readonly). |  [optional] |
|**dealServingMetadata** | [**DealServingMetadata**](DealServingMetadata.md) |  |  [optional] |
|**deliveryControl** | [**DeliveryControl**](DeliveryControl.md) |  |  [optional] |
|**externalDealId** | **String** | The external deal id assigned to this deal once the deal is finalized. This is the deal-id that shows up in serving/reporting etc. (readonly) |  [optional] |
|**flightEndTimeMs** | **String** | Proposed flight end time of the deal (ms since epoch) This will generally be stored in a granularity of a second. (updatable) |  [optional] |
|**flightStartTimeMs** | **String** | Proposed flight start time of the deal (ms since epoch) This will generally be stored in a granularity of a second. (updatable) |  [optional] |
|**inventoryDescription** | **String** | Description for the deal terms. (buyer-readonly) |  [optional] |
|**isRfpTemplate** | **Boolean** | Indicates whether the current deal is a RFP template. RFP template is created by buyer and not based on seller created products. |  [optional] |
|**isSetupComplete** | **Boolean** | True, if the buyside inventory setup is complete for this deal. (readonly, except via OrderSetupCompleted action) |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;adexchangebuyer#marketplaceDeal\&quot;. |  [optional] |
|**lastUpdateTimeMs** | **String** | The time (ms since epoch) when the deal was last updated. (readonly) |  [optional] |
|**makegoodRequestedReason** | **String** |  |  [optional] |
|**name** | **String** | The name of the deal. (updatable) |  [optional] |
|**productId** | **String** | The product-id from which this deal was created. (readonly, except on create) |  [optional] |
|**productRevisionNumber** | **String** | The revision number of the product that the deal was created from (readonly, except on create) |  [optional] |
|**programmaticCreativeSource** | **String** | Specifies the creative source for programmatic deals, PUBLISHER means creative is provided by seller and ADVERTISR means creative is provided by buyer. (buyer-readonly) |  [optional] |
|**proposalId** | **String** |  |  [optional] |
|**sellerContacts** | [**List&lt;ContactInformation&gt;**](ContactInformation.md) | Optional Seller contact information for the deal (buyer-readonly) |  [optional] |
|**sharedTargetings** | [**List&lt;SharedTargeting&gt;**](SharedTargeting.md) | The shared targeting visible to buyers and sellers. Each shared targeting entity is AND&#39;d together. (updatable) |  [optional] |
|**syndicationProduct** | **String** | The syndication product associated with the deal. (readonly, except on create) |  [optional] |
|**terms** | [**DealTerms**](DealTerms.md) |  |  [optional] |
|**webPropertyCode** | **String** |  |  [optional] |



