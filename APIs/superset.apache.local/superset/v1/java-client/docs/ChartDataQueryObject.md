

# ChartDataQueryObject


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationLayers** | [**List&lt;AnnotationLayer&gt;**](AnnotationLayer.md) | Annotation layers to apply to chart |  [optional] |
|**appliedTimeExtras** | **Object** | A mapping of temporal extras that have been applied to the query |  [optional] |
|**applyFetchValuesPredicate** | **Boolean** | Add fetch values predicate (where clause) to query if defined in datasource |  [optional] |
|**columns** | **List&lt;String&gt;** | Columns which to select in the query. |  [optional] |
|**datasource** | [**ChartDataDatasource**](ChartDataDatasource.md) |  |  [optional] |
|**druidTimeOrigin** | **String** | Starting point for time grain counting on legacy Druid datasources. Used to change e.g. Monday/Sunday first-day-of-week. This field is deprecated and should be passed to &#x60;extras&#x60; as &#x60;druid_time_origin&#x60;. |  [optional] |
|**extras** | [**ChartDataExtras**](ChartDataExtras.md) | Extra parameters to add to the query. |  [optional] |
|**filters** | [**List&lt;ChartDataFilter&gt;**](ChartDataFilter.md) |  |  [optional] |
|**granularity** | **String** | Name of temporal column used for time filtering. For legacy Druid datasources this defines the time grain. |  [optional] |
|**granularitySqla** | **String** | Name of temporal column used for time filtering for SQL datasources. This field is deprecated, use &#x60;granularity&#x60; instead. |  [optional] |
|**groupby** | **List&lt;String&gt;** |  |  [optional] |
|**having** | **String** | HAVING clause to be added to aggregate queries using AND operator. This field is deprecated and should be passed to &#x60;extras&#x60;. |  [optional] |
|**havingFilters** | [**List&lt;ChartDataFilter&gt;**](ChartDataFilter.md) | HAVING filters to be added to legacy Druid datasource queries. This field is deprecated and should be passed to &#x60;extras&#x60; as &#x60;having_druid&#x60;. |  [optional] |
|**isRowcount** | **Boolean** | Should the rowcount of the actual query be returned |  [optional] |
|**isTimeseries** | **Boolean** | Is the &#x60;query_object&#x60; a timeseries. |  [optional] |
|**metrics** | **List&lt;Object&gt;** | Aggregate expressions. Metrics can be passed as both references to datasource metrics (strings), or ad-hoc metricswhich are defined only within the query object. See &#x60;ChartDataAdhocMetricSchema&#x60; for the structure of ad-hoc metrics. |  [optional] |
|**orderDesc** | **Boolean** | Reverse order. Default: &#x60;false&#x60; |  [optional] |
|**orderby** | **List&lt;Object&gt;** | Expects a list of lists where the first element is the column name which to sort by, and the second element is a boolean. |  [optional] |
|**postProcessing** | [**List&lt;ChartDataPostProcessingOperation&gt;**](ChartDataPostProcessingOperation.md) | Post processing operations to be applied to the result set. Operations are applied to the result set in sequential order. |  [optional] |
|**resultType** | **Object** |  |  [optional] |
|**rowLimit** | **Integer** | Maximum row count (0&#x3D;disabled). Default: &#x60;config[\&quot;ROW_LIMIT\&quot;]&#x60; |  [optional] |
|**rowOffset** | **Integer** | Number of rows to skip. Default: &#x60;0&#x60; |  [optional] |
|**timeOffsets** | **List&lt;String&gt;** |  |  [optional] |
|**timeRange** | **String** | A time rage, either expressed as a colon separated string &#x60;since : until&#x60; or human readable freeform. Valid formats for &#x60;since&#x60; and &#x60;until&#x60; are:  - ISO 8601 - X days/years/hours/day/year/weeks - X days/years/hours/day/year/weeks ago - X days/years/hours/day/year/weeks from now  Additionally, the following freeform can be used:  - Last day - Last week - Last month - Last quarter - Last year - No filter - Last X seconds/minutes/hours/days/weeks/months/years - Next X seconds/minutes/hours/days/weeks/months/years  |  [optional] |
|**timeShift** | **String** | A human-readable date/time string. Please refer to [parsdatetime](https://github.com/bear/parsedatetime) documentation for details on valid values. |  [optional] |
|**timeseriesLimit** | **Integer** | Maximum row count for timeseries queries. Default: &#x60;0&#x60; |  [optional] |
|**timeseriesLimitMetric** | **Object** | Metric used to limit timeseries queries by. |  [optional] |
|**urlParams** | **Map&lt;String, String&gt;** | Optional query parameters passed to a dashboard or Explore view |  [optional] |
|**where** | **String** | WHERE clause to be added to queries using AND operator.This field is deprecated and should be passed to &#x60;extras&#x60;. |  [optional] |



