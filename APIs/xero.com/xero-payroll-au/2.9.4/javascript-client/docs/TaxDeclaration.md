# XeroPayrollAuApi.TaxDeclaration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approvedWithholdingVariationPercentage** | **Number** | If the employee has approved withholding variation. e.g (0 - 100) | [optional] 
**australianResidentForTaxPurposes** | **Boolean** | If the employee is Australian resident for tax purposes. e.g true or false | [optional] 
**eligibleToReceiveLeaveLoading** | **Boolean** | If the employee is eligible to receive an additional percentage on top of ordinary earnings when they take leave (typically 17.5%). e.g true or false | [optional] 
**employeeID** | **String** | Address line 1 for employee home address | [optional] 
**employmentBasis** | [**EmploymentBasis**](EmploymentBasis.md) |  | [optional] 
**hasHELPDebt** | **Boolean** | If employee has HECS or HELP debt. e.g true or false | [optional] 
**hasSFSSDebt** | **Boolean** | If employee has financial supplement debt. e.g true or false | [optional] 
**hasStudentStartupLoan** | **Boolean** | If the employee is eligible for student startup loan rules | [optional] 
**hasTradeSupportLoanDebt** | **Boolean** | If employee has trade support loan. e.g true or false | [optional] 
**residencyStatus** | [**ResidencyStatus**](ResidencyStatus.md) |  | [optional] 
**tFNExemptionType** | [**TFNExemptionType**](TFNExemptionType.md) |  | [optional] 
**taxFileNumber** | **String** | The tax file number e.g 123123123. | [optional] 
**taxFreeThresholdClaimed** | **Boolean** | If tax free threshold claimed. e.g true or false | [optional] 
**taxOffsetEstimatedAmount** | **Number** | If has tax offset estimated then the tax offset estimated amount. e.g 100 | [optional] 
**updatedDateUTC** | **String** | Last modified timestamp | [optional] [readonly] 
**upwardVariationTaxWithholdingAmount** | **Number** | If the employee has requested that additional tax be withheld each pay run. e.g 50 | [optional] 


