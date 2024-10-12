# CloudIoTApi.GatewayConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gatewayAuthMethod** | **String** | Indicates how to authorize and/or authenticate devices to access the gateway. | [optional] 
**gatewayType** | **String** | Indicates whether the device is a gateway. | [optional] 
**lastAccessedGatewayId** | **String** | [Output only] The ID of the gateway the device accessed most recently. | [optional] 
**lastAccessedGatewayTime** | **String** | [Output only] The most recent time at which the device accessed the gateway specified in &#x60;last_accessed_gateway&#x60;. | [optional] 



## Enum: GatewayAuthMethodEnum


* `GATEWAY_AUTH_METHOD_UNSPECIFIED` (value: `"GATEWAY_AUTH_METHOD_UNSPECIFIED"`)

* `ASSOCIATION_ONLY` (value: `"ASSOCIATION_ONLY"`)

* `DEVICE_AUTH_TOKEN_ONLY` (value: `"DEVICE_AUTH_TOKEN_ONLY"`)

* `ASSOCIATION_AND_DEVICE_AUTH_TOKEN` (value: `"ASSOCIATION_AND_DEVICE_AUTH_TOKEN"`)





## Enum: GatewayTypeEnum


* `GATEWAY_TYPE_UNSPECIFIED` (value: `"GATEWAY_TYPE_UNSPECIFIED"`)

* `GATEWAY` (value: `"GATEWAY"`)

* `NON_GATEWAY` (value: `"NON_GATEWAY"`)




