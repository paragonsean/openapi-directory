

# LifeInsurancePolicyModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**beneficiary** | [**BeneficiaryEnum**](#BeneficiaryEnum) |  |  [optional] |
|**beneficiaryDependentId** | **Integer** |  |  [optional] |
|**benefit** | **Double** |  |  [optional] |
|**description** | **String** |  |  |
|**externalDestinationId** | **String** |  |  [optional] |
|**factFinderId** | **Integer** |  |  |
|**frequency** | **Integer** |  |  [optional] |
|**generalAccountMarketValue** | **Double** |  |  [optional] |
|**insured** | [**InsuredEnum**](#InsuredEnum) |  |  [optional] |
|**payer** | [**PayerEnum**](#PayerEnum) |  |  [optional] |
|**policyType** | **Integer** |  |  [optional] |
|**premium** | **Double** |  |  [optional] |



## Enum: BeneficiaryEnum

| Name | Value |
|---- | -----|
| CLIENT | &quot;Client&quot; |
| CO_CLIENT | &quot;CoClient&quot; |
| DEPENDENT | &quot;Dependent&quot; |
| OTHER | &quot;Other&quot; |



## Enum: InsuredEnum

| Name | Value |
|---- | -----|
| CLIENT | &quot;Client&quot; |
| CO_CLIENT | &quot;CoClient&quot; |
| FIRST_TO_DIE | &quot;FirstToDie&quot; |
| SECOND_TO_DIE | &quot;SecondToDie&quot; |
| OTHER | &quot;Other&quot; |



## Enum: PayerEnum

| Name | Value |
|---- | -----|
| CLIENT | &quot;Client&quot; |
| CO_CLIENT | &quot;CoClient&quot; |
| JOINT | &quot;Joint&quot; |
| OTHER | &quot;Other&quot; |



