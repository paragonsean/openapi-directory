# ViatorApiDocumentationAmpSpecificationMerchantPartners.MerchantCancellationRequestCancelItemsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelCode** | **String** | **cancellation code** that describes the reason for the cancellation - see: [Suggested cancellation codes](#suggested-cancellation-codes)  | [optional] 
**cancelDescription** | **String** | **natural-language description** of the reason for cancellation (a reason must be provided if &#x60;cancelCode&#x60; is &#x60;62&#x60; or &#x60;66&#x60;) | [optional] 
**distributorItemRef** | **String** | **alphanumeric reference code** of the distributor item | [optional] 
**itemId** | **Number** | **numeric identifier** of item to cancel in itinerary | [optional] 


