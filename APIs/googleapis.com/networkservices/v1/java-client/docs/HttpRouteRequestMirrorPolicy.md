

# HttpRouteRequestMirrorPolicy

Specifies the policy on how requests are shadowed to a separate mirrored destination service. The proxy does not wait for responses from the shadow service. Prior to sending traffic to the shadow service, the host/authority header is suffixed with -shadow.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destination** | [**HttpRouteDestination**](HttpRouteDestination.md) |  |  [optional] |
|**mirrorPercent** | **Float** | Optional. The percentage of requests to get mirrored to the desired destination. |  [optional] |



