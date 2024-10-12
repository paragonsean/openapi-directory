

# BareMetalControlPlaneConfig

Specifies the control plane configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiServerArgs** | [**List&lt;BareMetalApiServerArgument&gt;**](BareMetalApiServerArgument.md) | Customizes the default API server args. Only a subset of customized flags are supported. For the exact format, refer to the [API server documentation](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/). |  [optional] |
|**controlPlaneNodePoolConfig** | [**BareMetalControlPlaneNodePoolConfig**](BareMetalControlPlaneNodePoolConfig.md) |  |  [optional] |



