# OpenapiJsClient.PatientLabResultSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **String** |  | [optional] [readonly] 
**dateTestPerformed** | **String** | Date of lab test. | [optional] 
**doctorComments** | **String** | Comment from the doctor on lab result. | [optional] 
**doctorSignoff** | **Boolean** | Check this box when the doctor has reviewed the lab result and taken appropriate action. | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**labAbnormalFlag** | **String** | HL7 codified abnormal flag for the result. | [optional] 
**labImportedFromCcr** | **String** | Imported CCR document that contains lab results. | [optional] [readonly] 
**labNormalRange** | **String** |  | [optional] 
**labNormalRangeUnits** | **String** |  | [optional] 
**labOrderStatus** | **String** | Status of the lab order. | [optional] 
**labResultValue** | **String** |  | [optional] 
**labResultValueAsFloat** | **Number** |  | [optional] 
**labResultValueUnits** | **String** |  | [optional] 
**loincCode** | **String** |  | [optional] 
**orderingDoctor** | **Number** |  | 
**patient** | **Number** |  | 
**scannedInResult** | **String** | Scanned in PDF for this lab result (optional). | [optional] [readonly] 
**title** | **String** |  | [optional] 
**updatedAt** | **String** |  | [optional] [readonly] 



## Enum: LabAbnormalFlagEnum


* `empty` (value: `""`)

* `L` (value: `"L"`)

* `H` (value: `"H"`)

* `LL` (value: `"LL"`)

* `HH` (value: `"HH"`)

* `LESS_THAN` (value: `"<"`)

* `GREATER_THAN` (value: `">"`)

* `N` (value: `"N"`)

* `A` (value: `"A"`)

* `AA` (value: `"AA"`)

* `null` (value: `"null"`)

* `U` (value: `"U"`)

* `D` (value: `"D"`)

* `B` (value: `"B"`)

* `W` (value: `"W"`)

* `S` (value: `"S"`)

* `R` (value: `"R"`)

* `I` (value: `"I"`)

* `MS` (value: `"MS"`)

* `VS` (value: `"VS"`)





## Enum: LabOrderStatusEnum


* `empty` (value: `""`)

* `Order Entered` (value: `"Order Entered"`)

* `Discontinued` (value: `"Discontinued"`)

* `In Progress` (value: `"In Progress"`)

* `Results Received` (value: `"Results Received"`)

* `Results Reviewed with Patient` (value: `"Results Reviewed with Patient"`)

* `Paper Order` (value: `"Paper Order"`)




