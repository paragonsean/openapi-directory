

# StagedEmployeeFederalTaxInner

The Federal Tax model

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **BigDecimal** | Tax amount. &lt;br  /&gt;Decimal (12,2) |  [optional] |
|**deductionsAmount** | **BigDecimal** | Box 4(b) on form W4 (year 2020 or later): Deductions amount. &lt;br  /&gt;Decimal (12,2) |  [optional] |
|**dependentsAmount** | **BigDecimal** | Box 3 on form W4 (year 2020 or later): Total dependents amount. &lt;br  /&gt;Decimal (12,2) |  [optional] |
|**exemptions** | **BigDecimal** | Federal tax exemptions value. &lt;br  /&gt;Decimal (12,2) |  [optional] |
|**filingStatus** | **String** | Employee federal filing status. Common values are *S* (Single), *M* (Married).&lt;br  /&gt;Max length: 50 |  [optional] |
|**higherRate** | **Boolean** | Box 2(c) on form W4 (year 2020 or later): Multiple Jobs or Spouse Works. &lt;br  /&gt;Boolean |  [optional] |
|**otherIncomeAmount** | **BigDecimal** | Box 4(a) on form W4 (year 2020 or later): Other income amount. &lt;br  /&gt;Decimal (12,2) |  [optional] |
|**percentage** | **BigDecimal** | Tax percentage. &lt;br  /&gt;Decimal (12,2) |  [optional] |
|**taxCalculationCode** | **String** | Tax calculation code. Common values are *F* (Flat), *P* (Percentage), *FDFP* (Flat Dollar Amount plus Fixed Percentage). &lt;br  /&gt;Max length: 10 |  [optional] |
|**w4FormYear** | **Integer** | The federal W4 form year &lt;br  /&gt;Integer |  [optional] |



