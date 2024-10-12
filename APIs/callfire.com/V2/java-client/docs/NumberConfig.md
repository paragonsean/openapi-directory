

# NumberConfig

Represents the configuration of a phone number purchased by user. You can configure number to accept inbound calls, play sounds to customer, make a transfer or setup an IVR script to interact with customer. See [CallFire IVR](https://www.callfire.com/products/ivr) for more info

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callTrackingConfig** | [**CallTrackingConfig**](CallTrackingConfig.md) |  |  [optional] |
|**configType** | [**ConfigTypeEnum**](#ConfigTypeEnum) | A type of config. Available values: TRACKING, IVR |  [optional] |
|**ivrInboundConfig** | [**IvrInboundConfig**](IvrInboundConfig.md) |  |  [optional] |
|**number** | **String** | Phone number in E.164 format (11-digit). Example: 12132000384 |  [optional] |
|**textInboundConfig** | [**TextInboundConfig**](TextInboundConfig.md) |  |  [optional] |



## Enum: ConfigTypeEnum

| Name | Value |
|---- | -----|
| IVR | &quot;IVR&quot; |
| TRACKING | &quot;TRACKING&quot; |



