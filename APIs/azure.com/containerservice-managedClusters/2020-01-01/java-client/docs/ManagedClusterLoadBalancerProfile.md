

# ManagedClusterLoadBalancerProfile

Profile of the managed cluster load balancer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allocatedOutboundPorts** | **Integer** | Desired number of allocated SNAT ports per VM. Allowed values must be in the range of 0 to 64000 (inclusive). The default value is 0 which results in Azure dynamically allocating ports. |  [optional] |
|**effectiveOutboundIPs** | [**List&lt;ResourceReference&gt;**](ResourceReference.md) | The effective outbound IP resources of the cluster load balancer. |  [optional] |
|**idleTimeoutInMinutes** | **Integer** | Desired outbound flow idle timeout in minutes. Allowed values must be in the range of 4 to 120 (inclusive). The default value is 30 minutes. |  [optional] |
|**managedOutboundIPs** | [**ManagedClusterLoadBalancerProfileManagedOutboundIPs**](ManagedClusterLoadBalancerProfileManagedOutboundIPs.md) |  |  [optional] |
|**outboundIPPrefixes** | [**ManagedClusterLoadBalancerProfileOutboundIPPrefixes**](ManagedClusterLoadBalancerProfileOutboundIPPrefixes.md) |  |  [optional] |
|**outboundIPs** | [**ManagedClusterLoadBalancerProfileOutboundIPs**](ManagedClusterLoadBalancerProfileOutboundIPs.md) |  |  [optional] |



