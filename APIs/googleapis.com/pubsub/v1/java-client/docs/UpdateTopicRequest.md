

# UpdateTopicRequest

Request for the UpdateTopic method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**topic** | [**Topic**](Topic.md) |  |  [optional] |
|**updateMask** | **String** | Required. Indicates which fields in the provided topic to update. Must be specified and non-empty. Note that if &#x60;update_mask&#x60; contains \&quot;message_storage_policy\&quot; but the &#x60;message_storage_policy&#x60; is not set in the &#x60;topic&#x60; provided above, then the updated value is determined by the policy configured at the project or organization level. |  [optional] |



