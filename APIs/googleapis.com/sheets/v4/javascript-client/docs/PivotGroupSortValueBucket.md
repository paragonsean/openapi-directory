# GoogleSheetsApi.PivotGroupSortValueBucket

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buckets** | [**[ExtendedValue]**](ExtendedValue.md) | Determines the bucket from which values are chosen to sort. For example, in a pivot table with one row group &amp; two column groups, the row group can list up to two values. The first value corresponds to a value within the first column group, and the second value corresponds to a value in the second column group. If no values are listed, this would indicate that the row should be sorted according to the \&quot;Grand Total\&quot; over the column groups. If a single value is listed, this would correspond to using the \&quot;Total\&quot; of that bucket. | [optional] 
**valuesIndex** | **Number** | The offset in the PivotTable.values list which the values in this grouping should be sorted by. | [optional] 


