# HrisApi.EmployeeCompensation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | [**Currency**](Currency.md) |  | [optional] 
**effectiveDate** | **String** | The date on which a change to an employee&#39;s compensation takes effect. | [optional] 
**flsaStatus** | **String** | The FLSA status for this compensation. | [optional] 
**id** | **String** | A unique identifier for an object. | [optional] [readonly] 
**jobId** | **String** | The ID of the job to which the compensation belongs. | [optional] [readonly] 
**paymentFrequency** | [**PaymentFrequency**](PaymentFrequency.md) |  | [optional] 
**paymentUnit** | [**PaymentUnit**](PaymentUnit.md) |  | [optional] 
**rate** | **Number** | The amount paid per payment unit. | [optional] 



## Enum: FlsaStatusEnum


* `exempt` (value: `"exempt"`)

* `salaried-nonexempt` (value: `"salaried-nonexempt"`)

* `nonexempt` (value: `"nonexempt"`)

* `owner` (value: `"owner"`)

* `other` (value: `"other"`)




