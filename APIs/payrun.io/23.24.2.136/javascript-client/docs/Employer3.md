# PayRunIo.Employer3

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address1**](Address1.md) |  | [optional] 
**apprenticeshipLevyAllowance** | **Number** | The employers&#39; apprenticeship levy allowance | [optional] 
**autoEnrolment** | [**AutoEnrolment**](AutoEnrolment.md) |  | [optional] 
**bacsServiceUserNumber** | **String** | The employers&#39; bacs service user number | [optional] 
**bankAccount** | [**BankAccount1**](BankAccount1.md) |  | [optional] 
**calculateApprenticeshipLevy** | **Boolean** | The employers&#39; calculate apprenticeship levy | [optional] 
**claimEmploymentAllowance** | **Boolean** | The employers&#39; claim employment allowance | [optional] 
**claimSmallEmployerRelief** | **Boolean** | The employers&#39; claim small employer relief | [optional] 
**effectiveDate** | **Date** | The employers&#39; effective date | [optional] 
**hmrcSettings** | [**HmrcSettings**](HmrcSettings.md) |  | [optional] 
**metaData** | **Object** | The employers&#39; meta data | [optional] 
**name** | **String** | The employers&#39; name | [optional] 
**nextRevisionDate** | **Date** | The employers&#39; next revision date | [optional] 
**region** | **String** | The employers&#39; region | [optional] 
**revision** | **Number** | The employers&#39; revision | [optional] 
**ruleExclusions** | **String** | The employers&#39; rule exclusions | [optional] 
**territory** | **String** | The employers&#39; territory | [optional] 



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





## Enum: TerritoryEnum


* `UnitedKingdom` (value: `"UnitedKingdom"`)




