

# Endpoint

Source or destination of the Connectivity Test.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appEngineVersion** | [**AppEngineVersionEndpoint**](AppEngineVersionEndpoint.md) |  |  [optional] |
|**cloudFunction** | [**CloudFunctionEndpoint**](CloudFunctionEndpoint.md) |  |  [optional] |
|**cloudRunRevision** | [**CloudRunRevisionEndpoint**](CloudRunRevisionEndpoint.md) |  |  [optional] |
|**cloudSqlInstance** | **String** | A [Cloud SQL](https://cloud.google.com/sql) instance URI. |  [optional] |
|**forwardingRule** | **String** | A forwarding rule and its corresponding IP address represent the frontend configuration of a Google Cloud load balancer. Forwarding rules are also used for protocol forwarding, Private Service Connect and other network services to provide forwarding information in the control plane. Format: projects/{project}/global/forwardingRules/{id} or projects/{project}/regions/{region}/forwardingRules/{id} |  [optional] |
|**forwardingRuleTarget** | [**ForwardingRuleTargetEnum**](#ForwardingRuleTargetEnum) | Output only. Specifies the type of the target of the forwarding rule. |  [optional] [readonly] |
|**gkeMasterCluster** | **String** | A cluster URI for [Google Kubernetes Engine master](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture). |  [optional] |
|**instance** | **String** | A Compute Engine instance URI. |  [optional] |
|**ipAddress** | **String** | The IP address of the endpoint, which can be an external or internal IP. |  [optional] |
|**loadBalancerId** | **String** | Output only. ID of the load balancer the forwarding rule points to. Empty for forwarding rules not related to load balancers. |  [optional] [readonly] |
|**loadBalancerType** | [**LoadBalancerTypeEnum**](#LoadBalancerTypeEnum) | Output only. Type of the load balancer the forwarding rule points to. |  [optional] [readonly] |
|**network** | **String** | A Compute Engine network URI. |  [optional] |
|**networkType** | [**NetworkTypeEnum**](#NetworkTypeEnum) | Type of the network where the endpoint is located. Applicable only to source endpoint, as destination network type can be inferred from the source. |  [optional] |
|**port** | **Integer** | The IP protocol port of the endpoint. Only applicable when protocol is TCP or UDP. |  [optional] |
|**projectId** | **String** | Project ID where the endpoint is located. The Project ID can be derived from the URI if you provide a VM instance or network URI. The following are two cases where you must provide the project ID: 1. Only the IP address is specified, and the IP address is within a Google Cloud project. 2. When you are using Shared VPC and the IP address that you provide is from the service project. In this case, the network that the IP address resides in is defined in the host project. |  [optional] |



## Enum: ForwardingRuleTargetEnum

| Name | Value |
|---- | -----|
| FORWARDING_RULE_TARGET_UNSPECIFIED | &quot;FORWARDING_RULE_TARGET_UNSPECIFIED&quot; |
| INSTANCE | &quot;INSTANCE&quot; |
| LOAD_BALANCER | &quot;LOAD_BALANCER&quot; |
| VPN_GATEWAY | &quot;VPN_GATEWAY&quot; |
| PSC | &quot;PSC&quot; |



## Enum: LoadBalancerTypeEnum

| Name | Value |
|---- | -----|
| LOAD_BALANCER_TYPE_UNSPECIFIED | &quot;LOAD_BALANCER_TYPE_UNSPECIFIED&quot; |
| HTTPS_ADVANCED_LOAD_BALANCER | &quot;HTTPS_ADVANCED_LOAD_BALANCER&quot; |
| HTTPS_LOAD_BALANCER | &quot;HTTPS_LOAD_BALANCER&quot; |
| REGIONAL_HTTPS_LOAD_BALANCER | &quot;REGIONAL_HTTPS_LOAD_BALANCER&quot; |
| INTERNAL_HTTPS_LOAD_BALANCER | &quot;INTERNAL_HTTPS_LOAD_BALANCER&quot; |
| SSL_PROXY_LOAD_BALANCER | &quot;SSL_PROXY_LOAD_BALANCER&quot; |
| TCP_PROXY_LOAD_BALANCER | &quot;TCP_PROXY_LOAD_BALANCER&quot; |
| INTERNAL_TCP_PROXY_LOAD_BALANCER | &quot;INTERNAL_TCP_PROXY_LOAD_BALANCER&quot; |
| NETWORK_LOAD_BALANCER | &quot;NETWORK_LOAD_BALANCER&quot; |
| LEGACY_NETWORK_LOAD_BALANCER | &quot;LEGACY_NETWORK_LOAD_BALANCER&quot; |
| TCP_UDP_INTERNAL_LOAD_BALANCER | &quot;TCP_UDP_INTERNAL_LOAD_BALANCER&quot; |



## Enum: NetworkTypeEnum

| Name | Value |
|---- | -----|
| NETWORK_TYPE_UNSPECIFIED | &quot;NETWORK_TYPE_UNSPECIFIED&quot; |
| GCP_NETWORK | &quot;GCP_NETWORK&quot; |
| NON_GCP_NETWORK | &quot;NON_GCP_NETWORK&quot; |



