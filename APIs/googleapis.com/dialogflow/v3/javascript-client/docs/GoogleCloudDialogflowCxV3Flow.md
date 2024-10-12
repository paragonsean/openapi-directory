# DialogflowApi.GoogleCloudDialogflowCxV3Flow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advancedSettings** | [**GoogleCloudDialogflowCxV3AdvancedSettings**](GoogleCloudDialogflowCxV3AdvancedSettings.md) |  | [optional] 
**description** | **String** | The description of the flow. The maximum length is 500 characters. If exceeded, the request is rejected. | [optional] 
**displayName** | **String** | Required. The human-readable name of the flow. | [optional] 
**eventHandlers** | [**[GoogleCloudDialogflowCxV3EventHandler]**](GoogleCloudDialogflowCxV3EventHandler.md) | A flow&#39;s event handlers serve two purposes: * They are responsible for handling events (e.g. no match, webhook errors) in the flow. * They are inherited by every page&#39;s event handlers, which can be used to handle common events regardless of the current page. Event handlers defined in the page have higher priority than those defined in the flow. Unlike transition_routes, these handlers are evaluated on a first-match basis. The first one that matches the event get executed, with the rest being ignored. | [optional] 
**knowledgeConnectorSettings** | [**GoogleCloudDialogflowCxV3KnowledgeConnectorSettings**](GoogleCloudDialogflowCxV3KnowledgeConnectorSettings.md) |  | [optional] 
**name** | **String** | The unique identifier of the flow. Format: &#x60;projects//locations//agents//flows/&#x60;. | [optional] 
**nluSettings** | [**GoogleCloudDialogflowCxV3NluSettings**](GoogleCloudDialogflowCxV3NluSettings.md) |  | [optional] 
**transitionRouteGroups** | **[String]** | A flow&#39;s transition route group serve two purposes: * They are responsible for matching the user&#39;s first utterances in the flow. * They are inherited by every page&#39;s transition route groups. Transition route groups defined in the page have higher priority than those defined in the flow. Format:&#x60;projects//locations//agents//flows//transitionRouteGroups/&#x60; or &#x60;projects//locations//agents//transitionRouteGroups/&#x60; for agent-level groups. | [optional] 
**transitionRoutes** | [**[GoogleCloudDialogflowCxV3TransitionRoute]**](GoogleCloudDialogflowCxV3TransitionRoute.md) | A flow&#39;s transition routes serve two purposes: * They are responsible for matching the user&#39;s first utterances in the flow. * They are inherited by every page&#39;s transition routes and can support use cases such as the user saying \&quot;help\&quot; or \&quot;can I talk to a human?\&quot;, which can be handled in a common way regardless of the current page. Transition routes defined in the page have higher priority than those defined in the flow. TransitionRoutes are evalauted in the following order: * TransitionRoutes with intent specified. * TransitionRoutes with only condition specified. TransitionRoutes with intent specified are inherited by pages in the flow. | [optional] 


