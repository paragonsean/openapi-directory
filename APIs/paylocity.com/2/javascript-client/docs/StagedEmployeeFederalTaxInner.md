# PaylocityApi.StagedEmployeeFederalTaxInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | Tax amount. &lt;br  /&gt;Decimal (12,2) | [optional] 
**deductionsAmount** | **Number** | Box 4(b) on form W4 (year 2020 or later): Deductions amount. &lt;br  /&gt;Decimal (12,2) | [optional] 
**dependentsAmount** | **Number** | Box 3 on form W4 (year 2020 or later): Total dependents amount. &lt;br  /&gt;Decimal (12,2) | [optional] 
**exemptions** | **Number** | Federal tax exemptions value. &lt;br  /&gt;Decimal (12,2) | [optional] 
**filingStatus** | **String** | Employee federal filing status. Common values are *S* (Single), *M* (Married).&lt;br  /&gt;Max length: 50 | [optional] 
**higherRate** | **Boolean** | Box 2(c) on form W4 (year 2020 or later): Multiple Jobs or Spouse Works. &lt;br  /&gt;Boolean | [optional] 
**otherIncomeAmount** | **Number** | Box 4(a) on form W4 (year 2020 or later): Other income amount. &lt;br  /&gt;Decimal (12,2) | [optional] 
**percentage** | **Number** | Tax percentage. &lt;br  /&gt;Decimal (12,2) | [optional] 
**taxCalculationCode** | **String** | Tax calculation code. Common values are *F* (Flat), *P* (Percentage), *FDFP* (Flat Dollar Amount plus Fixed Percentage). &lt;br  /&gt;Max length: 10 | [optional] 
**w4FormYear** | **Number** | The federal W4 form year &lt;br  /&gt;Integer | [optional] 


