

# DisputeEvidenceCreatedWebhook

Published when evidence is added to a [Dispute](https://developer.squareup.com/reference/square_2021-08-18/objects/Dispute) from the Disputes Dashboard in the Seller Dashboard, the Square Point of Sale app, or by calling either [CreateDisputeEvidenceFile](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/create-dispute-evidence-file) or [CreateDisputeEvidenceText](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/create-dispute-evidence-text).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **String** | Timestamp of when the webhook event was created, in RFC 3339 format. |  [optional] |
|**data** | [**DisputeEvidenceCreatedWebhookData**](DisputeEvidenceCreatedWebhookData.md) |  |  [optional] |
|**eventId** | **String** | A unique ID for the webhook event. |  [optional] |
|**locationId** | **String** | The ID of the target location associated with the event. |  [optional] |
|**merchantId** | **String** | The ID of the target merchant associated with the event. |  [optional] |
|**type** | **String** | The type of event this represents. |  [optional] |



