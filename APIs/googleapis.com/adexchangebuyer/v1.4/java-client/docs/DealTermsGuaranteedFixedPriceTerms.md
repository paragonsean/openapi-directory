

# DealTermsGuaranteedFixedPriceTerms


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingInfo** | [**DealTermsGuaranteedFixedPriceTermsBillingInfo**](DealTermsGuaranteedFixedPriceTermsBillingInfo.md) |  |  [optional] |
|**fixedPrices** | [**List&lt;PricePerBuyer&gt;**](PricePerBuyer.md) | Fixed price for the specified buyer. |  [optional] |
|**guaranteedImpressions** | **String** | Guaranteed impressions as a percentage. This is the percentage of guaranteed looks that the buyer is guaranteeing to buy. |  [optional] |
|**guaranteedLooks** | **String** | Count of guaranteed looks. Required for deal, optional for product. For CPD deals, buyer changes to guaranteed_looks will be ignored. |  [optional] |
|**minimumDailyLooks** | **String** | Count of minimum daily looks for a CPD deal. For CPD deals, buyer should negotiate on this field instead of guaranteed_looks. |  [optional] |



