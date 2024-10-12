

# ListDatabaseOperationsResponse

The response for ListDatabaseOperations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | &#x60;next_page_token&#x60; can be sent in a subsequent ListDatabaseOperations call to fetch more of the matching metadata. |  [optional] |
|**operations** | [**List&lt;Operation&gt;**](Operation.md) | The list of matching database long-running operations. Each operation&#39;s name will be prefixed by the database&#39;s name. The operation&#39;s metadata field type &#x60;metadata.type_url&#x60; describes the type of the metadata. |  [optional] |



