

# CheckSet

A conjunction of policy checks, scoped to a particular namespace or Kubernetes service account. In order for evaluation of a `CheckSet` to return \"allowed\" for a given image in a given Pod, one of the following conditions must be satisfied: * The image is explicitly exempted by an entry in `image_allowlist`, OR * ALL of the `checks` evaluate to \"allowed\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checks** | [**List&lt;Check&gt;**](Check.md) | Optional. The checks to apply. The ultimate result of evaluating the check set will be \&quot;allow\&quot; if and only if every check in &#x60;checks&#x60; evaluates to \&quot;allow\&quot;. If &#x60;checks&#x60; is empty, the default behavior is \&quot;always allow\&quot;. |  [optional] |
|**displayName** | **String** | Optional. A user-provided name for this &#x60;CheckSet&#x60;. This field has no effect on the policy evaluation behavior except to improve readability of messages in evaluation results. |  [optional] |
|**imageAllowlist** | [**ImageAllowlist**](ImageAllowlist.md) |  |  [optional] |
|**scope** | [**Scope**](Scope.md) |  |  [optional] |



