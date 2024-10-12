# ViatorApiDocumentationAmpSpecificationMerchantPartners.Product200ResponseAllOfDataMerchantTermsAndConditionsCancellationFromTourDateInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dayRangeMax** | **Number** | **number** of days prior to the tour start date that *this* policy window begins | [optional] 
**dayRangeMin** | **Number** | **number** of days prior to the tour start date that *this* policy window ends | [optional] 
**percentageRefundable** | **Number** | **percentage** of total price refundable if cancelled within *this* time window | [optional] 
**policyEndTimestamp** | **Number** | Usually shows the Unix timestamp giving the exact time the policy ends. &#x60;null&#x60; in /product as no booking has yet been made. | [optional] 
**policyStartTimestamp** | **Number** | Usually shows the Unix timestamp giving the exact time the policy commences. &#x60;null&#x60; in /product as no booking has yet been made. | [optional] 


