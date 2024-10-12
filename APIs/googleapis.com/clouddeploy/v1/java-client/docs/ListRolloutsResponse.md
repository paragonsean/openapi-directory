

# ListRolloutsResponse

ListRolloutsResponse is the response object reutrned by `ListRollouts`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**rollouts** | [**List&lt;Rollout&gt;**](Rollout.md) | The &#x60;Rollout&#x60; objects. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



