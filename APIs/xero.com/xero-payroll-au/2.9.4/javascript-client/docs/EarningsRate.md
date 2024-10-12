# XeroPayrollAuApi.EarningsRate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountCode** | **String** | See Accounts | [optional] 
**accrueLeave** | **Boolean** | Indicates that this earnings rate should accrue leave. Only applicable if RateType is MULTIPLE | [optional] 
**allowanceType** | [**AllowanceType**](AllowanceType.md) |  | [optional] 
**amount** | **Number** | Optional Amount for FIXEDAMOUNT RateType EarningsRate | [optional] 
**currentRecord** | **Boolean** | Is the current record | [optional] 
**earningsRateID** | **String** | Xero identifier | [optional] 
**earningsType** | [**EarningsType**](EarningsType.md) |  | [optional] 
**employmentTerminationPaymentType** | [**EmploymentTerminationPaymentType**](EmploymentTerminationPaymentType.md) |  | [optional] 
**isExemptFromSuper** | **Boolean** | See the ATO website for details of which payments are exempt from SGC | [optional] 
**isExemptFromTax** | **Boolean** | Most payments are subject to tax, so you should only set this value if you are sure that a payment is exempt from PAYG withholding | [optional] 
**isReportableAsW1** | **Boolean** | Boolean to determine if the earnings rate is reportable or exempt from W1 | [optional] 
**multiplier** | **Number** | This is the multiplier used to calculate the rate per unit, based on the employee’s ordinary earnings rate. For example, for time and a half enter 1.5. Only applicable if RateType is MULTIPLE | [optional] 
**name** | **String** | Name of the earnings rate (max length &#x3D; 100) | [optional] 
**ratePerUnit** | **String** | Default rate per unit (optional). Only applicable if RateType is RATEPERUNIT. | [optional] 
**rateType** | [**RateType**](RateType.md) |  | [optional] 
**typeOfUnits** | **String** | Type of units used to record earnings (max length &#x3D; 50). Only When RateType is RATEPERUNIT | [optional] 
**updatedDateUTC** | **String** | Last modified timestamp | [optional] [readonly] 


