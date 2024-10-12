

# PodResult

Result of evaluating the whole GKE policy for one Pod.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**imageResults** | [**List&lt;ImageResult&gt;**](ImageResult.md) | Per-image details. |  [optional] |
|**kubernetesNamespace** | **String** | The Kubernetes namespace of the Pod. |  [optional] |
|**kubernetesServiceAccount** | **String** | The Kubernetes service account of the Pod. |  [optional] |
|**podName** | **String** | The name of the Pod. |  [optional] |
|**verdict** | [**VerdictEnum**](#VerdictEnum) | The result of evaluating this Pod. |  [optional] |



## Enum: VerdictEnum

| Name | Value |
|---- | -----|
| POD_VERDICT_UNSPECIFIED | &quot;POD_VERDICT_UNSPECIFIED&quot; |
| CONFORMANT | &quot;CONFORMANT&quot; |
| NON_CONFORMANT | &quot;NON_CONFORMANT&quot; |
| ERROR | &quot;ERROR&quot; |



