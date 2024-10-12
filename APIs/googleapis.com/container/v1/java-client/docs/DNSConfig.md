

# DNSConfig

DNSConfig contains the desired set of options for configuring clusterDNS.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusterDns** | [**ClusterDnsEnum**](#ClusterDnsEnum) | cluster_dns indicates which in-cluster DNS provider should be used. |  [optional] |
|**clusterDnsDomain** | **String** | cluster_dns_domain is the suffix used for all cluster service records. |  [optional] |
|**clusterDnsScope** | [**ClusterDnsScopeEnum**](#ClusterDnsScopeEnum) | cluster_dns_scope indicates the scope of access to cluster DNS records. |  [optional] |



## Enum: ClusterDnsEnum

| Name | Value |
|---- | -----|
| PROVIDER_UNSPECIFIED | &quot;PROVIDER_UNSPECIFIED&quot; |
| PLATFORM_DEFAULT | &quot;PLATFORM_DEFAULT&quot; |
| CLOUD_DNS | &quot;CLOUD_DNS&quot; |
| KUBE_DNS | &quot;KUBE_DNS&quot; |



## Enum: ClusterDnsScopeEnum

| Name | Value |
|---- | -----|
| DNS_SCOPE_UNSPECIFIED | &quot;DNS_SCOPE_UNSPECIFIED&quot; |
| CLUSTER_SCOPE | &quot;CLUSTER_SCOPE&quot; |
| VPC_SCOPE | &quot;VPC_SCOPE&quot; |



