

# ApplicationGatewayProbePropertiesFormat

Properties of probe of application gateway

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**host** | **String** | Host to send probe to  |  [optional] |
|**interval** | **Integer** | Probing interval in seconds  |  [optional] |
|**path** | **String** | Relative path of probe  |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Protocol |  [optional] |
|**provisioningState** | **String** | Provisioning state of the backend http settings resource Updating/Deleting/Failed |  [optional] |
|**timeout** | **Integer** | Probing timeout in seconds  |  [optional] |
|**unhealthyThreshold** | **Integer** | Probing unhealthy threshold  |  [optional] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;Http&quot; |
| HTTPS | &quot;Https&quot; |



