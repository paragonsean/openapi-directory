

# GatewayServiceMesh

Information about the Kubernetes Gateway API service mesh configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deployment** | **String** | Required. Name of the Kubernetes Deployment whose traffic is managed by the specified HTTPRoute and Service. |  [optional] |
|**httpRoute** | **String** | Required. Name of the Gateway API HTTPRoute. |  [optional] |
|**routeUpdateWaitTime** | **String** | Optional. The time to wait for route updates to propagate. The maximum configurable time is 3 hours, in seconds format. If unspecified, there is no wait time. |  [optional] |
|**service** | **String** | Required. Name of the Kubernetes Service. |  [optional] |
|**stableCutbackDuration** | **String** | Optional. The amount of time to migrate traffic back from the canary Service to the original Service during the stable phase deployment. If specified, must be between 15s and 3600s. If unspecified, there is no cutback time. |  [optional] |



