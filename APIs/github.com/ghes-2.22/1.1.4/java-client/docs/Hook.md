

# Hook

Webhooks for repositories.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | Determines whether the hook is actually triggered on pushes. |  |
|**config** | [**HookConfig**](HookConfig.md) |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**events** | **List&lt;String&gt;** | Determines what events the hook is triggered for. Default: [&#39;push&#39;]. |  |
|**id** | **Integer** | Unique identifier of the webhook. |  |
|**lastResponse** | [**HookResponse**](HookResponse.md) |  |  |
|**name** | **String** | The name of a valid service, use &#39;web&#39; for a webhook. |  |
|**pingUrl** | **URI** |  |  |
|**testUrl** | **URI** |  |  |
|**type** | **String** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**url** | **URI** |  |  |



