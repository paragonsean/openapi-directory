

# ListMetricDescriptorsResponse

The ListMetricDescriptors response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metricDescriptors** | [**List&lt;MetricDescriptor&gt;**](MetricDescriptor.md) | The metric descriptors that are available to the project and that match the value of filter, if present. |  [optional] |
|**nextPageToken** | **String** | If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as page_token in the next call to this method. |  [optional] |



