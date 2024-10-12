

# NetworkBinding

Details on the network bindings between a container and its host container instance. After a task reaches the <code>RUNNING</code> status, manual and automatic host and container port assignments are visible in the <code>networkBindings</code> section of <a>DescribeTasks</a> API responses.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bindIP** | [**String**](String.md) |  |  [optional] |
|**containerPort** | [**Integer**](Integer.md) |  |  [optional] |
|**hostPort** | [**Integer**](Integer.md) |  |  [optional] |
|**protocol** | [**TransportProtocol**](TransportProtocol.md) |  |  [optional] |
|**containerPortRange** | [**String**](String.md) |  |  [optional] |
|**hostPortRange** | [**String**](String.md) |  |  [optional] |



