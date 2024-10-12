

# ListJobsResponse

ListJobsResponse is a list of Jobs resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiVersion** | **String** | The API version for this call such as \&quot;run.googleapis.com/v1alpha1\&quot;. |  [optional] |
|**items** | [**List&lt;Job&gt;**](Job.md) | List of Jobs. |  [optional] |
|**kind** | **String** | The kind of this resource, in this case \&quot;JobsList\&quot;. |  [optional] |
|**metadata** | [**ListMeta**](ListMeta.md) |  |  [optional] |
|**nextPageToken** | **String** | This field is equivalent to the metadata.continue field and is provided as a convenience for compatibility with https://google.aip.dev/158. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a list may not be possible if the server configuration has changed or more than a few minutes have passed. The metadata.resourceVersion field returned when using this field will be identical to the value in the first response. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



