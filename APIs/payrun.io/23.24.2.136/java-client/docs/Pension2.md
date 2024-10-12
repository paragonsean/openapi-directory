

# Pension2


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aeCompatible** | **Boolean** | The pensions&#39; a e compatible |  [optional] |
|**certification** | [**CertificationEnum**](#CertificationEnum) | The pensions&#39; certification |  [optional] |
|**code** | **String** | The pensions&#39; code |  [optional] |
|**contributionDeductionDay** | **Integer** | The pensions&#39; contribution deduction day |  [optional] |
|**effectiveDate** | **LocalDate** | The pensions&#39; effective date |  [optional] |
|**employeeContributionCash** | **Double** | The pensions&#39; employee contribution cash |  [optional] |
|**employeeContributionPercent** | **Double** | The pensions&#39; employee contribution percent |  [optional] |
|**employerContributionCash** | **Double** | The pensions&#39; employer contribution cash |  [optional] |
|**employerContributionPercent** | **Double** | The pensions&#39; employer contribution percent |  [optional] |
|**employerNiSaving** | **Boolean** | The pensions&#39; employer ni saving |  [optional] |
|**employerNiSavingPercentage** | **Double** | The pensions&#39; employer ni saving percentage |  [optional] |
|**group** | **String** | The pensions&#39; group |  [optional] |
|**lowerThreshold** | **Double** | The pensions&#39; lower threshold |  [optional] |
|**metaData** | **Object** | The pensions&#39; meta data |  [optional] |
|**nextRevisionDate** | **LocalDate** | The pensions&#39; next revision date |  [optional] |
|**pensionablePayCodes** | [**PensionablePayCodes**](PensionablePayCodes.md) |  |  [optional] |
|**proRataMethod** | [**ProRataMethodEnum**](#ProRataMethodEnum) | The pensions&#39; pro rata method |  [optional] |
|**providerEmployerRef** | **String** | The pensions&#39; provider employer ref |  [optional] |
|**providerName** | **String** | The pensions&#39; provider name |  [optional] |
|**qualifyingPayCodes** | [**QualifyingPayCodes**](QualifyingPayCodes.md) |  |  [optional] |
|**rasRoundingOverride** | [**RasRoundingOverrideEnum**](#RasRoundingOverrideEnum) | The pensions&#39; ras rounding override |  [optional] |
|**revision** | **Integer** | The pensions&#39; revision |  [optional] |
|**roundingOption** | [**RoundingOptionEnum**](#RoundingOptionEnum) | The pensions&#39; rounding option |  [optional] |
|**salarySacrifice** | **Boolean** | The pensions&#39; salary sacrifice |  [optional] |
|**schemeName** | **String** | The pensions&#39; scheme name |  [optional] |
|**subGroup** | **String** | The pensions&#39; sub group |  [optional] |
|**taxationMethod** | [**TaxationMethodEnum**](#TaxationMethodEnum) | The pensions&#39; taxation method |  [optional] |
|**upperThreshold** | **Double** | The pensions&#39; upper threshold |  [optional] |
|**useAEThresholds** | **Boolean** | The pensions&#39; use a e thresholds |  [optional] |



## Enum: CertificationEnum

| Name | Value |
|---- | -----|
| NOT_SET | &quot;NotSet&quot; |
| SET1 | &quot;Set1&quot; |
| SET2 | &quot;Set2&quot; |
| SET3 | &quot;Set3&quot; |



## Enum: ProRataMethodEnum

| Name | Value |
|---- | -----|
| NOT_SET | &quot;NotSet&quot; |
| ANNUAL260_DAYS | &quot;Annual260Days&quot; |
| ANNUAL365_DAYS | &quot;Annual365Days&quot; |
| ANNUAL_QUALIFYING_DAYS | &quot;AnnualQualifyingDays&quot; |
| DAYS_PER_CALENDAR_MONTH | &quot;DaysPerCalendarMonth&quot; |
| DAYS_PER_TAX_PERIOD | &quot;DaysPerTaxPeriod&quot; |
| WORKING_DAYS_PER_CALENDAR_MONTH | &quot;WorkingDaysPerCalendarMonth&quot; |
| WEEK_DAYS_PER_CALENDAR_MONTH | &quot;WeekDaysPerCalendarMonth&quot; |



## Enum: RasRoundingOverrideEnum

| Name | Value |
|---- | -----|
| NOT_SET | &quot;NotSet&quot; |
| PENNY_UP | &quot;PennyUp&quot; |
| PENNY_DOWN | &quot;PennyDown&quot; |
| BANKERS | &quot;Bankers&quot; |
| FIVE_UP | &quot;FiveUp&quot; |
| FIVE_DOWN | &quot;FiveDown&quot; |
| FLOOR | &quot;Floor&quot; |
| CEILING | &quot;Ceiling&quot; |



## Enum: RoundingOptionEnum

| Name | Value |
|---- | -----|
| NOT_SET | &quot;NotSet&quot; |
| PENNY_UP | &quot;PennyUp&quot; |
| PENNY_DOWN | &quot;PennyDown&quot; |
| BANKERS | &quot;Bankers&quot; |
| FIVE_UP | &quot;FiveUp&quot; |
| FIVE_DOWN | &quot;FiveDown&quot; |
| FLOOR | &quot;Floor&quot; |
| CEILING | &quot;Ceiling&quot; |



## Enum: TaxationMethodEnum

| Name | Value |
|---- | -----|
| NOT_SET | &quot;NotSet&quot; |
| NET_BASED | &quot;NetBased&quot; |
| RELIEF_AT_SOURCE | &quot;ReliefAtSource&quot; |
| TAX_RELIEF_EXCLUDED | &quot;TaxReliefExcluded&quot; |



