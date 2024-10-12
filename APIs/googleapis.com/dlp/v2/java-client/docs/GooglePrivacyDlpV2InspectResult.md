

# GooglePrivacyDlpV2InspectResult

All the findings for a single scanned item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**findings** | [**List&lt;GooglePrivacyDlpV2Finding&gt;**](GooglePrivacyDlpV2Finding.md) | List of findings for an item. |  [optional] |
|**findingsTruncated** | **Boolean** | If true, then this item might have more findings than were returned, and the findings returned are an arbitrary subset of all findings. The findings list might be truncated because the input items were too large, or because the server reached the maximum amount of resources allowed for a single API call. For best results, divide the input into smaller batches. |  [optional] |



