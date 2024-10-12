

# ApplicationGatewayProbePropertiesFormat

Properties of probe of application gateway

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**host** | **String** | Gets or sets the host to send probe to  |  [optional] |
|**interval** | **Integer** | Gets or sets probing interval in seconds  |  [optional] |
|**path** | **String** | Gets or sets the relative path of probe  |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Gets or sets the protocol |  [optional] |
|**provisioningState** | **String** | Gets or sets Provisioning state of the backend http settings resource Updating/Deleting/Failed |  [optional] |
|**timeout** | **Integer** | Gets or sets probing timeout in seconds  |  [optional] |
|**unhealthyThreshold** | **Integer** | Gets or sets probing unhealthy threshold  |  [optional] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;Http&quot; |
| HTTPS | &quot;Https&quot; |



