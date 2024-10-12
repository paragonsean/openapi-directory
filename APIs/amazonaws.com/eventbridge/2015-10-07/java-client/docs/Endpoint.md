

# Endpoint

A global endpoint used to improve your application's availability by making it regional-fault tolerant. For more information about global endpoints, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-global-endpoints.html\">Making applications Regional-fault tolerant with global endpoints and event replication</a> in the Amazon EventBridge User Guide.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  [optional] |
|**description** | [**String**](String.md) |  |  [optional] |
|**arn** | [**String**](String.md) |  |  [optional] |
|**routingConfig** | [**EndpointRoutingConfig**](EndpointRoutingConfig.md) |  |  [optional] |
|**replicationConfig** | [**EndpointReplicationConfig**](EndpointReplicationConfig.md) |  |  [optional] |
|**eventBuses** | [**List**](List.md) |  |  [optional] |
|**roleArn** | [**String**](String.md) |  |  [optional] |
|**endpointId** | [**String**](String.md) |  |  [optional] |
|**endpointUrl** | [**String**](String.md) |  |  [optional] |
|**state** | [**EndpointState**](EndpointState.md) |  |  [optional] |
|**stateReason** | [**String**](String.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastModifiedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |



