# FrankieFinancialApi.KYCScreeningResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressMatchCount** | **Number** | The number of address matches | 
**checkResult** | **String** | The disposition of the 2+2 Safe Harbour check  | [optional] 
**dobMatchCount** | **Number** | The number of date of birth matches | 
**matchingSources** | **[String]** | The is of matching data sources that produced a success match for the person being screened Example given is not indicative of the actual sources available.  | [optional] 
**nameMatchCount** | **Number** | The number of name matches | 



## Enum: CheckResultEnum


* `NOT_SCREENED` (value: `"NOT_SCREENED"`)

* `PASS` (value: `"PASS"`)

* `REFER` (value: `"REFER"`)

* `FAIL` (value: `"FAIL"`)




