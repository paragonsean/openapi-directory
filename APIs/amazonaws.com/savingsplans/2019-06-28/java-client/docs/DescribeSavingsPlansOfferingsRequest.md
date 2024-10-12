

# DescribeSavingsPlansOfferingsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**offeringIds** | **List&lt;String&gt;** | The IDs of the offerings. |  [optional] |
|**paymentOptions** | **List&lt;SavingsPlanPaymentOption&gt;** | The payment options. |  [optional] |
|**productType** | [**ProductTypeEnum**](#ProductTypeEnum) | The product type. |  [optional] |
|**planTypes** | **List&lt;SavingsPlanType&gt;** | The plan type. |  [optional] |
|**durations** | **List&lt;Integer&gt;** | The durations, in seconds. |  [optional] |
|**currencies** | **List&lt;CurrencyCode&gt;** | The currencies. |  [optional] |
|**descriptions** | **List&lt;String&gt;** | The descriptions. |  [optional] |
|**serviceCodes** | **List&lt;String&gt;** | The services. |  [optional] |
|**usageTypes** | **List&lt;String&gt;** | The usage details of the line item in the billing report. |  [optional] |
|**operations** | **List&lt;String&gt;** | The specific AWS operation for the line item in the billing report. |  [optional] |
|**filters** | [**List&lt;SavingsPlanOfferingFilterElement&gt;**](SavingsPlanOfferingFilterElement.md) | The filters. |  [optional] |
|**nextToken** | **String** | The token for the next page of results. |  [optional] |
|**maxResults** | **Integer** | The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value. |  [optional] |



## Enum: ProductTypeEnum

| Name | Value |
|---- | -----|
| EC2 | &quot;EC2&quot; |
| FARGATE | &quot;Fargate&quot; |
| LAMBDA | &quot;Lambda&quot; |
| SAGE_MAKER | &quot;SageMaker&quot; |



