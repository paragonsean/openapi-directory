# GkeHubApi.ResourceOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectVersion** | **String** | Optional. The Connect agent version to use for connect_resources. Defaults to the latest GKE Connect version. The version must be a currently supported version, obsolete versions will be rejected. | [optional] 
**k8sVersion** | **String** | Optional. Major version of the Kubernetes cluster. This is only used to determine which version to use for the CustomResourceDefinition resources, &#x60;apiextensions/v1beta1&#x60; or&#x60;apiextensions/v1&#x60;. | [optional] 
**v1beta1Crd** | **Boolean** | Optional. Use &#x60;apiextensions/v1beta1&#x60; instead of &#x60;apiextensions/v1&#x60; for CustomResourceDefinition resources. This option should be set for clusters with Kubernetes apiserver versions &lt;1.16. | [optional] 


