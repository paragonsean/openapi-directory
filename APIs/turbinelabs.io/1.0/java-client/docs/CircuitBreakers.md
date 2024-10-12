

# CircuitBreakers

Provides limits on various parameters to protect clusters against sudden surges in traffic. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxConnections** | **Integer** | Maximum number of connections that will be established to all instances in a cluster within a proxy. If set to 0, no new connections will be created. If not specified, defaults to 1024.  |  [optional] |
|**maxPendingRequests** | **Integer** | Maximum number of requests that will be queued while waiting on a connection pool to a cluster within a proxy. If set to 0, no requests will be queued. If not specified, defaults to 1024.  |  [optional] |
|**maxRequests** | **Integer** | Maximum number of requests that can be outstanding to all instances in a cluster within  a proxy. Only applicable to HTTP/2 traffic since HTTP/1.1 clusters are governed by the maximum connections circuit breaker. If set to 0, no requests will be made. If not specified, defaults to 1024.  |  [optional] |
|**maxRetries** | **Integer** | Maximum number of retries that can be outstanding to all instances in a cluster within a proxy. If set to 0, requests will not be retried. If not specified, defaults to 3.  |  [optional] |



