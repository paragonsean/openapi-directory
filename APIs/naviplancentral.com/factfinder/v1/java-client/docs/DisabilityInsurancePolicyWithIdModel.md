

# DisabilityInsurancePolicyWithIdModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**benefit** | **Double** |  |  [optional] |
|**benefitFrequency** | **Integer** |  |  [optional] |
|**benefitType** | [**BenefitTypeEnum**](#BenefitTypeEnum) |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**externalDestinationId** | **String** |  |  [optional] |
|**factFinderId** | **Integer** |  |  [optional] |
|**insurancePolicyId** | **Integer** |  |  [optional] |
|**insured** | [**InsuredEnum**](#InsuredEnum) |  |  [optional] |
|**links** | [**List&lt;ObjectLink&gt;**](ObjectLink.md) |  |  [optional] |
|**policyType** | **Integer** |  |  [optional] |
|**premium** | **Double** |  |  [optional] |
|**premiumFrequency** | **Integer** |  |  [optional] |



## Enum: BenefitTypeEnum

| Name | Value |
|---- | -----|
| DOLLAR | &quot;Dollar&quot; |
| PERCENT | &quot;Percent&quot; |



## Enum: InsuredEnum

| Name | Value |
|---- | -----|
| CLIENT | &quot;Client&quot; |
| CO_CLIENT | &quot;CoClient&quot; |



