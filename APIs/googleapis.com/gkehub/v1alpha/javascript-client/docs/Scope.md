# GkeHubApi.Scope

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. When the scope was created. | [optional] [readonly] 
**deleteTime** | **String** | Output only. When the scope was deleted. | [optional] [readonly] 
**labels** | **{String: String}** | Optional. Labels for this Scope. | [optional] 
**name** | **String** | The resource name for the scope &#x60;projects/{project}/locations/{location}/scopes/{scope}&#x60; | [optional] 
**namespaceLabels** | **{String: String}** | Optional. Scope-level cluster namespace labels. For the member clusters bound to the Scope, these labels are applied to each namespace under the Scope. Scope-level labels take precedence over Namespace-level labels (&#x60;namespace_labels&#x60; in the Fleet Namespace resource) if they share a key. Keys and values must be Kubernetes-conformant. | [optional] 
**state** | [**ScopeLifecycleState**](ScopeLifecycleState.md) |  | [optional] 
**uid** | **String** | Output only. Google-generated UUID for this resource. This is unique across all scope resources. If a scope resource is deleted and another resource with the same name is created, it gets a different uid. | [optional] [readonly] 
**updateTime** | **String** | Output only. When the scope was last updated. | [optional] [readonly] 


