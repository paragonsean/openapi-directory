

# GoogleCloudDialogflowCxV3ResponseMessageLiveAgentHandoff

Indicates that the conversation should be handed off to a live agent. Dialogflow only uses this to determine which conversations were handed off to a human agent for measurement purposes. What else to do with this signal is up to you and your handoff procedures. You may set this, for example: * In the entry_fulfillment of a Page if entering the page indicates something went extremely wrong in the conversation. * In a webhook response when you determine that the customer issue can only be handled by a human.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metadata** | **Map&lt;String, Object&gt;** | Custom metadata for your handoff procedure. Dialogflow doesn&#39;t impose any structure on this. |  [optional] |



