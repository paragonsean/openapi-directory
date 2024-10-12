

# DiscoveryEndpoint

Endpoints on each network, for Redis clients to connect to the cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | Output only. Address of the exposed Redis endpoint used by clients to connect to the service. The address could be either IP or hostname. |  [optional] [readonly] |
|**port** | **Integer** | Output only. The port number of the exposed Redis endpoint. |  [optional] [readonly] |
|**pscConfig** | [**PscConfig**](PscConfig.md) |  |  [optional] |



