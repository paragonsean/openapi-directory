

# GatewayConfig

Gateway-related configuration and state.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gatewayAuthMethod** | [**GatewayAuthMethodEnum**](#GatewayAuthMethodEnum) | Indicates how to authorize and/or authenticate devices to access the gateway. |  [optional] |
|**gatewayType** | [**GatewayTypeEnum**](#GatewayTypeEnum) | Indicates whether the device is a gateway. |  [optional] |
|**lastAccessedGatewayId** | **String** | [Output only] The ID of the gateway the device accessed most recently. |  [optional] |
|**lastAccessedGatewayTime** | **String** | [Output only] The most recent time at which the device accessed the gateway specified in &#x60;last_accessed_gateway&#x60;. |  [optional] |



## Enum: GatewayAuthMethodEnum

| Name | Value |
|---- | -----|
| GATEWAY_AUTH_METHOD_UNSPECIFIED | &quot;GATEWAY_AUTH_METHOD_UNSPECIFIED&quot; |
| ASSOCIATION_ONLY | &quot;ASSOCIATION_ONLY&quot; |
| DEVICE_AUTH_TOKEN_ONLY | &quot;DEVICE_AUTH_TOKEN_ONLY&quot; |
| ASSOCIATION_AND_DEVICE_AUTH_TOKEN | &quot;ASSOCIATION_AND_DEVICE_AUTH_TOKEN&quot; |



## Enum: GatewayTypeEnum

| Name | Value |
|---- | -----|
| GATEWAY_TYPE_UNSPECIFIED | &quot;GATEWAY_TYPE_UNSPECIFIED&quot; |
| GATEWAY | &quot;GATEWAY&quot; |
| NON_GATEWAY | &quot;NON_GATEWAY&quot; |



