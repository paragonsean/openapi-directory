

# LearningGenaiRootClassifierState

DataProviderOutput and MetricOutput can be saved between calls to the Classifier framework. For instance, you can run the query classifier, get outputs from those metrics, then use them in a result classifier as well. Example rule based on this idea: and_rules { rule { metric_name: 'query_safesearch_v2' ... } rule { metric_name: 'response_safesearch_v2' ... } }

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataProviderOutput** | [**List&lt;LearningGenaiRootDataProviderOutput&gt;**](LearningGenaiRootDataProviderOutput.md) |  |  [optional] |
|**metricOutput** | [**List&lt;LearningGenaiRootMetricOutput&gt;**](LearningGenaiRootMetricOutput.md) |  |  [optional] |



