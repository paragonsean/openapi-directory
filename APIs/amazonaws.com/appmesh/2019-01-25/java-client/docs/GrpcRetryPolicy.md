

# GrpcRetryPolicy

An object that represents a retry policy. Specify at least one value for at least one of the types of <code>RetryEvents</code>, a value for <code>maxRetries</code>, and a value for <code>perRetryTimeout</code>. Both <code>server-error</code> and <code>gateway-error</code> under <code>httpRetryEvents</code> include the Envoy <code>reset</code> policy. For more information on the <code>reset</code> policy, see the <a href=\"https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/router_filter#x-envoy-retry-on\">Envoy documentation</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**grpcRetryEvents** | [**List**](List.md) |  |  [optional] |
|**httpRetryEvents** | [**List**](List.md) |  |  [optional] |
|**maxRetries** | [**Integer**](Integer.md) |  |  |
|**perRetryTimeout** | [**GrpcRetryPolicyPerRetryTimeout**](GrpcRetryPolicyPerRetryTimeout.md) |  |  |
|**tcpRetryEvents** | [**List**](List.md) |  |  [optional] |



