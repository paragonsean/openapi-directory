# CloudDnsApi.RRSetRoutingPolicyHealthCheckTargets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**externalEndpoints** | **[String]** | The Internet IP addresses to be health checked. The format matches the format of ResourceRecordSet.rrdata as defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1) | [optional] 
**internalLoadBalancers** | [**[RRSetRoutingPolicyLoadBalancerTarget]**](RRSetRoutingPolicyLoadBalancerTarget.md) | Configuration for internal load balancers to be health checked. | [optional] 


