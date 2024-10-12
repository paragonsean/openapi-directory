# ContainerServiceClient.ManagedClusterLoadBalancerProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocatedOutboundPorts** | **Number** | Desired number of allocated SNAT ports per VM. Allowed values must be in the range of 0 to 64000 (inclusive). The default value is 0 which results in Azure dynamically allocating ports. | [optional] [default to 0]
**effectiveOutboundIPs** | [**[ResourceReference]**](ResourceReference.md) | The effective outbound IP resources of the cluster load balancer. | [optional] 
**idleTimeoutInMinutes** | **Number** | Desired outbound flow idle timeout in minutes. Allowed values must be in the range of 4 to 120 (inclusive). The default value is 30 minutes. | [optional] [default to 30]
**managedOutboundIPs** | [**ManagedClusterLoadBalancerProfileManagedOutboundIPs**](ManagedClusterLoadBalancerProfileManagedOutboundIPs.md) |  | [optional] 
**outboundIPPrefixes** | [**ManagedClusterLoadBalancerProfileOutboundIPPrefixes**](ManagedClusterLoadBalancerProfileOutboundIPPrefixes.md) |  | [optional] 
**outboundIPs** | [**ManagedClusterLoadBalancerProfileOutboundIPs**](ManagedClusterLoadBalancerProfileOutboundIPs.md) |  | [optional] 


