

# CellData

Data about a specific cell.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSourceFormula** | [**DataSourceFormula**](DataSourceFormula.md) |  |  [optional] |
|**dataSourceTable** | [**DataSourceTable**](DataSourceTable.md) |  |  [optional] |
|**dataValidation** | [**DataValidationRule**](DataValidationRule.md) |  |  [optional] |
|**effectiveFormat** | [**CellFormat**](CellFormat.md) |  |  [optional] |
|**effectiveValue** | [**ExtendedValue**](ExtendedValue.md) |  |  [optional] |
|**formattedValue** | **String** | The formatted value of the cell. This is the value as it&#39;s shown to the user. This field is read-only. |  [optional] |
|**hyperlink** | **String** | A hyperlink this cell points to, if any. If the cell contains multiple hyperlinks, this field will be empty. This field is read-only. To set it, use a &#x60;&#x3D;HYPERLINK&#x60; formula in the userEnteredValue.formulaValue field. A cell-level link can also be set from the userEnteredFormat.textFormat field. Alternatively, set a hyperlink in the textFormatRun.format.link field that spans the entire cell. |  [optional] |
|**note** | **String** | Any note on the cell. |  [optional] |
|**pivotTable** | [**PivotTable**](PivotTable.md) |  |  [optional] |
|**textFormatRuns** | [**List&lt;TextFormatRun&gt;**](TextFormatRun.md) | Runs of rich text applied to subsections of the cell. Runs are only valid on user entered strings, not formulas, bools, or numbers. Properties of a run start at a specific index in the text and continue until the next run. Runs will inherit the properties of the cell unless explicitly changed. When writing, the new runs will overwrite any prior runs. When writing a new user_entered_value, previous runs are erased. |  [optional] |
|**userEnteredFormat** | [**CellFormat**](CellFormat.md) |  |  [optional] |
|**userEnteredValue** | [**ExtendedValue**](ExtendedValue.md) |  |  [optional] |



