

# ListAutomationRunsResponse

The response object from `ListAutomationRuns`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**automationRuns** | [**List&lt;AutomationRun&gt;**](AutomationRun.md) | The &#x60;AutomationRuns&#x60; objects. |  [optional] |
|**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



