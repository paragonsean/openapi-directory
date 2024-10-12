

# DescribeSavingsPlansOfferingRatesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**savingsPlanOfferingIds** | **List&lt;String&gt;** | The IDs of the offerings. |  [optional] |
|**savingsPlanPaymentOptions** | **List&lt;SavingsPlanPaymentOption&gt;** | The payment options. |  [optional] |
|**savingsPlanTypes** | **List&lt;SavingsPlanType&gt;** | The plan types. |  [optional] |
|**products** | **List&lt;SavingsPlanProductType&gt;** | The AWS products. |  [optional] |
|**serviceCodes** | **List&lt;SavingsPlanRateServiceCode&gt;** | The services. |  [optional] |
|**usageTypes** | **List&lt;String&gt;** | The usage details of the line item in the billing report. |  [optional] |
|**operations** | **List&lt;String&gt;** | The specific AWS operation for the line item in the billing report. |  [optional] |
|**filters** | [**List&lt;SavingsPlanOfferingRateFilterElement&gt;**](SavingsPlanOfferingRateFilterElement.md) | The filters. |  [optional] |
|**nextToken** | **String** | The token for the next page of results. |  [optional] |
|**maxResults** | **Integer** | The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value. |  [optional] |



