

# Binding

Protocol binding details for asynchronous operations

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destinationName** | **String** | Name of destination for asynchronous messages of this operation |  |
|**destinationType** | **String** | Type of destination for asynchronous messages of this operation |  [optional] |
|**keyType** | **String** | Type of key for Kafka messages |  [optional] |
|**method** | **String** | HTTP method for WebSocket binding |  [optional] |
|**persistent** | **Boolean** | Persistent attribute for MQTT binding |  [optional] |
|**qoS** | **String** | Quality of Service attribute for MQTT binding |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Protocol binding identifier |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| KAFKA | &quot;KAFKA&quot; |
| MQTT | &quot;MQTT&quot; |
| WS | &quot;WS&quot; |
| AMQP | &quot;AMQP&quot; |
| NATS | &quot;NATS&quot; |
| GOOGLEPUBSUB | &quot;GOOGLEPUBSUB&quot; |



