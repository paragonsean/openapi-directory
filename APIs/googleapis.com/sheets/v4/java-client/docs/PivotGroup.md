

# PivotGroup

A single grouping (either row or column) in a pivot table.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSourceColumnReference** | [**DataSourceColumnReference**](DataSourceColumnReference.md) |  |  [optional] |
|**groupLimit** | [**PivotGroupLimit**](PivotGroupLimit.md) |  |  [optional] |
|**groupRule** | [**PivotGroupRule**](PivotGroupRule.md) |  |  [optional] |
|**label** | **String** | The labels to use for the row/column groups which can be customized. For example, in the following pivot table, the row label is &#x60;Region&#x60; (which could be renamed to &#x60;State&#x60;) and the column label is &#x60;Product&#x60; (which could be renamed &#x60;Item&#x60;). Pivot tables created before December 2017 do not have header labels. If you&#39;d like to add header labels to an existing pivot table, please delete the existing pivot table and then create a new pivot table with same parameters. +--------------+---------+-------+ | SUM of Units | Product | | | Region | Pen | Paper | +--------------+---------+-------+ | New York | 345 | 98 | | Oregon | 234 | 123 | | Tennessee | 531 | 415 | +--------------+---------+-------+ | Grand Total | 1110 | 636 | +--------------+---------+-------+ |  [optional] |
|**repeatHeadings** | **Boolean** | True if the headings in this pivot group should be repeated. This is only valid for row groupings and is ignored by columns. By default, we minimize repetition of headings by not showing higher level headings where they are the same. For example, even though the third row below corresponds to \&quot;Q1 Mar\&quot;, \&quot;Q1\&quot; is not shown because it is redundant with previous rows. Setting repeat_headings to true would cause \&quot;Q1\&quot; to be repeated for \&quot;Feb\&quot; and \&quot;Mar\&quot;. +--------------+ | Q1 | Jan | | | Feb | | | Mar | +--------+-----+ | Q1 Total | +--------------+ |  [optional] |
|**showTotals** | **Boolean** | True if the pivot table should include the totals for this grouping. |  [optional] |
|**sortOrder** | [**SortOrderEnum**](#SortOrderEnum) | The order the values in this group should be sorted. |  [optional] |
|**sourceColumnOffset** | **Integer** | The column offset of the source range that this grouping is based on. For example, if the source was &#x60;C10:E15&#x60;, a &#x60;sourceColumnOffset&#x60; of &#x60;0&#x60; means this group refers to column &#x60;C&#x60;, whereas the offset &#x60;1&#x60; would refer to column &#x60;D&#x60;. |  [optional] |
|**valueBucket** | [**PivotGroupSortValueBucket**](PivotGroupSortValueBucket.md) |  |  [optional] |
|**valueMetadata** | [**List&lt;PivotGroupValueMetadata&gt;**](PivotGroupValueMetadata.md) | Metadata about values in the grouping. |  [optional] |



## Enum: SortOrderEnum

| Name | Value |
|---- | -----|
| SORT_ORDER_UNSPECIFIED | &quot;SORT_ORDER_UNSPECIFIED&quot; |
| ASCENDING | &quot;ASCENDING&quot; |
| DESCENDING | &quot;DESCENDING&quot; |



