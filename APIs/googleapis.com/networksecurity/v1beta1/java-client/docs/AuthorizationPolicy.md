

# AuthorizationPolicy

AuthorizationPolicy is a resource that specifies how a server should authorize incoming connections. This resource in itself does not change the configuration unless it's attached to a target https proxy or endpoint config selector resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | Required. The action to take when a rule match is found. Possible values are \&quot;ALLOW\&quot; or \&quot;DENY\&quot;. |  [optional] |
|**createTime** | **String** | Output only. The timestamp when the resource was created. |  [optional] [readonly] |
|**description** | **String** | Optional. Free-text description of the resource. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Set of label tags associated with the AuthorizationPolicy resource. |  [optional] |
|**name** | **String** | Required. Name of the AuthorizationPolicy resource. It matches pattern &#x60;projects/{project}/locations/{location}/authorizationPolicies/&#x60;. |  [optional] |
|**rules** | [**List&lt;Rule&gt;**](Rule.md) | Optional. List of rules to match. Note that at least one of the rules must match in order for the action specified in the &#39;action&#39; field to be taken. A rule is a match if there is a matching source and destination. If left blank, the action specified in the &#x60;action&#x60; field will be applied on every request. |  [optional] |
|**updateTime** | **String** | Output only. The timestamp when the resource was updated. |  [optional] [readonly] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| ACTION_UNSPECIFIED | &quot;ACTION_UNSPECIFIED&quot; |
| ALLOW | &quot;ALLOW&quot; |
| DENY | &quot;DENY&quot; |



