

# DealTerms


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brandingType** | **String** | Visibility of the URL in bid requests. |  [optional] |
|**crossListedExternalDealIdType** | **String** | Indicates that this ExternalDealId exists under at least two different AdxInventoryDeals. Currently, the only case that the same ExternalDealId will exist is programmatic cross sell case. |  [optional] |
|**description** | **String** | Description for the proposed terms of the deal. |  [optional] |
|**estimatedGrossSpend** | [**Price**](Price.md) |  |  [optional] |
|**estimatedImpressionsPerDay** | **String** | Non-binding estimate of the impressions served per day Can be set by buyer or seller. |  [optional] |
|**guaranteedFixedPriceTerms** | [**DealTermsGuaranteedFixedPriceTerms**](DealTermsGuaranteedFixedPriceTerms.md) |  |  [optional] |
|**nonGuaranteedAuctionTerms** | [**DealTermsNonGuaranteedAuctionTerms**](DealTermsNonGuaranteedAuctionTerms.md) |  |  [optional] |
|**nonGuaranteedFixedPriceTerms** | [**DealTermsNonGuaranteedFixedPriceTerms**](DealTermsNonGuaranteedFixedPriceTerms.md) |  |  [optional] |
|**rubiconNonGuaranteedTerms** | [**DealTermsRubiconNonGuaranteedTerms**](DealTermsRubiconNonGuaranteedTerms.md) |  |  [optional] |
|**sellerTimeZone** | **String** | For deals with Cost Per Day billing, defines the timezone used to mark the boundaries of a day (buyer-readonly) |  [optional] |



