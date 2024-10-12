

# User

A user associated with the broker. For Amazon MQ for RabbitMQ brokers, one and only one administrative user is accepted and created when a broker is first provisioned. All subsequent broker users are created by making RabbitMQ API calls directly to brokers or via the RabbitMQ web console.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consoleAccess** | [**Boolean**](Boolean.md) |  |  [optional] |
|**groups** | [**List**](List.md) |  |  [optional] |
|**password** | [**String**](String.md) |  |  |
|**username** | [**String**](String.md) |  |  |
|**replicationUser** | [**Boolean**](Boolean.md) |  |  [optional] |



