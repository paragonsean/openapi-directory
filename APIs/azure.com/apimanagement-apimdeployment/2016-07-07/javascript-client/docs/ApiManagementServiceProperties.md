# ApiManagementClient.ApiManagementServiceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalLocations** | [**[AdditionalRegion]**](AdditionalRegion.md) | Additional datacenter locations of the API Management service. | [optional] 
**addresserEmail** | **String** | Addresser email. | [optional] 
**createdAtUtc** | **Date** | Creation UTC date of the API Management service.The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard. | [optional] [readonly] 
**customProperties** | **{String: String}** | Custom properties of the API Management service, like disabling TLS 1.0. | [optional] 
**hostnameConfigurations** | [**[HostnameConfiguration]**](HostnameConfiguration.md) | Custom hostname configuration of the API Management service. | [optional] 
**managementApiUrl** | **String** | Management API endpoint URL of the API Management service. | [optional] [readonly] 
**portalUrl** | **String** | Publisher portal endpoint Url of the API Management service. | [optional] [readonly] 
**provisioningState** | **String** | The current provisioning state of the API Management service which can be one of the following: Created/Activating/Succeeded/Updating/Failed/Stopped/Terminating/TerminationFailed/Deleted. | [optional] [readonly] 
**publisherEmail** | **String** | Publisher email. | 
**publisherName** | **String** | Publisher name. | 
**runtimeUrl** | **String** | Proxy endpoint URL of the API Management service. | [optional] [readonly] 
**scmUrl** | **String** | SCM endpoint URL of the API Management service. | [optional] [readonly] 
**staticIPs** | **[String]** | Static IP addresses of the API Management service virtual machines. Available only for Standard and Premium SKU. | [optional] [readonly] 
**targetProvisioningState** | **String** | The provisioning state of the API Management service, which is targeted by the long running operation started on the service. | [optional] [readonly] 
**vpnType** | **String** | The type of VPN in which API Management service needs to be configured in. None (Default Value) means the API Management service is not part of any Virtual Network, External means the API Management deployment is set up inside a Virtual Network having an Internet Facing Endpoint, and Internal means that API Management deployment is setup inside a Virtual Network having an Intranet Facing Endpoint only. | [optional] [default to &#39;None&#39;]
**vpnconfiguration** | [**VirtualNetworkConfiguration**](VirtualNetworkConfiguration.md) |  | [optional] 



## Enum: VpnTypeEnum


* `None` (value: `"None"`)

* `External` (value: `"External"`)

* `Internal` (value: `"Internal"`)




