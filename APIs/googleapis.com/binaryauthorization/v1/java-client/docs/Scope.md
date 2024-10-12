

# Scope

A scope specifier for `CheckSet` objects.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kubernetesNamespace** | **String** | Optional. Matches all Kubernetes service accounts in the provided namespace, unless a more specific &#x60;kubernetes_service_account&#x60; scope already matched. |  [optional] |
|**kubernetesServiceAccount** | **String** | Optional. Matches a single Kubernetes service account, e.g. &#x60;my-namespace:my-service-account&#x60;. &#x60;kubernetes_service_account&#x60; scope is always more specific than &#x60;kubernetes_namespace&#x60; scope for the same namespace. |  [optional] |



