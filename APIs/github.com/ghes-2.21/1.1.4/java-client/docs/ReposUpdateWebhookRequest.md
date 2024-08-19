

# ReposUpdateWebhookRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | Determines if notifications are sent when the webhook is triggered. Set to &#x60;true&#x60; to send notifications. |  [optional] |
|**addEvents** | **List&lt;String&gt;** | Determines a list of events to be added to the list of events that the Hook triggers for. |  [optional] |
|**config** | [**ReposUpdateWebhookRequestConfig**](ReposUpdateWebhookRequestConfig.md) |  |  [optional] |
|**events** | **List&lt;String&gt;** | Determines what [events](https://docs.github.com/enterprise-server@2.21/webhooks/event-payloads) the hook is triggered for. This replaces the entire array of events. |  [optional] |
|**removeEvents** | **List&lt;String&gt;** | Determines a list of events to be removed from the list of events that the Hook triggers for. |  [optional] |



