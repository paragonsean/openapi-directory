

# HistogramResults

Output only. Histogram results that match HistogramFacets specified in SearchJobsRequest.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**compensationHistogramResults** | [**List&lt;CompensationHistogramResult&gt;**](CompensationHistogramResult.md) | Specifies compensation field-based histogram results that match HistogramFacets.compensation_histogram_requests. |  [optional] |
|**customAttributeHistogramResults** | [**List&lt;CustomAttributeHistogramResult&gt;**](CustomAttributeHistogramResult.md) | Specifies histogram results for custom attributes that match HistogramFacets.custom_attribute_histogram_facets. |  [optional] |
|**simpleHistogramResults** | [**List&lt;HistogramResult&gt;**](HistogramResult.md) | Specifies histogram results that matches HistogramFacets.simple_histogram_facets. |  [optional] |



