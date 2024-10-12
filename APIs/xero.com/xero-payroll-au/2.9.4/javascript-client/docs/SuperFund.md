# XeroPayrollAuApi.SuperFund

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ABN** | **String** | ABN of the self managed super fund | [optional] 
**accountName** | **String** | The account name for the self managed super fund. | [optional] 
**accountNumber** | **String** | The account number for the self managed super fund. | [optional] 
**BSB** | **String** | BSB of the self managed super fund | [optional] 
**electronicServiceAddress** | **String** | The electronic service address for the self managed super fund. | [optional] 
**employerNumber** | **String** | Some funds assign a unique number to each employer | [optional] 
**name** | **String** | Name of the super fund | [optional] 
**SPIN** | **String** | The SPIN of the Regulated SuperFund. This field has been deprecated. It will only be present for legacy superfunds. New superfunds will not have a SPIN value. The USI field should be used instead of SPIN. | [optional] 
**superFundID** | **String** | Xero identifier for a super fund | [optional] 
**type** | [**SuperFundType**](SuperFundType.md) |  | 
**USI** | **String** | The USI of the Regulated SuperFund | [optional] 
**updatedDateUTC** | **String** | Last modified timestamp | [optional] [readonly] 
**validationErrors** | [**[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 


