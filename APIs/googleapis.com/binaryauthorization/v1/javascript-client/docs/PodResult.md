# BinaryAuthorizationApi.PodResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imageResults** | [**[ImageResult]**](ImageResult.md) | Per-image details. | [optional] 
**kubernetesNamespace** | **String** | The Kubernetes namespace of the Pod. | [optional] 
**kubernetesServiceAccount** | **String** | The Kubernetes service account of the Pod. | [optional] 
**podName** | **String** | The name of the Pod. | [optional] 
**verdict** | **String** | The result of evaluating this Pod. | [optional] 



## Enum: VerdictEnum


* `POD_VERDICT_UNSPECIFIED` (value: `"POD_VERDICT_UNSPECIFIED"`)

* `CONFORMANT` (value: `"CONFORMANT"`)

* `NON_CONFORMANT` (value: `"NON_CONFORMANT"`)

* `ERROR` (value: `"ERROR"`)




