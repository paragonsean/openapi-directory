

# Employee2


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aeAssessmentOverride** | [**AeAssessmentOverrideEnum**](#AeAssessmentOverrideEnum) | The employees&#39; a e assessment override |  [optional] |
|**aeAssessmentOverrideDate** | **LocalDate** | The employees&#39; a e assessment override date |  [optional] |
|**aeExclusionReasonCode** | [**AeExclusionReasonCodeEnum**](#AeExclusionReasonCodeEnum) | The employees&#39; a e exclusion reason code |  [optional] |
|**aePostponementDate** | **LocalDate** | The employees&#39; a e postponement date |  [optional] |
|**address** | [**Address**](Address.md) |  |  [optional] |
|**bankAccount** | [**BankAccount**](BankAccount.md) |  |  [optional] |
|**code** | **String** | The employees&#39; code |  [optional] |
|**dateOfBirth** | **LocalDate** | The employees&#39; date of birth |  [optional] |
|**deactivated** | **Boolean** | The employees&#39; deactivated |  [optional] |
|**directorshipAppointmentDate** | **LocalDate** | The employees&#39; directorship appointment date |  [optional] |
|**eeACitizen** | **Boolean** | The employees&#39; e e a citizen |  [optional] |
|**EPM6** | **Boolean** | The employees&#39; e p m6 |  [optional] |
|**effectiveDate** | **LocalDate** | The employees&#39; effective date |  [optional] |
|**employeePartner** | [**EmployeePartner**](EmployeePartner.md) |  |  [optional] |
|**firstName** | **String** | The employees&#39; the first name |  [optional] |
|**gender** | [**GenderEnum**](#GenderEnum) | The employees&#39; gender |  [optional] |
|**hoursPerWeek** | **Double** | The employees&#39; hours per week |  [optional] |
|**initials** | **String** | The employees&#39; initials |  [optional] |
|**irregularEmployment** | **Boolean** | The employees&#39; irregular employment |  [optional] |
|**isAgencyWorker** | **Boolean** | The employees&#39; is agency worker |  [optional] |
|**lastName** | **String** | The employees&#39; last name |  [optional] |
|**leaverReason** | [**LeaverReasonEnum**](#LeaverReasonEnum) | The employees&#39; leaver reason |  [optional] |
|**leavingDate** | **LocalDate** | The employees&#39; leaving date |  [optional] |
|**maritalStatus** | [**MaritalStatusEnum**](#MaritalStatusEnum) | The employees&#39; marital status |  [optional] |
|**metaData** | **Object** | The employees&#39; meta data |  [optional] |
|**middleName** | **String** | The employees&#39; middle name |  [optional] |
|**nextRevisionDate** | **LocalDate** | The employees&#39; next revision date |  [optional] |
|**niNumber** | **String** | The employees&#39; ni number |  [optional] |
|**nicLiability** | [**NicLiabilityEnum**](#NicLiabilityEnum) | The employees&#39; nic liability |  [optional] |
|**offPayrollWorker** | **Boolean** | The employees&#39; off payroll worker |  [optional] |
|**onStrike** | **Boolean** | The employees&#39; on strike |  [optional] |
|**p45IssuedDate** | **LocalDate** | The employees&#39; p45 issued date |  [optional] |
|**passportNumber** | **String** | The employees&#39; passport number |  [optional] |
|**paySchedule** | [**PaySchedule1**](PaySchedule1.md) |  |  [optional] |
|**paymentMethod** | [**PaymentMethodEnum**](#PaymentMethodEnum) | The employees&#39; payment method |  [optional] |
|**paymentToANonIndividual** | **Boolean** | The employees&#39; payment to a non individual |  [optional] |
|**region** | [**RegionEnum**](#RegionEnum) | The employees&#39; region |  [optional] |
|**revision** | **Integer** | The employees&#39; revision |  [optional] |
|**ruleExclusions** | [**RuleExclusionsEnum**](#RuleExclusionsEnum) | The employees&#39; rule exclusions |  [optional] |
|**seconded** | [**SecondedEnum**](#SecondedEnum) | The employees&#39; seconded |  [optional] |
|**startDate** | **LocalDate** | The employees&#39; start date |  [optional] |
|**starterDeclaration** | [**StarterDeclarationEnum**](#StarterDeclarationEnum) | The employees&#39; starter declaration |  [optional] |
|**territory** | [**TerritoryEnum**](#TerritoryEnum) | The employees&#39; territory |  [optional] |
|**title** | **String** | The employees&#39; title |  [optional] |
|**veteranPeriodStartDate** | **LocalDate** | The employees&#39; veteran period start date |  [optional] |
|**workingWeek** | [**WorkingWeekEnum**](#WorkingWeekEnum) | The employees&#39; working week |  [optional] |



## Enum: AeAssessmentOverrideEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| OPT_OUT | &quot;OptOut&quot; |
| OPT_IN | &quot;OptIn&quot; |
| VOLUNTARY_JOINER | &quot;VoluntaryJoiner&quot; |
| CONTRACTUAL_PENSION | &quot;ContractualPension&quot; |
| CEASED_MEMBERSHIP | &quot;CeasedMembership&quot; |
| LEAVER | &quot;Leaver&quot; |
| EXCLUDED | &quot;Excluded&quot; |



## Enum: AeExclusionReasonCodeEnum

| Name | Value |
|---- | -----|
| OTHER_NOT_KNOWN | &quot;OtherNotKnown&quot; |
| NOT_A_WORKER | &quot;NotAWorker&quot; |
| NOT_UK_WORKER | &quot;NotUKWorker&quot; |
| TEMPORARY_UK_WORKER | &quot;TemporaryUKWorker&quot; |
| OUTSIDE_AGE_RANGE | &quot;OutsideAgeRange&quot; |
| SINGLE_EMPLOYEE_DIRECTOR | &quot;SingleEmployeeDirector&quot; |
| CEASED_MEMBERSHIP_WITHIN12_MONTHS | &quot;CeasedMembershipWithin12Months&quot; |
| CEASED_MEMBERSHIP_BEYOND12_MONTHS | &quot;CeasedMembershipBeyond12Months&quot; |
| WORKER_WULS_WITHIN12_MONTH | &quot;WorkerWULSWithin12Month&quot; |
| WORKER_WULS_BEYOND12_MONTH | &quot;WorkerWULSBeyond12Month&quot; |
| WORKER_IN_NOTICE_PERIOD | &quot;WorkerInNoticePeriod&quot; |
| WORKER_TAX_PROTECTION | &quot;WorkerTaxProtection&quot; |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| MALE | &quot;Male&quot; |
| FEMALE | &quot;Female&quot; |



## Enum: LeaverReasonEnum

| Name | Value |
|---- | -----|
| RESIGNED | &quot;Resigned&quot; |
| DISMISSED | &quot;Dismissed&quot; |
| REDUNDANT | &quot;Redundant&quot; |
| RETIRED | &quot;Retired&quot; |
| DECEASED | &quot;Deceased&quot; |
| LEGAL_CUSTODY | &quot;LegalCustody&quot; |
| OTHER | &quot;Other&quot; |



## Enum: MaritalStatusEnum

| Name | Value |
|---- | -----|
| NOT_SET | &quot;NotSet&quot; |
| SINGLE | &quot;Single&quot; |
| MARRIED | &quot;Married&quot; |
| DIVORCED | &quot;Divorced&quot; |
| WIDOWED | &quot;Widowed&quot; |



## Enum: NicLiabilityEnum

| Name | Value |
|---- | -----|
| HAS_OTHER_JOB | &quot;HasOtherJob&quot; |
| IS_FEMALE_ENTITLED_TO_REDUCED_RATE | &quot;IsFemaleEntitledToReducedRate&quot; |
| IS_NOT_LIABLE | &quot;IsNotLiable&quot; |
| IS_CONTRACTED_OUT | &quot;IsContractedOut&quot; |
| IS_FULLY_LIABLE | &quot;IsFullyLiable&quot; |
| IS_APPRENTICE | &quot;IsApprentice&quot; |
| LEAVER_BEYOND6_WEEKS | &quot;LeaverBeyond6Weeks&quot; |
| PAYMENT_AFTER_LEAVING_IRREGULAR | &quot;PaymentAfterLeavingIrregular&quot; |
| IS_FREE_PORT_WORKER | &quot;IsFreePortWorker&quot; |
| IS_NOT_LIABLE_FOR_EMPLOYER_NI | &quot;IsNotLiableForEmployerNi&quot; |



## Enum: PaymentMethodEnum

| Name | Value |
|---- | -----|
| NOT_SET | &quot;NotSet&quot; |
| CASH | &quot;Cash&quot; |
| CHEQUE | &quot;Cheque&quot; |
| BACS | &quot;BACS&quot; |
| FASTER_PAYMENTS | &quot;FasterPayments&quot; |
| OTHER | &quot;Other&quot; |



## Enum: RegionEnum

| Name | Value |
|---- | -----|
| NOT_SET | &quot;NotSet&quot; |
| ENGLAND | &quot;England&quot; |
| SCOTLAND | &quot;Scotland&quot; |
| WALES | &quot;Wales&quot; |



## Enum: RuleExclusionsEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| NI_MISSING_PAY_INSTRUCTION_RULE | &quot;NiMissingPayInstructionRule&quot; |
| TAX_MISSING_PAY_INSTRUCTION_RULE | &quot;TaxMissingPayInstructionRule&quot; |
| TAX_CODE_UPLIFT_RULE | &quot;TaxCodeUpliftRule&quot; |
| NI_SET_EXPECTED_LETTER_RULE | &quot;NiSetExpectedLetterRule&quot; |
| NI_DATE_OF_BIRTH_CHANGE_RETROSPECTIVE_C_RULE | &quot;NiDateOfBirthChangeRetrospectiveCRule&quot; |
| NI_DEFERMENT_STATUS_CHANGE_RULE | &quot;NiDefermentStatusChangeRule&quot; |
| NI_END_CONTRACTED_OUT_TRANSFER_RULE | &quot;NiEndContractedOutTransferRule&quot; |
| PAYMENT_AFTER_LEAVING_TAX_CODE_RULE | &quot;PaymentAfterLeavingTaxCodeRule&quot; |
| LEAVER_END_INSTRUCTIONS_RULE | &quot;LeaverEndInstructionsRule&quot; |
| P45_STUDENT_LOAN_INSTRUCTION_RULE | &quot;P45StudentLoanInstructionRule&quot; |
| P45_TAX_INSTRUCTION_RULE | &quot;P45TaxInstructionRule&quot; |
| P45_YTD_TAX_RULE | &quot;P45YtdTaxRule&quot; |
| YTD_INSTRUCTION_RULE | &quot;YtdInstructionRule&quot; |
| TAX_CODE_REGION_CHANGE_RULE | &quot;TaxCodeRegionChangeRule&quot; |
| AUTO_ENROLMENT_STATUS_CHANGE_RULE | &quot;AutoEnrolmentStatusChangeRule&quot; |
| EMPLOYEE_DECEASED_RULE | &quot;EmployeeDeceasedRule&quot; |
| BENEFIT_INSTRUCTION_AUTO_END_RULE | &quot;BenefitInstructionAutoEndRule&quot; |



## Enum: SecondedEnum

| Name | Value |
|---- | -----|
| NOT_SET | &quot;NotSet&quot; |
| STAY183_DAYS_OR_MORE | &quot;Stay183DaysOrMore&quot; |
| STAY_LESS_THAN183_DAYS | &quot;StayLessThan183Days&quot; |
| IN_OUT_UK | &quot;InOutUk&quot; |



## Enum: StarterDeclarationEnum

| Name | Value |
|---- | -----|
| PREVIOUSLY_REPORTED | &quot;PreviouslyReported&quot; |
| A | &quot;A&quot; |
| B | &quot;B&quot; |
| C | &quot;C&quot; |



## Enum: TerritoryEnum

| Name | Value |
|---- | -----|
| UNITED_KINGDOM | &quot;UnitedKingdom&quot; |



## Enum: WorkingWeekEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| MONDAY | &quot;Monday&quot; |
| TUESDAY | &quot;Tuesday&quot; |
| WEDNESDAY | &quot;Wednesday&quot; |
| THURSDAY | &quot;Thursday&quot; |
| FRIDAY | &quot;Friday&quot; |
| ALL_WEEK_DAYS | &quot;AllWeekDays&quot; |
| SATURDAY | &quot;Saturday&quot; |
| SUNDAY | &quot;Sunday&quot; |
| ALL_DAYS | &quot;AllDays&quot; |



