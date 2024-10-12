

# NetworkPolicy

Configuration options for the NetworkPolicy feature. https://kubernetes.io/docs/concepts/services-networking/networkpolicies/

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Whether network policy is enabled on the cluster. |  [optional] |
|**provider** | [**ProviderEnum**](#ProviderEnum) | The selected network policy provider. |  [optional] |



## Enum: ProviderEnum

| Name | Value |
|---- | -----|
| PROVIDER_UNSPECIFIED | &quot;PROVIDER_UNSPECIFIED&quot; |
| CALICO | &quot;CALICO&quot; |



