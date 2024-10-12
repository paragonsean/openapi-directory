

# ListWorkflowsResponse

Response for the ListWorkflows method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Unreachable resources. |  [optional] |
|**workflows** | [**List&lt;Workflow&gt;**](Workflow.md) | The workflows that match the request. |  [optional] |



