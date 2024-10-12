

# SlicerSpec

The specifications of a slicer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applyToPivotTables** | **Boolean** | True if the filter should apply to pivot tables. If not set, default to &#x60;True&#x60;. |  [optional] |
|**backgroundColor** | [**Color**](Color.md) |  |  [optional] |
|**backgroundColorStyle** | [**ColorStyle**](ColorStyle.md) |  |  [optional] |
|**columnIndex** | **Integer** | The zero-based column index in the data table on which the filter is applied to. |  [optional] |
|**dataRange** | [**GridRange**](GridRange.md) |  |  [optional] |
|**filterCriteria** | [**FilterCriteria**](FilterCriteria.md) |  |  [optional] |
|**horizontalAlignment** | [**HorizontalAlignmentEnum**](#HorizontalAlignmentEnum) | The horizontal alignment of title in the slicer. If unspecified, defaults to &#x60;LEFT&#x60; |  [optional] |
|**textFormat** | [**TextFormat**](TextFormat.md) |  |  [optional] |
|**title** | **String** | The title of the slicer. |  [optional] |



## Enum: HorizontalAlignmentEnum

| Name | Value |
|---- | -----|
| HORIZONTAL_ALIGN_UNSPECIFIED | &quot;HORIZONTAL_ALIGN_UNSPECIFIED&quot; |
| LEFT | &quot;LEFT&quot; |
| CENTER | &quot;CENTER&quot; |
| RIGHT | &quot;RIGHT&quot; |



