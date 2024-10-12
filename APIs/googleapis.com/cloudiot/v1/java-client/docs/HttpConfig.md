

# HttpConfig

The configuration of the HTTP bridge for a device registry.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**httpEnabledState** | [**HttpEnabledStateEnum**](#HttpEnabledStateEnum) | If enabled, allows devices to use DeviceService via the HTTP protocol. Otherwise, any requests to DeviceService will fail for this registry. |  [optional] |



## Enum: HttpEnabledStateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;HTTP_STATE_UNSPECIFIED&quot; |
| ENABLED | &quot;HTTP_ENABLED&quot; |
| DISABLED | &quot;HTTP_DISABLED&quot; |



