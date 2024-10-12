

# DeleteConnectionRequest

Request to delete a private service access connection. The call will fail if there are any managed service instances using this connection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consumerNetwork** | **String** | Required. The network that the consumer is using to connect with services. Must be in the form of projects/{project}/global/networks/{network} {project} is a project number, as in &#39;12345&#39; {network} is a network name. |  [optional] |



