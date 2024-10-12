

# HistogramChartSpec

A histogram chart. A histogram chart groups data items into bins, displaying each bin as a column of stacked items. Histograms are used to display the distribution of a dataset. Each column of items represents a range into which those items fall. The number of bins can be chosen automatically or specified explicitly.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bucketSize** | **Double** | By default the bucket size (the range of values stacked in a single column) is chosen automatically, but it may be overridden here. E.g., A bucket size of 1.5 results in buckets from 0 - 1.5, 1.5 - 3.0, etc. Cannot be negative. This field is optional. |  [optional] |
|**legendPosition** | [**LegendPositionEnum**](#LegendPositionEnum) | The position of the chart legend. |  [optional] |
|**outlierPercentile** | **Double** | The outlier percentile is used to ensure that outliers do not adversely affect the calculation of bucket sizes. For example, setting an outlier percentile of 0.05 indicates that the top and bottom 5% of values when calculating buckets. The values are still included in the chart, they will be added to the first or last buckets instead of their own buckets. Must be between 0.0 and 0.5. |  [optional] |
|**series** | [**List&lt;HistogramSeries&gt;**](HistogramSeries.md) | The series for a histogram may be either a single series of values to be bucketed or multiple series, each of the same length, containing the name of the series followed by the values to be bucketed for that series. |  [optional] |
|**showItemDividers** | **Boolean** | Whether horizontal divider lines should be displayed between items in each column. |  [optional] |



## Enum: LegendPositionEnum

| Name | Value |
|---- | -----|
| HISTOGRAM_CHART_LEGEND_POSITION_UNSPECIFIED | &quot;HISTOGRAM_CHART_LEGEND_POSITION_UNSPECIFIED&quot; |
| BOTTOM_LEGEND | &quot;BOTTOM_LEGEND&quot; |
| LEFT_LEGEND | &quot;LEFT_LEGEND&quot; |
| RIGHT_LEGEND | &quot;RIGHT_LEGEND&quot; |
| TOP_LEGEND | &quot;TOP_LEGEND&quot; |
| NO_LEGEND | &quot;NO_LEGEND&quot; |
| INSIDE_LEGEND | &quot;INSIDE_LEGEND&quot; |



