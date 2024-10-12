

# ILifeInsurancePolicy


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**beneficiaryName** | **String** |  |  [optional] [readonly] |
|**benefitPeriod** | [**TimePeriod**](TimePeriod.md) |  |  [optional] |
|**cashSurrenderValue** | [**Currency**](Currency.md) |  |  [optional] |
|**coverageCeaseDate** | [**Date**](Date.md) |  |  [optional] |
|**dailyBenefitValue** | **Double** |  |  [optional] [readonly] |
|**description** | **String** |  |  [optional] [readonly] |
|**effectiveDate** | [**Date**](Date.md) |  |  [optional] |
|**formattedBenefitValue** | **String** |  |  [optional] [readonly] |
|**formattedInsuredType** | **String** |  |  [optional] [readonly] |
|**formattedPolicyType** | **String** |  |  [optional] [readonly] |
|**id** | **String** |  |  [optional] [readonly] |
|**insured** | [**InsuredEnum**](#InsuredEnum) |  |  [optional] [readonly] |
|**isCSVPayableWithDeathBenefit** | [**DescriptiveBoolean**](DescriptiveBoolean.md) |  |  [optional] |
|**monthlyBenefitValue** | **Double** |  |  [optional] [readonly] |
|**ownerName** | **String** |  |  [optional] [readonly] |
|**policyType** | [**PolicyTypeEnum**](#PolicyTypeEnum) |  |  [optional] [readonly] |
|**premiumData** | [**IInsurancePremium**](IInsurancePremium.md) |  |  [optional] |
|**premiumsWaivedAtDisability** | [**DescriptiveBoolean**](DescriptiveBoolean.md) |  |  [optional] |
|**rawBenefitValue** | **Double** |  |  [optional] [readonly] |
|**waitingPeriod** | [**TimePeriod**](TimePeriod.md) |  |  [optional] |



## Enum: InsuredEnum

| Name | Value |
|---- | -----|
| CLIENT | &quot;Client&quot; |
| CO_CLIENT | &quot;CoClient&quot; |
| FIRST_TO_DIE | &quot;FirstToDie&quot; |
| SECOND_TO_DIE | &quot;SecondToDie&quot; |
| OTHER | &quot;Other&quot; |



## Enum: PolicyTypeEnum

| Name | Value |
|---- | -----|
| WHOLE_LIFE | &quot;WholeLife&quot; |
| UNIVERSAL_LIFE | &quot;UniversalLife&quot; |
| TERM1_LIFE | &quot;Term1Life&quot; |
| TERM5_LIFE | &quot;Term5Life&quot; |
| TERM10_LIFE | &quot;Term10Life&quot; |
| TERM20_LIFE | &quot;Term20Life&quot; |
| TERM100_LIFE | &quot;Term100Life&quot; |
| VARIABLE_LIFE | &quot;VariableLife&quot; |
| VARIABLE_UNIVERSAL_LIFE | &quot;VariableUniversalLife&quot; |
| GROUP_LONG_TERM_DISABILITY | &quot;GroupLongTermDisability&quot; |
| GROUP_SHORT_TERM_DISABILITY | &quot;GroupShortTermDisability&quot; |
| INDIVIDUAL_DISABILITY | &quot;IndividualDisability&quot; |
| LONG_TERM_CARE | &quot;LongTermCare&quot; |
| CRITICAL_ILLNESS | &quot;CriticalIllness&quot; |
| MEDICAL_COVERAGE_PLAN | &quot;MedicalCoveragePlan&quot; |
| CASH_TO_INSURED_COVERAGE | &quot;CashToInsuredCoverage&quot; |



