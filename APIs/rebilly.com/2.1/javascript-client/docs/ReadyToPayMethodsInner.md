# RebillyRestApi.ReadyToPayMethodsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brands** | [**[PaymentCardBrand]**](PaymentCardBrand.md) | The list of supported brands. | [optional] 
**feature** | [**ReadyToPayAchMethodFeature**](ReadyToPayAchMethodFeature.md) |  | [optional] 
**filters** | **[String]** | For the method to be applicable any of the following filters should match. If no filters sent – no restrictions applied. This follows our standard filter format.  | [optional] 
**method** | [**AlternativePaymentMethods**](AlternativePaymentMethods.md) | The payment method. | 


