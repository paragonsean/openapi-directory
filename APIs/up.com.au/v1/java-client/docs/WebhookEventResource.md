

# WebhookEventResource

Provides the event data used in asynchronous webhook event callbacks to subscribed endpoints. Webhooks events have defined `eventType`s and may optionally relate to other resources within the Up API. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**WebhookEventResourceAttributes**](WebhookEventResourceAttributes.md) |  |  |
|**id** | **String** | The unique identifier for this event. This will remain constant across delivery retries.  |  |
|**relationships** | [**WebhookEventResourceRelationships**](WebhookEventResourceRelationships.md) |  |  |
|**type** | **String** | The type of this resource: &#x60;webhook-events&#x60; |  |



