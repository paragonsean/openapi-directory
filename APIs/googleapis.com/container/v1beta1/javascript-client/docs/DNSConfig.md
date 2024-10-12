# KubernetesEngineApi.DNSConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusterDns** | **String** | cluster_dns indicates which in-cluster DNS provider should be used. | [optional] 
**clusterDnsDomain** | **String** | cluster_dns_domain is the suffix used for all cluster service records. | [optional] 
**clusterDnsScope** | **String** | cluster_dns_scope indicates the scope of access to cluster DNS records. | [optional] 



## Enum: ClusterDnsEnum


* `PROVIDER_UNSPECIFIED` (value: `"PROVIDER_UNSPECIFIED"`)

* `PLATFORM_DEFAULT` (value: `"PLATFORM_DEFAULT"`)

* `CLOUD_DNS` (value: `"CLOUD_DNS"`)

* `KUBE_DNS` (value: `"KUBE_DNS"`)





## Enum: ClusterDnsScopeEnum


* `DNS_SCOPE_UNSPECIFIED` (value: `"DNS_SCOPE_UNSPECIFIED"`)

* `CLUSTER_SCOPE` (value: `"CLUSTER_SCOPE"`)

* `VPC_SCOPE` (value: `"VPC_SCOPE"`)




