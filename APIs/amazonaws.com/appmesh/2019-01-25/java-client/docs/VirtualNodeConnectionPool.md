

# VirtualNodeConnectionPool

<p>An object that represents the type of virtual node connection pool.</p> <p>Only one protocol is used at a time and should be the same protocol as the one chosen under port mapping.</p> <p>If not present the default value for <code>maxPendingRequests</code> is <code>2147483647</code>.</p> <p/>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**grpc** | [**VirtualNodeConnectionPoolGrpc**](VirtualNodeConnectionPoolGrpc.md) |  |  [optional] |
|**http** | [**VirtualNodeConnectionPoolHttp**](VirtualNodeConnectionPoolHttp.md) |  |  [optional] |
|**http2** | [**VirtualNodeConnectionPoolHttp2**](VirtualNodeConnectionPoolHttp2.md) |  |  [optional] |
|**tcp** | [**VirtualNodeConnectionPoolTcp**](VirtualNodeConnectionPoolTcp.md) |  |  [optional] |



