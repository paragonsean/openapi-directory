

# OrgsCreateWebhookRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | Determines if notifications are sent when the webhook is triggered. Set to &#x60;true&#x60; to send notifications. |  [optional] |
|**config** | [**OrgsCreateWebhookRequestConfig**](OrgsCreateWebhookRequestConfig.md) |  |  |
|**events** | **List&lt;String&gt;** | Determines what [events](https://docs.github.com/enterprise-server@3.2/webhooks/event-payloads) the hook is triggered for. Set to &#x60;[\&quot;*\&quot;]&#x60; to receive all possible events. |  [optional] |
|**name** | **String** | Must be passed as \&quot;web\&quot;. |  |



