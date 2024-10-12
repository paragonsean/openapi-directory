# AdExchangeBuyerApi.DealTermsGuaranteedFixedPriceTermsBillingInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currencyConversionTimeMs** | **String** | The timestamp (in ms since epoch) when the original reservation price for the deal was first converted to DFP currency. This is used to convert the contracted price into buyer&#39;s currency without discrepancy. | [optional] 
**dfpLineItemId** | **String** | The DFP line item id associated with this deal. For features like CPD, buyers can retrieve the DFP line item for billing reconciliation. | [optional] 
**originalContractedQuantity** | **String** | The original contracted quantity (# impressions) for this deal. To ensure delivery, sometimes the publisher will book the deal with a impression buffer, such that guaranteed_looks is greater than the contracted quantity. However clients are billed using the original contracted quantity. | [optional] 
**price** | [**Price**](Price.md) |  | [optional] 


