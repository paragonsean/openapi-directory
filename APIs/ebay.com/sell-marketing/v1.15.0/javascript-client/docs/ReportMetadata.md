# MarketingApi.ReportMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimensionMetadata** | [**[DimensionMetadata]**](DimensionMetadata.md) | A list containing the metadata for the dimension used in the report. | [optional] 
**maxNumberOfDimensionsToRequest** | **Number** | The maximum number of dimensions that can be requested for the specified report type. | [optional] 
**maxNumberOfMetricsToRequest** | **Number** | The maximum number of metrics that can be requested for the specified report type. | [optional] 
**metricMetadata** | [**[MetricMetadata]**](MetricMetadata.md) | A list containing the metadata for the metrics in the report. | [optional] 
**reportType** | **String** | The &lt;b&gt;report_type&lt;/b&gt;, as specified in the request to create the report task.&lt;br/&gt;&lt;br/&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; INVENTORY_PERFORMANCE_REPORT is not currently available; availability date is pending.&lt;/span&gt; For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/marketing/types/plr:ReportTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 


