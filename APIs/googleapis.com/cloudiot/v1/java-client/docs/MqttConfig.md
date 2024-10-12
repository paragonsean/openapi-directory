

# MqttConfig

The configuration of MQTT for a device registry.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mqttEnabledState** | [**MqttEnabledStateEnum**](#MqttEnabledStateEnum) | If enabled, allows connections using the MQTT protocol. Otherwise, MQTT connections to this registry will fail. |  [optional] |



## Enum: MqttEnabledStateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;MQTT_STATE_UNSPECIFIED&quot; |
| ENABLED | &quot;MQTT_ENABLED&quot; |
| DISABLED | &quot;MQTT_DISABLED&quot; |



