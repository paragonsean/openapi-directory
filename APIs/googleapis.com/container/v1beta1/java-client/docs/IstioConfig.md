

# IstioConfig

Configuration options for Istio addon.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**auth** | [**AuthEnum**](#AuthEnum) | The specified Istio auth mode, either none, or mutual TLS. |  [optional] |
|**disabled** | **Boolean** | Whether Istio is enabled for this cluster. |  [optional] |



## Enum: AuthEnum

| Name | Value |
|---- | -----|
| NONE | &quot;AUTH_NONE&quot; |
| MUTUAL_TLS | &quot;AUTH_MUTUAL_TLS&quot; |



