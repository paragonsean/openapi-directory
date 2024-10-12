# DialogflowApi.GoogleCloudDialogflowCxV3beta1Page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advancedSettings** | [**GoogleCloudDialogflowCxV3beta1AdvancedSettings**](GoogleCloudDialogflowCxV3beta1AdvancedSettings.md) |  | [optional] 
**description** | **String** | The description of the page. The maximum length is 500 characters. | [optional] 
**displayName** | **String** | Required. The human-readable name of the page, unique within the flow. | [optional] 
**entryFulfillment** | [**GoogleCloudDialogflowCxV3beta1Fulfillment**](GoogleCloudDialogflowCxV3beta1Fulfillment.md) |  | [optional] 
**eventHandlers** | [**[GoogleCloudDialogflowCxV3beta1EventHandler]**](GoogleCloudDialogflowCxV3beta1EventHandler.md) | Handlers associated with the page to handle events such as webhook errors, no match or no input. | [optional] 
**form** | [**GoogleCloudDialogflowCxV3beta1Form**](GoogleCloudDialogflowCxV3beta1Form.md) |  | [optional] 
**knowledgeConnectorSettings** | [**GoogleCloudDialogflowCxV3beta1KnowledgeConnectorSettings**](GoogleCloudDialogflowCxV3beta1KnowledgeConnectorSettings.md) |  | [optional] 
**name** | **String** | The unique identifier of the page. Required for the Pages.UpdatePage method. Pages.CreatePage populates the name automatically. Format: &#x60;projects//locations//agents//flows//pages/&#x60;. | [optional] 
**transitionRouteGroups** | **[String]** | Ordered list of &#x60;TransitionRouteGroups&#x60; added to the page. Transition route groups must be unique within a page. If the page links both flow-level transition route groups and agent-level transition route groups, the flow-level ones will have higher priority and will be put before the agent-level ones. * If multiple transition routes within a page scope refer to the same intent, then the precedence order is: page&#39;s transition route -&gt; page&#39;s transition route group -&gt; flow&#39;s transition routes. * If multiple transition route groups within a page contain the same intent, then the first group in the ordered list takes precedence. Format:&#x60;projects//locations//agents//flows//transitionRouteGroups/&#x60; or &#x60;projects//locations//agents//transitionRouteGroups/&#x60; for agent-level groups. | [optional] 
**transitionRoutes** | [**[GoogleCloudDialogflowCxV3beta1TransitionRoute]**](GoogleCloudDialogflowCxV3beta1TransitionRoute.md) | A list of transitions for the transition rules of this page. They route the conversation to another page in the same flow, or another flow. When we are in a certain page, the TransitionRoutes are evalauted in the following order: * TransitionRoutes defined in the page with intent specified. * TransitionRoutes defined in the transition route groups with intent specified. * TransitionRoutes defined in flow with intent specified. * TransitionRoutes defined in the transition route groups with intent specified. * TransitionRoutes defined in the page with only condition specified. * TransitionRoutes defined in the transition route groups with only condition specified. | [optional] 


