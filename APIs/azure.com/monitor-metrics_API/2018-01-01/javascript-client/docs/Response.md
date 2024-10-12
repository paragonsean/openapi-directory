# MonitorManagementClient.Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | **Number** | The integer value representing the cost of the query, for data case. | [optional] 
**interval** | **String** | The interval (window size) for which the metric data was returned in.  This may be adjusted in the future and returned back from what was originally requested.  This is not present if a metadata request was made. | [optional] 
**namespace** | **String** | The namespace of the metrics been queried | [optional] 
**resourceregion** | **String** | The region of the resource been queried for metrics. | [optional] 
**timespan** | **String** | The timespan for which the data was retrieved. Its value consists of two datetimes concatenated, separated by &#39;/&#39;.  This may be adjusted in the future and returned back from what was originally requested. | 
**value** | [**[Metric]**](Metric.md) | the value of the collection. | 


