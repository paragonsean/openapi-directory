# NetworkManagementApi.Endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appEngineVersion** | [**AppEngineVersionEndpoint**](AppEngineVersionEndpoint.md) |  | [optional] 
**cloudFunction** | [**CloudFunctionEndpoint**](CloudFunctionEndpoint.md) |  | [optional] 
**cloudRunRevision** | [**CloudRunRevisionEndpoint**](CloudRunRevisionEndpoint.md) |  | [optional] 
**cloudSqlInstance** | **String** | A [Cloud SQL](https://cloud.google.com/sql) instance URI. | [optional] 
**forwardingRule** | **String** | A forwarding rule and its corresponding IP address represent the frontend configuration of a Google Cloud load balancer. Forwarding rules are also used for protocol forwarding, Private Service Connect and other network services to provide forwarding information in the control plane. Format: projects/{project}/global/forwardingRules/{id} or projects/{project}/regions/{region}/forwardingRules/{id} | [optional] 
**forwardingRuleTarget** | **String** | Output only. Specifies the type of the target of the forwarding rule. | [optional] [readonly] 
**gkeMasterCluster** | **String** | A cluster URI for [Google Kubernetes Engine master](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture). | [optional] 
**instance** | **String** | A Compute Engine instance URI. | [optional] 
**ipAddress** | **String** | The IP address of the endpoint, which can be an external or internal IP. | [optional] 
**loadBalancerId** | **String** | Output only. ID of the load balancer the forwarding rule points to. Empty for forwarding rules not related to load balancers. | [optional] [readonly] 
**loadBalancerType** | **String** | Output only. Type of the load balancer the forwarding rule points to. | [optional] [readonly] 
**network** | **String** | A Compute Engine network URI. | [optional] 
**networkType** | **String** | Type of the network where the endpoint is located. Applicable only to source endpoint, as destination network type can be inferred from the source. | [optional] 
**port** | **Number** | The IP protocol port of the endpoint. Only applicable when protocol is TCP or UDP. | [optional] 
**projectId** | **String** | Project ID where the endpoint is located. The Project ID can be derived from the URI if you provide a VM instance or network URI. The following are two cases where you must provide the project ID: 1. Only the IP address is specified, and the IP address is within a Google Cloud project. 2. When you are using Shared VPC and the IP address that you provide is from the service project. In this case, the network that the IP address resides in is defined in the host project. | [optional] 



## Enum: ForwardingRuleTargetEnum


* `FORWARDING_RULE_TARGET_UNSPECIFIED` (value: `"FORWARDING_RULE_TARGET_UNSPECIFIED"`)

* `INSTANCE` (value: `"INSTANCE"`)

* `LOAD_BALANCER` (value: `"LOAD_BALANCER"`)

* `VPN_GATEWAY` (value: `"VPN_GATEWAY"`)

* `PSC` (value: `"PSC"`)





## Enum: LoadBalancerTypeEnum


* `LOAD_BALANCER_TYPE_UNSPECIFIED` (value: `"LOAD_BALANCER_TYPE_UNSPECIFIED"`)

* `HTTPS_ADVANCED_LOAD_BALANCER` (value: `"HTTPS_ADVANCED_LOAD_BALANCER"`)

* `HTTPS_LOAD_BALANCER` (value: `"HTTPS_LOAD_BALANCER"`)

* `REGIONAL_HTTPS_LOAD_BALANCER` (value: `"REGIONAL_HTTPS_LOAD_BALANCER"`)

* `INTERNAL_HTTPS_LOAD_BALANCER` (value: `"INTERNAL_HTTPS_LOAD_BALANCER"`)

* `SSL_PROXY_LOAD_BALANCER` (value: `"SSL_PROXY_LOAD_BALANCER"`)

* `TCP_PROXY_LOAD_BALANCER` (value: `"TCP_PROXY_LOAD_BALANCER"`)

* `INTERNAL_TCP_PROXY_LOAD_BALANCER` (value: `"INTERNAL_TCP_PROXY_LOAD_BALANCER"`)

* `NETWORK_LOAD_BALANCER` (value: `"NETWORK_LOAD_BALANCER"`)

* `LEGACY_NETWORK_LOAD_BALANCER` (value: `"LEGACY_NETWORK_LOAD_BALANCER"`)

* `TCP_UDP_INTERNAL_LOAD_BALANCER` (value: `"TCP_UDP_INTERNAL_LOAD_BALANCER"`)





## Enum: NetworkTypeEnum


* `NETWORK_TYPE_UNSPECIFIED` (value: `"NETWORK_TYPE_UNSPECIFIED"`)

* `GCP_NETWORK` (value: `"GCP_NETWORK"`)

* `NON_GCP_NETWORK` (value: `"NON_GCP_NETWORK"`)




