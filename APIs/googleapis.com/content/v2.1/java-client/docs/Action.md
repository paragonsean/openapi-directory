

# Action

An actionable step that can be executed to solve the issue.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**builtinSimpleAction** | [**BuiltInSimpleAction**](BuiltInSimpleAction.md) |  |  [optional] |
|**buttonLabel** | **String** | Label of the action button. |  [optional] |
|**externalAction** | [**ExternalAction**](ExternalAction.md) |  |  [optional] |
|**isAvailable** | **Boolean** | Controlling whether the button is active or disabled. The value is &#39;false&#39; when the action was already requested or is not available. If the action is not available then a reason will be present. If (your) third-party application shows a disabled button for action that is not available, then it should also show reasons. |  [optional] |
|**reasons** | [**List&lt;ActionReason&gt;**](ActionReason.md) | List of reasons why the action is not available. The list of reasons is empty if the action is available. If there is only one reason, it can be displayed next to the disabled button. If there are more reasons, all of them should be displayed, for example in a pop-up dialog. |  [optional] |



