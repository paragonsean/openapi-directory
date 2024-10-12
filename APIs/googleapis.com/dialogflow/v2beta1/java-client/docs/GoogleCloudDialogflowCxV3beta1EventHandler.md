

# GoogleCloudDialogflowCxV3beta1EventHandler

An event handler specifies an event that can be handled during a session. When the specified event happens, the following actions are taken in order: * If there is a `trigger_fulfillment` associated with the event, it will be called. * If there is a `target_page` associated with the event, the session will transition into the specified page. * If there is a `target_flow` associated with the event, the session will transition into the specified flow.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**event** | **String** | Required. The name of the event to handle. |  [optional] |
|**name** | **String** | Output only. The unique identifier of this event handler. |  [optional] [readonly] |
|**targetFlow** | **String** | The target flow to transition to. Format: &#x60;projects//locations//agents//flows/&#x60;. |  [optional] |
|**targetPage** | **String** | The target page to transition to. Format: &#x60;projects//locations//agents//flows//pages/&#x60;. |  [optional] |
|**triggerFulfillment** | [**GoogleCloudDialogflowCxV3beta1Fulfillment**](GoogleCloudDialogflowCxV3beta1Fulfillment.md) |  |  [optional] |



