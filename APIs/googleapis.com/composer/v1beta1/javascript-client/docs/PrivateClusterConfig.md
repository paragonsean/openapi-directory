# CloudComposerApi.PrivateClusterConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enablePrivateEndpoint** | **Boolean** | Optional. If &#x60;true&#x60;, access to the public endpoint of the GKE cluster is denied. | [optional] 
**masterIpv4CidrBlock** | **String** | Optional. The CIDR block from which IPv4 range for GKE master will be reserved. If left blank, the default value of &#39;172.16.0.0/23&#39; is used. | [optional] 
**masterIpv4ReservedRange** | **String** | Output only. The IP range in CIDR notation to use for the hosted master network. This range is used for assigning internal IP addresses to the cluster master or set of masters and to the internal load balancer virtual IP. This range must not overlap with any other ranges in use within the cluster&#39;s network. | [optional] [readonly] 


