# MicrocksApiV17.Binding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinationName** | **String** | Name of destination for asynchronous messages of this operation | 
**destinationType** | **String** | Type of destination for asynchronous messages of this operation | [optional] 
**keyType** | **String** | Type of key for Kafka messages | [optional] 
**method** | **String** | HTTP method for WebSocket binding | [optional] 
**persistent** | **Boolean** | Persistent attribute for MQTT binding | [optional] 
**qoS** | **String** | Quality of Service attribute for MQTT binding | [optional] 
**type** | **String** | Protocol binding identifier | 



## Enum: TypeEnum


* `KAFKA` (value: `"KAFKA"`)

* `MQTT` (value: `"MQTT"`)

* `WS` (value: `"WS"`)

* `AMQP` (value: `"AMQP"`)

* `NATS` (value: `"NATS"`)

* `GOOGLEPUBSUB` (value: `"GOOGLEPUBSUB"`)




