

# RBACRoleBinding

RBACRoleBinding represents a rbacrolebinding across the Fleet

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. When the rbacrolebinding was created. |  [optional] [readonly] |
|**deleteTime** | **String** | Output only. When the rbacrolebinding was deleted. |  [optional] [readonly] |
|**group** | **String** | group is the group, as seen by the kubernetes cluster. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Labels for this RBACRolebinding. |  [optional] |
|**name** | **String** | The resource name for the rbacrolebinding &#x60;projects/{project}/locations/{location}/scopes/{scope}/rbacrolebindings/{rbacrolebinding}&#x60; or &#x60;projects/{project}/locations/{location}/memberships/{membership}/rbacrolebindings/{rbacrolebinding}&#x60; |  [optional] |
|**role** | [**Role**](Role.md) |  |  [optional] |
|**state** | [**RBACRoleBindingLifecycleState**](RBACRoleBindingLifecycleState.md) |  |  [optional] |
|**uid** | **String** | Output only. Google-generated UUID for this resource. This is unique across all rbacrolebinding resources. If a rbacrolebinding resource is deleted and another resource with the same name is created, it gets a different uid. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. When the rbacrolebinding was last updated. |  [optional] [readonly] |
|**user** | **String** | user is the name of the user as seen by the kubernetes cluster, example \&quot;alice\&quot; or \&quot;alice@domain.tld\&quot; |  [optional] |



