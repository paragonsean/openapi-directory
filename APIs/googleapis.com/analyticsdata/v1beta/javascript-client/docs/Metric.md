# GoogleAnalyticsDataApi.Metric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **String** | A mathematical expression for derived metrics. For example, the metric Event count per user is &#x60;eventCount/totalUsers&#x60;. | [optional] 
**invisible** | **Boolean** | Indicates if a metric is invisible in the report response. If a metric is invisible, the metric will not produce a column in the response, but can be used in &#x60;metricFilter&#x60;, &#x60;orderBys&#x60;, or a metric &#x60;expression&#x60;. | [optional] 
**name** | **String** | The name of the metric. See the [API Metrics](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#metrics) for the list of metric names supported by core reporting methods such as &#x60;runReport&#x60; and &#x60;batchRunReports&#x60;. See [Realtime Metrics](https://developers.google.com/analytics/devguides/reporting/data/v1/realtime-api-schema#metrics) for the list of metric names supported by the &#x60;runRealtimeReport&#x60; method. See [Funnel Metrics](https://developers.google.com/analytics/devguides/reporting/data/v1/exploration-api-schema#metrics) for the list of metric names supported by the &#x60;runFunnelReport&#x60; method. If &#x60;expression&#x60; is specified, &#x60;name&#x60; can be any string that you would like within the allowed character set. For example if &#x60;expression&#x60; is &#x60;screenPageViews/sessions&#x60;, you could call that metric&#39;s name &#x3D; &#x60;viewsPerSession&#x60;. Metric names that you choose must match the regular expression &#x60;^[a-zA-Z0-9_]$&#x60;. Metrics are referenced by &#x60;name&#x60; in &#x60;metricFilter&#x60;, &#x60;orderBys&#x60;, and metric &#x60;expression&#x60;. | [optional] 


