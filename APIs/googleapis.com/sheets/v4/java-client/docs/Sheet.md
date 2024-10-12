

# Sheet

A sheet in a spreadsheet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bandedRanges** | [**List&lt;BandedRange&gt;**](BandedRange.md) | The banded (alternating colors) ranges on this sheet. |  [optional] |
|**basicFilter** | [**BasicFilter**](BasicFilter.md) |  |  [optional] |
|**charts** | [**List&lt;EmbeddedChart&gt;**](EmbeddedChart.md) | The specifications of every chart on this sheet. |  [optional] |
|**columnGroups** | [**List&lt;DimensionGroup&gt;**](DimensionGroup.md) | All column groups on this sheet, ordered by increasing range start index, then by group depth. |  [optional] |
|**conditionalFormats** | [**List&lt;ConditionalFormatRule&gt;**](ConditionalFormatRule.md) | The conditional format rules in this sheet. |  [optional] |
|**data** | [**List&lt;GridData&gt;**](GridData.md) | Data in the grid, if this is a grid sheet. The number of GridData objects returned is dependent on the number of ranges requested on this sheet. For example, if this is representing &#x60;Sheet1&#x60;, and the spreadsheet was requested with ranges &#x60;Sheet1!A1:C10&#x60; and &#x60;Sheet1!D15:E20&#x60;, then the first GridData will have a startRow/startColumn of &#x60;0&#x60;, while the second one will have &#x60;startRow 14&#x60; (zero-based row 15), and &#x60;startColumn 3&#x60; (zero-based column D). For a DATA_SOURCE sheet, you can not request a specific range, the GridData contains all the values. |  [optional] |
|**developerMetadata** | [**List&lt;DeveloperMetadata&gt;**](DeveloperMetadata.md) | The developer metadata associated with a sheet. |  [optional] |
|**filterViews** | [**List&lt;FilterView&gt;**](FilterView.md) | The filter views in this sheet. |  [optional] |
|**merges** | [**List&lt;GridRange&gt;**](GridRange.md) | The ranges that are merged together. |  [optional] |
|**properties** | [**SheetProperties**](SheetProperties.md) |  |  [optional] |
|**protectedRanges** | [**List&lt;ProtectedRange&gt;**](ProtectedRange.md) | The protected ranges in this sheet. |  [optional] |
|**rowGroups** | [**List&lt;DimensionGroup&gt;**](DimensionGroup.md) | All row groups on this sheet, ordered by increasing range start index, then by group depth. |  [optional] |
|**slicers** | [**List&lt;Slicer&gt;**](Slicer.md) | The slicers on this sheet. |  [optional] |



