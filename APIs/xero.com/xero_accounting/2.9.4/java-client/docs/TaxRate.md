

# TaxRate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**canApplyToAssets** | **Boolean** | Boolean to describe if tax rate can be used for asset accounts i.e.  true,false |  [optional] [readonly] |
|**canApplyToEquity** | **Boolean** | Boolean to describe if tax rate can be used for equity accounts i.e true,false |  [optional] [readonly] |
|**canApplyToExpenses** | **Boolean** | Boolean to describe if tax rate can be used for expense accounts  i.e. true,false |  [optional] [readonly] |
|**canApplyToLiabilities** | **Boolean** | Boolean to describe if tax rate can be used for liability accounts  i.e. true,false |  [optional] [readonly] |
|**canApplyToRevenue** | **Boolean** | Boolean to describe if tax rate can be used for revenue accounts i.e. true,false |  [optional] [readonly] |
|**displayTaxRate** | **Double** | Tax Rate (decimal to 4dp) e.g 12.5000 |  [optional] [readonly] |
|**effectiveRate** | **Double** | Effective Tax Rate (decimal to 4dp) e.g 12.5000 |  [optional] [readonly] |
|**name** | **String** | Name of tax rate |  [optional] |
|**reportTaxType** | [**ReportTaxTypeEnum**](#ReportTaxTypeEnum) | See ReportTaxTypes |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | See Status Codes |  [optional] |
|**taxComponents** | [**List&lt;TaxComponent&gt;**](TaxComponent.md) | See TaxComponents |  [optional] |
|**taxType** | **String** | The tax type |  [optional] |



## Enum: ReportTaxTypeEnum

| Name | Value |
|---- | -----|
| AVALARA | &quot;AVALARA&quot; |
| BASEXCLUDED | &quot;BASEXCLUDED&quot; |
| CAPITALSALESOUTPUT | &quot;CAPITALSALESOUTPUT&quot; |
| CAPITALEXPENSESINPUT | &quot;CAPITALEXPENSESINPUT&quot; |
| ECOUTPUT | &quot;ECOUTPUT&quot; |
| ECOUTPUTSERVICES | &quot;ECOUTPUTSERVICES&quot; |
| ECINPUT | &quot;ECINPUT&quot; |
| ECACQUISITIONS | &quot;ECACQUISITIONS&quot; |
| EXEMPTEXPENSES | &quot;EXEMPTEXPENSES&quot; |
| EXEMPTINPUT | &quot;EXEMPTINPUT&quot; |
| EXEMPTOUTPUT | &quot;EXEMPTOUTPUT&quot; |
| GSTONIMPORTS | &quot;GSTONIMPORTS&quot; |
| INPUT | &quot;INPUT&quot; |
| INPUTTAXED | &quot;INPUTTAXED&quot; |
| MOSSSALES | &quot;MOSSSALES&quot; |
| NONE | &quot;NONE&quot; |
| NONEOUTPUT | &quot;NONEOUTPUT&quot; |
| OUTPUT | &quot;OUTPUT&quot; |
| PURCHASESINPUT | &quot;PURCHASESINPUT&quot; |
| SALESOUTPUT | &quot;SALESOUTPUT&quot; |
| EXEMPTCAPITAL | &quot;EXEMPTCAPITAL&quot; |
| EXEMPTEXPORT | &quot;EXEMPTEXPORT&quot; |
| CAPITALEXINPUT | &quot;CAPITALEXINPUT&quot; |
| GSTONCAPIMPORTS | &quot;GSTONCAPIMPORTS&quot; |
| GSTONCAPITALIMPORTS | &quot;GSTONCAPITALIMPORTS&quot; |
| REVERSECHARGES | &quot;REVERSECHARGES&quot; |
| PAYMENTS | &quot;PAYMENTS&quot; |
| INVOICE | &quot;INVOICE&quot; |
| CASH | &quot;CASH&quot; |
| ACCRUAL | &quot;ACCRUAL&quot; |
| FLATRATECASH | &quot;FLATRATECASH&quot; |
| FLATRATEACCRUAL | &quot;FLATRATEACCRUAL&quot; |
| ACCRUALS | &quot;ACCRUALS&quot; |
| TXCA | &quot;TXCA&quot; |
| SRCAS | &quot;SRCAS&quot; |
| DSOUTPUT | &quot;DSOUTPUT&quot; |
| BLINPUT2 | &quot;BLINPUT2&quot; |
| EPINPUT | &quot;EPINPUT&quot; |
| IMINPUT2 | &quot;IMINPUT2&quot; |
| MEINPUT | &quot;MEINPUT&quot; |
| IGDSINPUT2 | &quot;IGDSINPUT2&quot; |
| ESN33_OUTPUT | &quot;ESN33OUTPUT&quot; |
| OPINPUT | &quot;OPINPUT&quot; |
| OSOUTPUT | &quot;OSOUTPUT&quot; |
| TXN33_INPUT | &quot;TXN33INPUT&quot; |
| TXESSINPUT | &quot;TXESSINPUT&quot; |
| TXREINPUT | &quot;TXREINPUT&quot; |
| TXPETINPUT | &quot;TXPETINPUT&quot; |
| NRINPUT | &quot;NRINPUT&quot; |
| ES33_OUTPUT | &quot;ES33OUTPUT&quot; |
| ZERORATEDINPUT | &quot;ZERORATEDINPUT&quot; |
| ZERORATEDOUTPUT | &quot;ZERORATEDOUTPUT&quot; |
| DRCHARGESUPPLY | &quot;DRCHARGESUPPLY&quot; |
| DRCHARGE | &quot;DRCHARGE&quot; |
| CAPINPUT | &quot;CAPINPUT&quot; |
| CAPIMPORTS | &quot;CAPIMPORTS&quot; |
| IMINPUT | &quot;IMINPUT&quot; |
| INPUT2 | &quot;INPUT2&quot; |
| CIUINPUT | &quot;CIUINPUT&quot; |
| SRINPUT | &quot;SRINPUT&quot; |
| OUTPUT2 | &quot;OUTPUT2&quot; |
| SROUTPUT | &quot;SROUTPUT&quot; |
| CAPOUTPUT | &quot;CAPOUTPUT&quot; |
| SROUTPUT2 | &quot;SROUTPUT2&quot; |
| CIUOUTPUT | &quot;CIUOUTPUT&quot; |
| ZROUTPUT | &quot;ZROUTPUT&quot; |
| ZREXPORT | &quot;ZREXPORT&quot; |
| ACC28_PLUS | &quot;ACC28PLUS&quot; |
| ACCUPTO28 | &quot;ACCUPTO28&quot; |
| OTHEROUTPUT | &quot;OTHEROUTPUT&quot; |
| SHOUTPUT | &quot;SHOUTPUT&quot; |
| ZRINPUT | &quot;ZRINPUT&quot; |
| BADDEBT | &quot;BADDEBT&quot; |
| OTHERINPUT | &quot;OTHERINPUT&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| DELETED | &quot;DELETED&quot; |
| ARCHIVED | &quot;ARCHIVED&quot; |
| PENDING | &quot;PENDING&quot; |



