# VMwareEngineApi.NetworkConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dnsServerIp** | **String** | Output only. DNS Server IP of the Private Cloud. All DNS queries can be forwarded to this address for name resolution of Private Cloud&#39;s management entities like vCenter, NSX-T Manager and ESXi hosts. | [optional] [readonly] 
**managementCidr** | **String** | Required. Management CIDR used by VMware management appliances. | [optional] 
**managementIpAddressLayoutVersion** | **Number** | Output only. The IP address layout version of the management IP address range. Possible versions include: * &#x60;managementIpAddressLayoutVersion&#x3D;1&#x60;: Indicates the legacy IP address layout used by some existing private clouds. This is no longer supported for new private clouds as it does not support all features. * &#x60;managementIpAddressLayoutVersion&#x3D;2&#x60;: Indicates the latest IP address layout used by all newly created private clouds. This version supports all current features. | [optional] [readonly] 
**vmwareEngineNetwork** | **String** | Optional. The relative resource name of the VMware Engine network attached to the private cloud. Specify the name in the following form: &#x60;projects/{project}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}&#x60; where &#x60;{project}&#x60; can either be a project number or a project ID. | [optional] 
**vmwareEngineNetworkCanonical** | **String** | Output only. The canonical name of the VMware Engine network in the form: &#x60;projects/{project_number}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}&#x60; | [optional] [readonly] 


