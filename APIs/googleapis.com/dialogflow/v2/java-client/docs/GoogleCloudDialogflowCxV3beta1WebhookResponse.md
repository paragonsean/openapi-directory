

# GoogleCloudDialogflowCxV3beta1WebhookResponse

The response message for a webhook call.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fulfillmentResponse** | [**GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponse**](GoogleCloudDialogflowCxV3beta1WebhookResponseFulfillmentResponse.md) |  |  [optional] |
|**pageInfo** | [**GoogleCloudDialogflowCxV3beta1PageInfo**](GoogleCloudDialogflowCxV3beta1PageInfo.md) |  |  [optional] |
|**payload** | **Map&lt;String, Object&gt;** | Value to append directly to QueryResult.webhook_payloads. |  [optional] |
|**sessionInfo** | [**GoogleCloudDialogflowCxV3beta1SessionInfo**](GoogleCloudDialogflowCxV3beta1SessionInfo.md) |  |  [optional] |
|**targetFlow** | **String** | The target flow to transition to. Format: &#x60;projects//locations//agents//flows/&#x60;. |  [optional] |
|**targetPage** | **String** | The target page to transition to. Format: &#x60;projects//locations//agents//flows//pages/&#x60;. |  [optional] |



