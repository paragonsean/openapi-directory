

# BareMetalAdminControlPlaneConfig

BareMetalAdminControlPlaneConfig specifies the control plane configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiServerArgs** | [**List&lt;BareMetalAdminApiServerArgument&gt;**](BareMetalAdminApiServerArgument.md) | Customizes the default API server args. Only a subset of customized flags are supported. Please refer to the API server documentation below to know the exact format: https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/ |  [optional] |
|**controlPlaneNodePoolConfig** | [**BareMetalAdminControlPlaneNodePoolConfig**](BareMetalAdminControlPlaneNodePoolConfig.md) |  |  [optional] |



