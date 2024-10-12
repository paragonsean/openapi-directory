# BinaryAuthorizationApi.CheckSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checks** | [**[Check]**](Check.md) | Optional. The checks to apply. The ultimate result of evaluating the check set will be \&quot;allow\&quot; if and only if every check in &#x60;checks&#x60; evaluates to \&quot;allow\&quot;. If &#x60;checks&#x60; is empty, the default behavior is \&quot;always allow\&quot;. | [optional] 
**displayName** | **String** | Optional. A user-provided name for this &#x60;CheckSet&#x60;. This field has no effect on the policy evaluation behavior except to improve readability of messages in evaluation results. | [optional] 
**imageAllowlist** | [**ImageAllowlist**](ImageAllowlist.md) |  | [optional] 
**scope** | [**Scope**](Scope.md) |  | [optional] 


