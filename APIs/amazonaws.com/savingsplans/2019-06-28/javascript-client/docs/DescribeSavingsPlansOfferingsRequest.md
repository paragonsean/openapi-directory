# AwsSavingsPlans.DescribeSavingsPlansOfferingsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offeringIds** | **[String]** | The IDs of the offerings. | [optional] 
**paymentOptions** | [**[SavingsPlanPaymentOption]**](SavingsPlanPaymentOption.md) | The payment options. | [optional] 
**productType** | **String** | The product type. | [optional] 
**planTypes** | [**[SavingsPlanType]**](SavingsPlanType.md) | The plan type. | [optional] 
**durations** | **[Number]** | The durations, in seconds. | [optional] 
**currencies** | [**[CurrencyCode]**](CurrencyCode.md) | The currencies. | [optional] 
**descriptions** | **[String]** | The descriptions. | [optional] 
**serviceCodes** | **[String]** | The services. | [optional] 
**usageTypes** | **[String]** | The usage details of the line item in the billing report. | [optional] 
**operations** | **[String]** | The specific AWS operation for the line item in the billing report. | [optional] 
**filters** | [**[SavingsPlanOfferingFilterElement]**](SavingsPlanOfferingFilterElement.md) | The filters. | [optional] 
**nextToken** | **String** | The token for the next page of results. | [optional] 
**maxResults** | **Number** | The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value. | [optional] 



## Enum: ProductTypeEnum


* `EC2` (value: `"EC2"`)

* `Fargate` (value: `"Fargate"`)

* `Lambda` (value: `"Lambda"`)

* `SageMaker` (value: `"SageMaker"`)




