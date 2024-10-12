# DataflowApi.MetricStructuredName

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **{String: String}** | Zero or more labeled fields which identify the part of the job this metric is associated with, such as the name of a step or collection. For example, built-in counters associated with steps will have context[&#39;step&#39;] &#x3D; . Counters associated with PCollections in the SDK will have context[&#39;pcollection&#39;] &#x3D; . | [optional] 
**name** | **String** | Worker-defined metric name. | [optional] 
**origin** | **String** | Origin (namespace) of metric name. May be blank for user-define metrics; will be \&quot;dataflow\&quot; for metrics defined by the Dataflow service or SDK. | [optional] 


