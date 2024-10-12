

# Employer3


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**Address1**](Address1.md) |  |  [optional] |
|**apprenticeshipLevyAllowance** | **Double** | The employers&#39; apprenticeship levy allowance |  [optional] |
|**autoEnrolment** | [**AutoEnrolment**](AutoEnrolment.md) |  |  [optional] |
|**bacsServiceUserNumber** | **String** | The employers&#39; bacs service user number |  [optional] |
|**bankAccount** | [**BankAccount1**](BankAccount1.md) |  |  [optional] |
|**calculateApprenticeshipLevy** | **Boolean** | The employers&#39; calculate apprenticeship levy |  [optional] |
|**claimEmploymentAllowance** | **Boolean** | The employers&#39; claim employment allowance |  [optional] |
|**claimSmallEmployerRelief** | **Boolean** | The employers&#39; claim small employer relief |  [optional] |
|**effectiveDate** | **LocalDate** | The employers&#39; effective date |  [optional] |
|**hmrcSettings** | [**HmrcSettings**](HmrcSettings.md) |  |  [optional] |
|**metaData** | **Object** | The employers&#39; meta data |  [optional] |
|**name** | **String** | The employers&#39; name |  [optional] |
|**nextRevisionDate** | **LocalDate** | The employers&#39; next revision date |  [optional] |
|**region** | [**RegionEnum**](#RegionEnum) | The employers&#39; region |  [optional] |
|**revision** | **Integer** | The employers&#39; revision |  [optional] |
|**ruleExclusions** | [**RuleExclusionsEnum**](#RuleExclusionsEnum) | The employers&#39; rule exclusions |  [optional] |
|**territory** | [**TerritoryEnum**](#TerritoryEnum) | The employers&#39; territory |  [optional] |



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



## Enum: TerritoryEnum

| Name | Value |
|---- | -----|
| UNITED_KINGDOM | &quot;UnitedKingdom&quot; |



