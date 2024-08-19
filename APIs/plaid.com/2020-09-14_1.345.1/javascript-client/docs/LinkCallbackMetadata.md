# ThePlaidApi.LinkCallbackMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**[LinkDeliveryAccount]**](LinkDeliveryAccount.md) | A list of accounts attached to the connected Item. If Account Select is enabled via the developer dashboard, accounts will only include selected accounts. | [optional] 
**callbackType** | [**LinkDeliveryWebhookCallbackType**](LinkDeliveryWebhookCallbackType.md) |  | [optional] 
**eventName** | [**LinkEventName**](LinkEventName.md) |  | [optional] 
**institution** | [**LinkDeliveryInstitution**](LinkDeliveryInstitution.md) |  | [optional] 
**linkSessionId** | **String** | A unique identifier associated with a user&#39;s actions and events through the Link flow. Include this identifier when opening a support ticket for faster turnaround. | [optional] 
**requestId** | **String** | The request ID for the last request made by Link. This can be shared with Plaid Support to expedite investigation. | [optional] 
**status** | **String** | Indicates where in the flow the Link user exited | [optional] 


