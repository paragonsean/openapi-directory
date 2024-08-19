

# HookDeliveryItem

Delivery made by a webhook, without request and response information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | **String** | The type of activity for the event that triggered the delivery. |  |
|**deliveredAt** | **OffsetDateTime** | Time when the webhook delivery occurred. |  |
|**duration** | **BigDecimal** | Time spent delivering. |  |
|**event** | **String** | The event that triggered the delivery. |  |
|**guid** | **String** | Unique identifier for the event (shared with all deliveries for all webhooks that subscribe to this event). |  |
|**id** | **Integer** | Unique identifier of the webhook delivery. |  |
|**installationId** | **Integer** | The id of the GitHub App installation associated with this event. |  |
|**redelivery** | **Boolean** | Whether the webhook delivery is a redelivery. |  |
|**repositoryId** | **Integer** | The id of the repository associated with this event. |  |
|**status** | **String** | Describes the response returned after attempting the delivery. |  |
|**statusCode** | **Integer** | Status code received when delivery was made. |  |



