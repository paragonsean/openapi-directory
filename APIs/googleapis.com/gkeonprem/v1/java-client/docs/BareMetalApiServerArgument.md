

# BareMetalApiServerArgument

Represents an arg name->value pair. Only a subset of customized flags are supported. For the exact format, refer to the [API server documentation](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**argument** | **String** | Required. The argument name as it appears on the API Server command line, make sure to remove the leading dashes. |  [optional] |
|**value** | **String** | Required. The value of the arg as it will be passed to the API Server command line. |  [optional] |



