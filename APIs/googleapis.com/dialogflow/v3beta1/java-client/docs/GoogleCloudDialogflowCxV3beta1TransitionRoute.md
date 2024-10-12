

# GoogleCloudDialogflowCxV3beta1TransitionRoute

A transition route specifies a intent that can be matched and/or a data condition that can be evaluated during a session. When a specified transition is matched, the following actions are taken in order: * If there is a `trigger_fulfillment` associated with the transition, it will be called. * If there is a `target_page` associated with the transition, the session will transition into the specified page. * If there is a `target_flow` associated with the transition, the session will transition into the specified flow.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**condition** | **String** | The condition to evaluate against form parameters or session parameters. See the [conditions reference](https://cloud.google.com/dialogflow/cx/docs/reference/condition). At least one of &#x60;intent&#x60; or &#x60;condition&#x60; must be specified. When both &#x60;intent&#x60; and &#x60;condition&#x60; are specified, the transition can only happen when both are fulfilled. |  [optional] |
|**description** | **String** | Optional. The description of the transition route. The maximum length is 500 characters. |  [optional] |
|**intent** | **String** | The unique identifier of an Intent. Format: &#x60;projects//locations//agents//intents/&#x60;. Indicates that the transition can only happen when the given intent is matched. At least one of &#x60;intent&#x60; or &#x60;condition&#x60; must be specified. When both &#x60;intent&#x60; and &#x60;condition&#x60; are specified, the transition can only happen when both are fulfilled. |  [optional] |
|**name** | **String** | Output only. The unique identifier of this transition route. |  [optional] [readonly] |
|**targetFlow** | **String** | The target flow to transition to. Format: &#x60;projects//locations//agents//flows/&#x60;. |  [optional] |
|**targetPage** | **String** | The target page to transition to. Format: &#x60;projects//locations//agents//flows//pages/&#x60;. |  [optional] |
|**triggerFulfillment** | [**GoogleCloudDialogflowCxV3beta1Fulfillment**](GoogleCloudDialogflowCxV3beta1Fulfillment.md) |  |  [optional] |



