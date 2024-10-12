

# NetworkPolicy

Represents a network policy resource. Network policies are regional resources. You can use a network policy to enable or disable internet access and external IP access. Network policies are associated with a VMware Engine network, which might span across regions. For a given region, a network policy applies to all private clouds in the VMware Engine network associated with the policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Creation time of this resource. |  [optional] [readonly] |
|**description** | **String** | Optional. User-provided description for this network policy. |  [optional] |
|**edgeServicesCidr** | **String** | Required. IP address range in CIDR notation used to create internet access and external IP access. An RFC 1918 CIDR block, with a \&quot;/26\&quot; prefix, is required. The range cannot overlap with any prefixes either in the consumer VPC network or in use by the private clouds attached to that VPC network. |  [optional] |
|**externalIp** | [**NetworkService**](NetworkService.md) |  |  [optional] |
|**internetAccess** | [**NetworkService**](NetworkService.md) |  |  [optional] |
|**name** | **String** | Output only. The resource name of this network policy. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1/networkPolicies/my-network-policy&#x60; |  [optional] [readonly] |
|**uid** | **String** | Output only. System-generated unique identifier for the resource. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Last update time of this resource. |  [optional] [readonly] |
|**vmwareEngineNetwork** | **String** | Optional. The relative resource name of the VMware Engine network. Specify the name in the following form: &#x60;projects/{project}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}&#x60; where &#x60;{project}&#x60; can either be a project number or a project ID. |  [optional] |
|**vmwareEngineNetworkCanonical** | **String** | Output only. The canonical name of the VMware Engine network in the form: &#x60;projects/{project_number}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}&#x60; |  [optional] [readonly] |



