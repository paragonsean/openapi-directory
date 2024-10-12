# PayRunIo.Pension2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aECompatible** | **Boolean** | The pensions&#39; a e compatible | [optional] 
**certification** | **String** | The pensions&#39; certification | [optional] 
**code** | **String** | The pensions&#39; code | [optional] 
**contributionDeductionDay** | **Number** | The pensions&#39; contribution deduction day | [optional] 
**effectiveDate** | **Date** | The pensions&#39; effective date | [optional] 
**employeeContributionCash** | **Number** | The pensions&#39; employee contribution cash | [optional] 
**employeeContributionPercent** | **Number** | The pensions&#39; employee contribution percent | [optional] 
**employerContributionCash** | **Number** | The pensions&#39; employer contribution cash | [optional] 
**employerContributionPercent** | **Number** | The pensions&#39; employer contribution percent | [optional] 
**employerNiSaving** | **Boolean** | The pensions&#39; employer ni saving | [optional] 
**employerNiSavingPercentage** | **Number** | The pensions&#39; employer ni saving percentage | [optional] 
**group** | **String** | The pensions&#39; group | [optional] 
**lowerThreshold** | **Number** | The pensions&#39; lower threshold | [optional] 
**metaData** | **Object** | The pensions&#39; meta data | [optional] 
**nextRevisionDate** | **Date** | The pensions&#39; next revision date | [optional] 
**pensionablePayCodes** | [**PensionablePayCodes**](PensionablePayCodes.md) |  | [optional] 
**proRataMethod** | **String** | The pensions&#39; pro rata method | [optional] 
**providerEmployerRef** | **String** | The pensions&#39; provider employer ref | [optional] 
**providerName** | **String** | The pensions&#39; provider name | [optional] 
**qualifyingPayCodes** | [**QualifyingPayCodes**](QualifyingPayCodes.md) |  | [optional] 
**rasRoundingOverride** | **String** | The pensions&#39; ras rounding override | [optional] 
**revision** | **Number** | The pensions&#39; revision | [optional] 
**roundingOption** | **String** | The pensions&#39; rounding option | [optional] 
**salarySacrifice** | **Boolean** | The pensions&#39; salary sacrifice | [optional] 
**schemeName** | **String** | The pensions&#39; scheme name | [optional] 
**subGroup** | **String** | The pensions&#39; sub group | [optional] 
**taxationMethod** | **String** | The pensions&#39; taxation method | [optional] 
**upperThreshold** | **Number** | The pensions&#39; upper threshold | [optional] 
**useAEThresholds** | **Boolean** | The pensions&#39; use a e thresholds | [optional] 



## Enum: CertificationEnum


* `NotSet` (value: `"NotSet"`)

* `Set1` (value: `"Set1"`)

* `Set2` (value: `"Set2"`)

* `Set3` (value: `"Set3"`)





## Enum: ProRataMethodEnum


* `NotSet` (value: `"NotSet"`)

* `Annual260Days` (value: `"Annual260Days"`)

* `Annual365Days` (value: `"Annual365Days"`)

* `AnnualQualifyingDays` (value: `"AnnualQualifyingDays"`)

* `DaysPerCalendarMonth` (value: `"DaysPerCalendarMonth"`)

* `DaysPerTaxPeriod` (value: `"DaysPerTaxPeriod"`)

* `WorkingDaysPerCalendarMonth` (value: `"WorkingDaysPerCalendarMonth"`)

* `WeekDaysPerCalendarMonth` (value: `"WeekDaysPerCalendarMonth"`)





## Enum: RasRoundingOverrideEnum


* `NotSet` (value: `"NotSet"`)

* `PennyUp` (value: `"PennyUp"`)

* `PennyDown` (value: `"PennyDown"`)

* `Bankers` (value: `"Bankers"`)

* `FiveUp` (value: `"FiveUp"`)

* `FiveDown` (value: `"FiveDown"`)

* `Floor` (value: `"Floor"`)

* `Ceiling` (value: `"Ceiling"`)





## Enum: RoundingOptionEnum


* `NotSet` (value: `"NotSet"`)

* `PennyUp` (value: `"PennyUp"`)

* `PennyDown` (value: `"PennyDown"`)

* `Bankers` (value: `"Bankers"`)

* `FiveUp` (value: `"FiveUp"`)

* `FiveDown` (value: `"FiveDown"`)

* `Floor` (value: `"Floor"`)

* `Ceiling` (value: `"Ceiling"`)





## Enum: TaxationMethodEnum


* `NotSet` (value: `"NotSet"`)

* `NetBased` (value: `"NetBased"`)

* `ReliefAtSource` (value: `"ReliefAtSource"`)

* `TaxReliefExcluded` (value: `"TaxReliefExcluded"`)




