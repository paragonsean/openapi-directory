# NaviPlanApi.ILifeInsurancePolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beneficiaryName** | **String** |  | [optional] [readonly] 
**benefitPeriod** | [**TimePeriod**](TimePeriod.md) |  | [optional] 
**cashSurrenderValue** | [**Currency**](Currency.md) |  | [optional] 
**coverageCeaseDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**dailyBenefitValue** | **Number** |  | [optional] [readonly] 
**description** | **String** |  | [optional] [readonly] 
**effectiveDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**formattedBenefitValue** | **String** |  | [optional] [readonly] 
**formattedInsuredType** | **String** |  | [optional] [readonly] 
**formattedPolicyType** | **String** |  | [optional] [readonly] 
**id** | **String** |  | [optional] [readonly] 
**insured** | **String** |  | [optional] [readonly] 
**isCSVPayableWithDeathBenefit** | [**DescriptiveBoolean**](DescriptiveBoolean.md) |  | [optional] 
**monthlyBenefitValue** | **Number** |  | [optional] [readonly] 
**ownerName** | **String** |  | [optional] [readonly] 
**policyType** | **String** |  | [optional] [readonly] 
**premiumData** | [**IInsurancePremium**](IInsurancePremium.md) |  | [optional] 
**premiumsWaivedAtDisability** | [**DescriptiveBoolean**](DescriptiveBoolean.md) |  | [optional] 
**rawBenefitValue** | **Number** |  | [optional] [readonly] 
**waitingPeriod** | [**TimePeriod**](TimePeriod.md) |  | [optional] 



## Enum: InsuredEnum


* `Client` (value: `"Client"`)

* `CoClient` (value: `"CoClient"`)

* `FirstToDie` (value: `"FirstToDie"`)

* `SecondToDie` (value: `"SecondToDie"`)

* `Other` (value: `"Other"`)





## Enum: PolicyTypeEnum


* `WholeLife` (value: `"WholeLife"`)

* `UniversalLife` (value: `"UniversalLife"`)

* `Term1Life` (value: `"Term1Life"`)

* `Term5Life` (value: `"Term5Life"`)

* `Term10Life` (value: `"Term10Life"`)

* `Term20Life` (value: `"Term20Life"`)

* `Term100Life` (value: `"Term100Life"`)

* `VariableLife` (value: `"VariableLife"`)

* `VariableUniversalLife` (value: `"VariableUniversalLife"`)

* `GroupLongTermDisability` (value: `"GroupLongTermDisability"`)

* `GroupShortTermDisability` (value: `"GroupShortTermDisability"`)

* `IndividualDisability` (value: `"IndividualDisability"`)

* `LongTermCare` (value: `"LongTermCare"`)

* `CriticalIllness` (value: `"CriticalIllness"`)

* `MedicalCoveragePlan` (value: `"MedicalCoveragePlan"`)

* `CashToInsuredCoverage` (value: `"CashToInsuredCoverage"`)




