

# GroupKind

This is a direct map to the Kubernetes GroupKind type [GroupKind](https://godoc.org/k8s.io/apimachinery/pkg/runtime/schema#GroupKind) and is used for identifying specific \"types\" of resources to restore.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**resourceGroup** | **String** | Optional. API group string of a Kubernetes resource, e.g. \&quot;apiextensions.k8s.io\&quot;, \&quot;storage.k8s.io\&quot;, etc. Note: use empty string for core API group |  [optional] |
|**resourceKind** | **String** | Optional. Kind of a Kubernetes resource, must be in UpperCamelCase (PascalCase) and singular form. E.g. \&quot;CustomResourceDefinition\&quot;, \&quot;StorageClass\&quot;, etc. |  [optional] |



