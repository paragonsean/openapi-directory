# GkeHubApi.Namespace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. When the namespace was created. | [optional] [readonly] 
**deleteTime** | **String** | Output only. When the namespace was deleted. | [optional] [readonly] 
**labels** | **{String: String}** | Optional. Labels for this Namespace. | [optional] 
**name** | **String** | The resource name for the namespace &#x60;projects/{project}/locations/{location}/namespaces/{namespace}&#x60; | [optional] 
**namespaceLabels** | **{String: String}** | Optional. Namespace-level cluster namespace labels. These labels are applied to the related namespace of the member clusters bound to the parent Scope. Scope-level labels (&#x60;namespace_labels&#x60; in the Fleet Scope resource) take precedence over Namespace-level labels if they share a key. Keys and values must be Kubernetes-conformant. | [optional] 
**scope** | **String** | Required. Scope associated with the namespace | [optional] 
**state** | [**NamespaceLifecycleState**](NamespaceLifecycleState.md) |  | [optional] 
**uid** | **String** | Output only. Google-generated UUID for this resource. This is unique across all namespace resources. If a namespace resource is deleted and another resource with the same name is created, it gets a different uid. | [optional] [readonly] 
**updateTime** | **String** | Output only. When the namespace was last updated. | [optional] [readonly] 


