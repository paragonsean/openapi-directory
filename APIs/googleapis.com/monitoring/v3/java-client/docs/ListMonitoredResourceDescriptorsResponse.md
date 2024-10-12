

# ListMonitoredResourceDescriptorsResponse

The ListMonitoredResourceDescriptors response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as page_token in the next call to this method. |  [optional] |
|**resourceDescriptors** | [**List&lt;MonitoredResourceDescriptor&gt;**](MonitoredResourceDescriptor.md) | The monitored resource descriptors that are available to this project and that match filter, if present. |  [optional] |



