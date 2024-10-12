

# IDisabilityInsurancePolicyDomainObject


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**benefit** | **Double** |  |  [optional] |
|**benefitFrequency** | **Integer** |  |  [optional] |
|**benefitType** | [**BenefitTypeEnum**](#BenefitTypeEnum) |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**disabilityInsurancePolicyId** | **Integer** |  |  [optional] |
|**externalDestinationId** | **String** |  |  [optional] |
|**factFinderId** | **Integer** |  |  [optional] |
|**insured** | [**InsuredEnum**](#InsuredEnum) |  |  [optional] |
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



