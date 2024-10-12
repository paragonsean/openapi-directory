

# VirtualGatewayConnectionPool

<p>An object that represents the type of virtual gateway connection pool.</p> <p>Only one protocol is used at a time and should be the same protocol as the one chosen under port mapping.</p> <p>If not present the default value for <code>maxPendingRequests</code> is <code>2147483647</code>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**grpc** | [**VirtualGatewayConnectionPoolGrpc**](VirtualGatewayConnectionPoolGrpc.md) |  |  [optional] |
|**http** | [**VirtualGatewayConnectionPoolHttp**](VirtualGatewayConnectionPoolHttp.md) |  |  [optional] |
|**http2** | [**VirtualGatewayConnectionPoolHttp2**](VirtualGatewayConnectionPoolHttp2.md) |  |  [optional] |



