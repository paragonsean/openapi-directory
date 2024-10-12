

# ListBackupOperationsResponse

The response for ListBackupOperations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | &#x60;next_page_token&#x60; can be sent in a subsequent ListBackupOperations call to fetch more of the matching metadata. |  [optional] |
|**operations** | [**List&lt;Operation&gt;**](Operation.md) | The list of matching backup long-running operations. Each operation&#39;s name will be prefixed by the backup&#39;s name. The operation&#39;s metadata field type &#x60;metadata.type_url&#x60; describes the type of the metadata. Operations returned include those that are pending or have completed/failed/canceled within the last 7 days. Operations returned are ordered by &#x60;operation.metadata.value.progress.start_time&#x60; in descending order starting from the most recently started operation. |  [optional] |



