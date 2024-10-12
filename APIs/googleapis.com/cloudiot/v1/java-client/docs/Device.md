

# Device

The device resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blocked** | **Boolean** | If a device is blocked, connections or requests from this device will fail. Can be used to temporarily prevent the device from connecting if, for example, the sensor is generating bad data and needs maintenance. |  [optional] |
|**config** | [**DeviceConfig**](DeviceConfig.md) |  |  [optional] |
|**credentials** | [**List&lt;DeviceCredential&gt;**](DeviceCredential.md) | The credentials used to authenticate this device. To allow credential rotation without interruption, multiple device credentials can be bound to this device. No more than 3 credentials can be bound to a single device at a time. When new credentials are added to a device, they are verified against the registry credentials. For details, see the description of the &#x60;DeviceRegistry.credentials&#x60; field. |  [optional] |
|**gatewayConfig** | [**GatewayConfig**](GatewayConfig.md) |  |  [optional] |
|**id** | **String** | The user-defined device identifier. The device ID must be unique within a device registry. |  [optional] |
|**lastConfigAckTime** | **String** | [Output only] The last time a cloud-to-device config version acknowledgment was received from the device. This field is only for configurations sent through MQTT. |  [optional] |
|**lastConfigSendTime** | **String** | [Output only] The last time a cloud-to-device config version was sent to the device. |  [optional] |
|**lastErrorStatus** | [**Status**](Status.md) |  |  [optional] |
|**lastErrorTime** | **String** | [Output only] The time the most recent error occurred, such as a failure to publish to Cloud Pub/Sub. This field is the timestamp of &#39;last_error_status&#39;. |  [optional] |
|**lastEventTime** | **String** | [Output only] The last time a telemetry event was received. Timestamps are periodically collected and written to storage; they may be stale by a few minutes. |  [optional] |
|**lastHeartbeatTime** | **String** | [Output only] The last time an MQTT &#x60;PINGREQ&#x60; was received. This field applies only to devices connecting through MQTT. MQTT clients usually only send &#x60;PINGREQ&#x60; messages if the connection is idle, and no other messages have been sent. Timestamps are periodically collected and written to storage; they may be stale by a few minutes. |  [optional] |
|**lastStateTime** | **String** | [Output only] The last time a state event was received. Timestamps are periodically collected and written to storage; they may be stale by a few minutes. |  [optional] |
|**logLevel** | [**LogLevelEnum**](#LogLevelEnum) | **Beta Feature** The logging verbosity for device activity. If unspecified, DeviceRegistry.log_level will be used. |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | The metadata key-value pairs assigned to the device. This metadata is not interpreted or indexed by Cloud IoT Core. It can be used to add contextual information for the device. Keys must conform to the regular expression a-zA-Z+ and be less than 128 bytes in length. Values are free-form strings. Each value must be less than or equal to 32 KB in size. The total size of all keys and values must be less than 256 KB, and the maximum number of key-value pairs is 500. |  [optional] |
|**name** | **String** | The resource path name. For example, &#x60;projects/p1/locations/us-central1/registries/registry0/devices/dev0&#x60; or &#x60;projects/p1/locations/us-central1/registries/registry0/devices/{num_id}&#x60;. When &#x60;name&#x60; is populated as a response from the service, it always ends in the device numeric ID. |  [optional] |
|**numId** | **String** | [Output only] A server-defined unique numeric ID for the device. This is a more compact way to identify devices, and it is globally unique. |  [optional] |
|**state** | [**DeviceState**](DeviceState.md) |  |  [optional] |



## Enum: LogLevelEnum

| Name | Value |
|---- | -----|
| LOG_LEVEL_UNSPECIFIED | &quot;LOG_LEVEL_UNSPECIFIED&quot; |
| NONE | &quot;NONE&quot; |
| ERROR | &quot;ERROR&quot; |
| INFO | &quot;INFO&quot; |
| DEBUG | &quot;DEBUG&quot; |



