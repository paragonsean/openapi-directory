

# TlsRouteRouteDestination

Describe the destination for traffic to be routed to.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**serviceName** | **String** | Required. The URL of a BackendService to route traffic to. |  [optional] |
|**weight** | **Integer** | Optional. Specifies the proportion of requests forwareded to the backend referenced by the service_name field. This is computed as: - weight/Sum(weights in destinations) Weights in all destinations does not need to sum up to 100. |  [optional] |



