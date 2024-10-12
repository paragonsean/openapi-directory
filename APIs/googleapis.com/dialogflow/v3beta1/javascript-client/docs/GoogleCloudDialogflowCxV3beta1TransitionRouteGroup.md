# DialogflowApi.GoogleCloudDialogflowCxV3beta1TransitionRouteGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | Required. The human-readable name of the transition route group, unique within the flow. The display name can be no longer than 30 characters. | [optional] 
**name** | **String** | The unique identifier of the transition route group. TransitionRouteGroups.CreateTransitionRouteGroup populates the name automatically. Format: &#x60;projects//locations//agents//flows//transitionRouteGroups/&#x60; or &#x60;projects//locations//agents//transitionRouteGroups/&#x60; for agent-level groups. | [optional] 
**transitionRoutes** | [**[GoogleCloudDialogflowCxV3beta1TransitionRoute]**](GoogleCloudDialogflowCxV3beta1TransitionRoute.md) | Transition routes associated with the TransitionRouteGroup. | [optional] 


