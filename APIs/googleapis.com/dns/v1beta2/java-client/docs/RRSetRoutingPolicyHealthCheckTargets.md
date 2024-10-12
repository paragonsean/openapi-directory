

# RRSetRoutingPolicyHealthCheckTargets

HealthCheckTargets describes endpoints to health-check when responding to Routing Policy queries. Only the healthy endpoints will be included in the response. Only one of internal_load_balancer and external_endpoints should be set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**externalEndpoints** | **List&lt;String&gt;** | The Internet IP addresses to be health checked. The format matches the format of ResourceRecordSet.rrdata as defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1) |  [optional] |
|**internalLoadBalancers** | [**List&lt;RRSetRoutingPolicyLoadBalancerTarget&gt;**](RRSetRoutingPolicyLoadBalancerTarget.md) | Configuration for internal load balancers to be health checked. |  [optional] |



