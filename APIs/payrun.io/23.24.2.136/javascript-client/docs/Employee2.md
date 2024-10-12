# PayRunIo.Employee2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aEAssessmentOverride** | **String** | The employees&#39; a e assessment override | [optional] 
**aEAssessmentOverrideDate** | **Date** | The employees&#39; a e assessment override date | [optional] 
**aEExclusionReasonCode** | **String** | The employees&#39; a e exclusion reason code | [optional] 
**aEPostponementDate** | **Date** | The employees&#39; a e postponement date | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**bankAccount** | [**BankAccount**](BankAccount.md) |  | [optional] 
**code** | **String** | The employees&#39; code | [optional] 
**dateOfBirth** | **Date** | The employees&#39; date of birth | [optional] 
**deactivated** | **Boolean** | The employees&#39; deactivated | [optional] 
**directorshipAppointmentDate** | **Date** | The employees&#39; directorship appointment date | [optional] 
**eEACitizen** | **Boolean** | The employees&#39; e e a citizen | [optional] 
**ePM6** | **Boolean** | The employees&#39; e p m6 | [optional] 
**effectiveDate** | **Date** | The employees&#39; effective date | [optional] 
**employeePartner** | [**EmployeePartner**](EmployeePartner.md) |  | [optional] 
**firstName** | **String** | The employees&#39; the first name | [optional] 
**gender** | **String** | The employees&#39; gender | [optional] 
**hoursPerWeek** | **Number** | The employees&#39; hours per week | [optional] 
**initials** | **String** | The employees&#39; initials | [optional] 
**irregularEmployment** | **Boolean** | The employees&#39; irregular employment | [optional] 
**isAgencyWorker** | **Boolean** | The employees&#39; is agency worker | [optional] 
**lastName** | **String** | The employees&#39; last name | [optional] 
**leaverReason** | **String** | The employees&#39; leaver reason | [optional] 
**leavingDate** | **Date** | The employees&#39; leaving date | [optional] 
**maritalStatus** | **String** | The employees&#39; marital status | [optional] 
**metaData** | **Object** | The employees&#39; meta data | [optional] 
**middleName** | **String** | The employees&#39; middle name | [optional] 
**nextRevisionDate** | **Date** | The employees&#39; next revision date | [optional] 
**niNumber** | **String** | The employees&#39; ni number | [optional] 
**nicLiability** | **String** | The employees&#39; nic liability | [optional] 
**offPayrollWorker** | **Boolean** | The employees&#39; off payroll worker | [optional] 
**onStrike** | **Boolean** | The employees&#39; on strike | [optional] 
**p45IssuedDate** | **Date** | The employees&#39; p45 issued date | [optional] 
**passportNumber** | **String** | The employees&#39; passport number | [optional] 
**paySchedule** | [**PaySchedule1**](PaySchedule1.md) |  | [optional] 
**paymentMethod** | **String** | The employees&#39; payment method | [optional] 
**paymentToANonIndividual** | **Boolean** | The employees&#39; payment to a non individual | [optional] 
**region** | **String** | The employees&#39; region | [optional] 
**revision** | **Number** | The employees&#39; revision | [optional] 
**ruleExclusions** | **String** | The employees&#39; rule exclusions | [optional] 
**seconded** | **String** | The employees&#39; seconded | [optional] 
**startDate** | **Date** | The employees&#39; start date | [optional] 
**starterDeclaration** | **String** | The employees&#39; starter declaration | [optional] 
**territory** | **String** | The employees&#39; territory | [optional] 
**title** | **String** | The employees&#39; title | [optional] 
**veteranPeriodStartDate** | **Date** | The employees&#39; veteran period start date | [optional] 
**workingWeek** | **String** | The employees&#39; working week | [optional] 



## Enum: AEAssessmentOverrideEnum


* `None` (value: `"None"`)

* `OptOut` (value: `"OptOut"`)

* `OptIn` (value: `"OptIn"`)

* `VoluntaryJoiner` (value: `"VoluntaryJoiner"`)

* `ContractualPension` (value: `"ContractualPension"`)

* `CeasedMembership` (value: `"CeasedMembership"`)

* `Leaver` (value: `"Leaver"`)

* `Excluded` (value: `"Excluded"`)





## Enum: AEExclusionReasonCodeEnum


* `OtherNotKnown` (value: `"OtherNotKnown"`)

* `NotAWorker` (value: `"NotAWorker"`)

* `NotUKWorker` (value: `"NotUKWorker"`)

* `TemporaryUKWorker` (value: `"TemporaryUKWorker"`)

* `OutsideAgeRange` (value: `"OutsideAgeRange"`)

* `SingleEmployeeDirector` (value: `"SingleEmployeeDirector"`)

* `CeasedMembershipWithin12Months` (value: `"CeasedMembershipWithin12Months"`)

* `CeasedMembershipBeyond12Months` (value: `"CeasedMembershipBeyond12Months"`)

* `WorkerWULSWithin12Month` (value: `"WorkerWULSWithin12Month"`)

* `WorkerWULSBeyond12Month` (value: `"WorkerWULSBeyond12Month"`)

* `WorkerInNoticePeriod` (value: `"WorkerInNoticePeriod"`)

* `WorkerTaxProtection` (value: `"WorkerTaxProtection"`)





## Enum: GenderEnum


* `Unknown` (value: `"Unknown"`)

* `Male` (value: `"Male"`)

* `Female` (value: `"Female"`)





## Enum: LeaverReasonEnum


* `Resigned` (value: `"Resigned"`)

* `Dismissed` (value: `"Dismissed"`)

* `Redundant` (value: `"Redundant"`)

* `Retired` (value: `"Retired"`)

* `Deceased` (value: `"Deceased"`)

* `LegalCustody` (value: `"LegalCustody"`)

* `Other` (value: `"Other"`)





## Enum: MaritalStatusEnum


* `NotSet` (value: `"NotSet"`)

* `Single` (value: `"Single"`)

* `Married` (value: `"Married"`)

* `Divorced` (value: `"Divorced"`)

* `Widowed` (value: `"Widowed"`)





## Enum: NicLiabilityEnum


* `HasOtherJob` (value: `"HasOtherJob"`)

* `IsFemaleEntitledToReducedRate` (value: `"IsFemaleEntitledToReducedRate"`)

* `IsNotLiable` (value: `"IsNotLiable"`)

* `IsContractedOut` (value: `"IsContractedOut"`)

* `IsFullyLiable` (value: `"IsFullyLiable"`)

* `IsApprentice` (value: `"IsApprentice"`)

* `LeaverBeyond6Weeks` (value: `"LeaverBeyond6Weeks"`)

* `PaymentAfterLeavingIrregular` (value: `"PaymentAfterLeavingIrregular"`)

* `IsFreePortWorker` (value: `"IsFreePortWorker"`)

* `IsNotLiableForEmployerNi` (value: `"IsNotLiableForEmployerNi"`)





## Enum: PaymentMethodEnum


* `NotSet` (value: `"NotSet"`)

* `Cash` (value: `"Cash"`)

* `Cheque` (value: `"Cheque"`)

* `BACS` (value: `"BACS"`)

* `FasterPayments` (value: `"FasterPayments"`)

* `Other` (value: `"Other"`)





## Enum: RegionEnum


* `NotSet` (value: `"NotSet"`)

* `England` (value: `"England"`)

* `Scotland` (value: `"Scotland"`)

* `Wales` (value: `"Wales"`)





## Enum: RuleExclusionsEnum


* `None` (value: `"None"`)

* `NiMissingPayInstructionRule` (value: `"NiMissingPayInstructionRule"`)

* `TaxMissingPayInstructionRule` (value: `"TaxMissingPayInstructionRule"`)

* `TaxCodeUpliftRule` (value: `"TaxCodeUpliftRule"`)

* `NiSetExpectedLetterRule` (value: `"NiSetExpectedLetterRule"`)

* `NiDateOfBirthChangeRetrospectiveCRule` (value: `"NiDateOfBirthChangeRetrospectiveCRule"`)

* `NiDefermentStatusChangeRule` (value: `"NiDefermentStatusChangeRule"`)

* `NiEndContractedOutTransferRule` (value: `"NiEndContractedOutTransferRule"`)

* `PaymentAfterLeavingTaxCodeRule` (value: `"PaymentAfterLeavingTaxCodeRule"`)

* `LeaverEndInstructionsRule` (value: `"LeaverEndInstructionsRule"`)

* `P45StudentLoanInstructionRule` (value: `"P45StudentLoanInstructionRule"`)

* `P45TaxInstructionRule` (value: `"P45TaxInstructionRule"`)

* `P45YtdTaxRule` (value: `"P45YtdTaxRule"`)

* `YtdInstructionRule` (value: `"YtdInstructionRule"`)

* `TaxCodeRegionChangeRule` (value: `"TaxCodeRegionChangeRule"`)

* `AutoEnrolmentStatusChangeRule` (value: `"AutoEnrolmentStatusChangeRule"`)

* `EmployeeDeceasedRule` (value: `"EmployeeDeceasedRule"`)

* `BenefitInstructionAutoEndRule` (value: `"BenefitInstructionAutoEndRule"`)





## Enum: SecondedEnum


* `NotSet` (value: `"NotSet"`)

* `Stay183DaysOrMore` (value: `"Stay183DaysOrMore"`)

* `StayLessThan183Days` (value: `"StayLessThan183Days"`)

* `InOutUk` (value: `"InOutUk"`)





## Enum: StarterDeclarationEnum


* `PreviouslyReported` (value: `"PreviouslyReported"`)

* `A` (value: `"A"`)

* `B` (value: `"B"`)

* `C` (value: `"C"`)





## Enum: TerritoryEnum


* `UnitedKingdom` (value: `"UnitedKingdom"`)





## Enum: WorkingWeekEnum


* `None` (value: `"None"`)

* `Monday` (value: `"Monday"`)

* `Tuesday` (value: `"Tuesday"`)

* `Wednesday` (value: `"Wednesday"`)

* `Thursday` (value: `"Thursday"`)

* `Friday` (value: `"Friday"`)

* `AllWeekDays` (value: `"AllWeekDays"`)

* `Saturday` (value: `"Saturday"`)

* `Sunday` (value: `"Sunday"`)

* `AllDays` (value: `"AllDays"`)




