

# ListJobsResponse

Response to a request to list Cloud Dataflow jobs in a project. This might be a partial response, depending on the page size in the ListJobsRequest. However, if the project does not have any jobs, an instance of ListJobsResponse is not returned and the requests's response body is empty {}.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**failedLocation** | [**List&lt;FailedLocation&gt;**](FailedLocation.md) | Zero or more messages describing the [regional endpoints] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that failed to respond. |  [optional] |
|**jobs** | [**List&lt;Job&gt;**](Job.md) | A subset of the requested job information. |  [optional] |
|**nextPageToken** | **String** | Set if there may be more results than fit in this response. |  [optional] |



