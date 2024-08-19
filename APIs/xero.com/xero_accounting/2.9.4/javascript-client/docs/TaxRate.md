# XeroAccountingApi.TaxRate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canApplyToAssets** | **Boolean** | Boolean to describe if tax rate can be used for asset accounts i.e.  true,false | [optional] [readonly] 
**canApplyToEquity** | **Boolean** | Boolean to describe if tax rate can be used for equity accounts i.e true,false | [optional] [readonly] 
**canApplyToExpenses** | **Boolean** | Boolean to describe if tax rate can be used for expense accounts  i.e. true,false | [optional] [readonly] 
**canApplyToLiabilities** | **Boolean** | Boolean to describe if tax rate can be used for liability accounts  i.e. true,false | [optional] [readonly] 
**canApplyToRevenue** | **Boolean** | Boolean to describe if tax rate can be used for revenue accounts i.e. true,false | [optional] [readonly] 
**displayTaxRate** | **Number** | Tax Rate (decimal to 4dp) e.g 12.5000 | [optional] [readonly] 
**effectiveRate** | **Number** | Effective Tax Rate (decimal to 4dp) e.g 12.5000 | [optional] [readonly] 
**name** | **String** | Name of tax rate | [optional] 
**reportTaxType** | **String** | See ReportTaxTypes | [optional] 
**status** | **String** | See Status Codes | [optional] 
**taxComponents** | [**[TaxComponent]**](TaxComponent.md) | See TaxComponents | [optional] 
**taxType** | **String** | The tax type | [optional] 



## Enum: ReportTaxTypeEnum


* `AVALARA` (value: `"AVALARA"`)

* `BASEXCLUDED` (value: `"BASEXCLUDED"`)

* `CAPITALSALESOUTPUT` (value: `"CAPITALSALESOUTPUT"`)

* `CAPITALEXPENSESINPUT` (value: `"CAPITALEXPENSESINPUT"`)

* `ECOUTPUT` (value: `"ECOUTPUT"`)

* `ECOUTPUTSERVICES` (value: `"ECOUTPUTSERVICES"`)

* `ECINPUT` (value: `"ECINPUT"`)

* `ECACQUISITIONS` (value: `"ECACQUISITIONS"`)

* `EXEMPTEXPENSES` (value: `"EXEMPTEXPENSES"`)

* `EXEMPTINPUT` (value: `"EXEMPTINPUT"`)

* `EXEMPTOUTPUT` (value: `"EXEMPTOUTPUT"`)

* `GSTONIMPORTS` (value: `"GSTONIMPORTS"`)

* `INPUT` (value: `"INPUT"`)

* `INPUTTAXED` (value: `"INPUTTAXED"`)

* `MOSSSALES` (value: `"MOSSSALES"`)

* `NONE` (value: `"NONE"`)

* `NONEOUTPUT` (value: `"NONEOUTPUT"`)

* `OUTPUT` (value: `"OUTPUT"`)

* `PURCHASESINPUT` (value: `"PURCHASESINPUT"`)

* `SALESOUTPUT` (value: `"SALESOUTPUT"`)

* `EXEMPTCAPITAL` (value: `"EXEMPTCAPITAL"`)

* `EXEMPTEXPORT` (value: `"EXEMPTEXPORT"`)

* `CAPITALEXINPUT` (value: `"CAPITALEXINPUT"`)

* `GSTONCAPIMPORTS` (value: `"GSTONCAPIMPORTS"`)

* `GSTONCAPITALIMPORTS` (value: `"GSTONCAPITALIMPORTS"`)

* `REVERSECHARGES` (value: `"REVERSECHARGES"`)

* `PAYMENTS` (value: `"PAYMENTS"`)

* `INVOICE` (value: `"INVOICE"`)

* `CASH` (value: `"CASH"`)

* `ACCRUAL` (value: `"ACCRUAL"`)

* `FLATRATECASH` (value: `"FLATRATECASH"`)

* `FLATRATEACCRUAL` (value: `"FLATRATEACCRUAL"`)

* `ACCRUALS` (value: `"ACCRUALS"`)

* `TXCA` (value: `"TXCA"`)

* `SRCAS` (value: `"SRCAS"`)

* `DSOUTPUT` (value: `"DSOUTPUT"`)

* `BLINPUT2` (value: `"BLINPUT2"`)

* `EPINPUT` (value: `"EPINPUT"`)

* `IMINPUT2` (value: `"IMINPUT2"`)

* `MEINPUT` (value: `"MEINPUT"`)

* `IGDSINPUT2` (value: `"IGDSINPUT2"`)

* `ESN33OUTPUT` (value: `"ESN33OUTPUT"`)

* `OPINPUT` (value: `"OPINPUT"`)

* `OSOUTPUT` (value: `"OSOUTPUT"`)

* `TXN33INPUT` (value: `"TXN33INPUT"`)

* `TXESSINPUT` (value: `"TXESSINPUT"`)

* `TXREINPUT` (value: `"TXREINPUT"`)

* `TXPETINPUT` (value: `"TXPETINPUT"`)

* `NRINPUT` (value: `"NRINPUT"`)

* `ES33OUTPUT` (value: `"ES33OUTPUT"`)

* `ZERORATEDINPUT` (value: `"ZERORATEDINPUT"`)

* `ZERORATEDOUTPUT` (value: `"ZERORATEDOUTPUT"`)

* `DRCHARGESUPPLY` (value: `"DRCHARGESUPPLY"`)

* `DRCHARGE` (value: `"DRCHARGE"`)

* `CAPINPUT` (value: `"CAPINPUT"`)

* `CAPIMPORTS` (value: `"CAPIMPORTS"`)

* `IMINPUT` (value: `"IMINPUT"`)

* `INPUT2` (value: `"INPUT2"`)

* `CIUINPUT` (value: `"CIUINPUT"`)

* `SRINPUT` (value: `"SRINPUT"`)

* `OUTPUT2` (value: `"OUTPUT2"`)

* `SROUTPUT` (value: `"SROUTPUT"`)

* `CAPOUTPUT` (value: `"CAPOUTPUT"`)

* `SROUTPUT2` (value: `"SROUTPUT2"`)

* `CIUOUTPUT` (value: `"CIUOUTPUT"`)

* `ZROUTPUT` (value: `"ZROUTPUT"`)

* `ZREXPORT` (value: `"ZREXPORT"`)

* `ACC28PLUS` (value: `"ACC28PLUS"`)

* `ACCUPTO28` (value: `"ACCUPTO28"`)

* `OTHEROUTPUT` (value: `"OTHEROUTPUT"`)

* `SHOUTPUT` (value: `"SHOUTPUT"`)

* `ZRINPUT` (value: `"ZRINPUT"`)

* `BADDEBT` (value: `"BADDEBT"`)

* `OTHERINPUT` (value: `"OTHERINPUT"`)





## Enum: StatusEnum


* `ACTIVE` (value: `"ACTIVE"`)

* `DELETED` (value: `"DELETED"`)

* `ARCHIVED` (value: `"ARCHIVED"`)

* `PENDING` (value: `"PENDING"`)




