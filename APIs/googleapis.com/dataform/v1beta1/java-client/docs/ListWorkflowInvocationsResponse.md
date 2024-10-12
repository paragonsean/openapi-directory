

# ListWorkflowInvocationsResponse

`ListWorkflowInvocations` response message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations which could not be reached. |  [optional] |
|**workflowInvocations** | [**List&lt;WorkflowInvocation&gt;**](WorkflowInvocation.md) | List of workflow invocations. |  [optional] |



