

# IngressConfig

Describes public connectivity configuration for the network.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**layer4** | [**List&lt;Layer4IngressConfig&gt;**](Layer4IngressConfig.md) | Configuration for layer4 public connectivity for this network. |  [optional] |
|**publicIPAddress** | **String** | The public IP address for reaching this network. |  [optional] [readonly] |
|**qosLevel** | [**QosLevelEnum**](#QosLevelEnum) | The QoS tier for ingress. |  [optional] |



## Enum: QosLevelEnum

| Name | Value |
|---- | -----|
| BRONZE | &quot;Bronze&quot; |



