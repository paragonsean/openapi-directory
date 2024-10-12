

# NetworkConfig

Regional Network Config.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**egressIps** | **List&lt;String&gt;** | Output only. Egress IPs |  [optional] [readonly] |
|**egressMode** | [**EgressModeEnum**](#EgressModeEnum) | Optional. Egress mode for the network. |  [optional] |



## Enum: EgressModeEnum

| Name | Value |
|---- | -----|
| NETWORK_EGRESS_MODE_UNSPECIFIED | &quot;NETWORK_EGRESS_MODE_UNSPECIFIED&quot; |
| AUTO_IP | &quot;AUTO_IP&quot; |
| STATIC_IP | &quot;STATIC_IP&quot; |



