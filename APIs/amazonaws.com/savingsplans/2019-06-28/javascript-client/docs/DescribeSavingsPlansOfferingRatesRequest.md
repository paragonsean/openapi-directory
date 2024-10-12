# AwsSavingsPlans.DescribeSavingsPlansOfferingRatesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**savingsPlanOfferingIds** | **[String]** | The IDs of the offerings. | [optional] 
**savingsPlanPaymentOptions** | [**[SavingsPlanPaymentOption]**](SavingsPlanPaymentOption.md) | The payment options. | [optional] 
**savingsPlanTypes** | [**[SavingsPlanType]**](SavingsPlanType.md) | The plan types. | [optional] 
**products** | [**[SavingsPlanProductType]**](SavingsPlanProductType.md) | The AWS products. | [optional] 
**serviceCodes** | [**[SavingsPlanRateServiceCode]**](SavingsPlanRateServiceCode.md) | The services. | [optional] 
**usageTypes** | **[String]** | The usage details of the line item in the billing report. | [optional] 
**operations** | **[String]** | The specific AWS operation for the line item in the billing report. | [optional] 
**filters** | [**[SavingsPlanOfferingRateFilterElement]**](SavingsPlanOfferingRateFilterElement.md) | The filters. | [optional] 
**nextToken** | **String** | The token for the next page of results. | [optional] 
**maxResults** | **Number** | The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value. | [optional] 


