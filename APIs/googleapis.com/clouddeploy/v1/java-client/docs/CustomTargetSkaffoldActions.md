

# CustomTargetSkaffoldActions

CustomTargetSkaffoldActions represents the `CustomTargetType` configuration using Skaffold custom actions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deployAction** | **String** | Required. The Skaffold custom action responsible for deploy operations. |  [optional] |
|**includeSkaffoldModules** | [**List&lt;SkaffoldModules&gt;**](SkaffoldModules.md) | Optional. List of Skaffold modules Cloud Deploy will include in the Skaffold Config as required before performing diagnose. |  [optional] |
|**renderAction** | **String** | Optional. The Skaffold custom action responsible for render operations. If not provided then Cloud Deploy will perform the render operations via &#x60;skaffold render&#x60;. |  [optional] |



