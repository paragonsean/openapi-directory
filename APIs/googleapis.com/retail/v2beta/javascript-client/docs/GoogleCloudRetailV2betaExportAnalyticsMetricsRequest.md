# VertexAiSearchForRetailApi.GoogleCloudRetailV2betaExportAnalyticsMetricsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **String** | A filtering expression to specify restrictions on returned metrics. The expression is a sequence of terms. Each term applies a restriction to the returned metrics. Use this expression to restrict results to a specific time range. Currently we expect only one types of fields: * &#x60;timestamp&#x60;: This can be specified twice, once with a less than operator and once with a greater than operator. The &#x60;timestamp&#x60; restriction should result in one, contiguous, valid, &#x60;timestamp&#x60; range. Some examples of valid filters expressions: * Example 1: &#x60;timestamp &gt; \&quot;2012-04-23T18:25:43.511Z\&quot; timestamp &lt; \&quot;2012-04-23T18:30:43.511Z\&quot;&#x60; * Example 2: &#x60;timestamp &gt; \&quot;2012-04-23T18:25:43.511Z\&quot;&#x60; | [optional] 
**outputConfig** | [**GoogleCloudRetailV2betaOutputConfig**](GoogleCloudRetailV2betaOutputConfig.md) |  | [optional] 


