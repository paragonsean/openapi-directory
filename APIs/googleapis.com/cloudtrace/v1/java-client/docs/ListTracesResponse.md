

# ListTracesResponse

The response message for the `ListTraces` method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | If defined, indicates that there are more traces that match the request and that this value should be passed to the next request to continue retrieving additional traces. |  [optional] |
|**traces** | [**List&lt;Trace&gt;**](Trace.md) | List of trace records as specified by the view parameter. |  [optional] |



