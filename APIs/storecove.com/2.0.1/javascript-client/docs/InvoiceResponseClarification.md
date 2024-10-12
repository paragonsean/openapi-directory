# StorecoveApi.InvoiceResponseClarification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clarification** | **String** | A textual description of the clarification | [optional] 
**clarificationCode** | **String** | The code for the clarification. For details see https://docs.peppol.eu/poacc/upgrade-3/codelist/OPStatusReason/ and https://docs.peppol.eu/poacc/upgrade-3/codelist/OPStatusAction/ | [optional] 
**clarificationCodeType** | **String** | The type of the clarification. | [optional] 
**conditions** | [**[InvoiceResponseCondition]**](InvoiceResponseCondition.md) | A list of conditions that triggered the error. This is only included for receiving in webhooks. You cannot currently send these conditions. | [optional] 



## Enum: ClarificationCodeEnum


* `NON` (value: `"NON"`)

* `REF` (value: `"REF"`)

* `LEG` (value: `"LEG"`)

* `REC` (value: `"REC"`)

* `QUA` (value: `"QUA"`)

* `DEL` (value: `"DEL"`)

* `PRI` (value: `"PRI"`)

* `QTY` (value: `"QTY"`)

* `ITM` (value: `"ITM"`)

* `PAY` (value: `"PAY"`)

* `UNR` (value: `"UNR"`)

* `FIN` (value: `"FIN"`)

* `PPD` (value: `"PPD"`)

* `OTH` (value: `"OTH"`)

* `NOA` (value: `"NOA"`)

* `PIN` (value: `"PIN"`)

* `NIN` (value: `"NIN"`)

* `CNF` (value: `"CNF"`)

* `CNP` (value: `"CNP"`)

* `CNA` (value: `"CNA"`)





## Enum: ClarificationCodeTypeEnum


* `OPStatusReason` (value: `"OPStatusReason"`)

* `OPStatusAction` (value: `"OPStatusAction"`)




