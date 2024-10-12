# VMwareEngineApi.NetworkPeering

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Creation time of this resource. | [optional] [readonly] 
**description** | **String** | Optional. User-provided description for this network peering. | [optional] 
**exchangeSubnetRoutes** | **Boolean** | Optional. True if full mesh connectivity is created and managed automatically between peered networks; false otherwise. Currently this field is always true because Google Compute Engine automatically creates and manages subnetwork routes between two VPC networks when peering state is &#39;ACTIVE&#39;. | [optional] 
**exportCustomRoutes** | **Boolean** | Optional. True if custom routes are exported to the peered network; false otherwise. The default value is true. | [optional] 
**exportCustomRoutesWithPublicIp** | **Boolean** | Optional. True if all subnet routes with a public IP address range are exported; false otherwise. The default value is true. IPv4 special-use ranges (https://en.wikipedia.org/wiki/IPv4#Special_addresses) are always exported to peers and are not controlled by this field. | [optional] 
**importCustomRoutes** | **Boolean** | Optional. True if custom routes are imported from the peered network; false otherwise. The default value is true. | [optional] 
**importCustomRoutesWithPublicIp** | **Boolean** | Optional. True if all subnet routes with public IP address range are imported; false otherwise. The default value is true. IPv4 special-use ranges (https://en.wikipedia.org/wiki/IPv4#Special_addresses) are always imported to peers and are not controlled by this field. | [optional] 
**name** | **String** | Output only. The resource name of the network peering. NetworkPeering is a global resource and location can only be global. Resource names are scheme-less URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/global/networkPeerings/my-peering&#x60; | [optional] [readonly] 
**peerMtu** | **Number** | Optional. Maximum transmission unit (MTU) in bytes. The default value is &#x60;1500&#x60;. If a value of &#x60;0&#x60; is provided for this field, VMware Engine uses the default value instead. | [optional] 
**peerNetwork** | **String** | Required. The relative resource name of the network to peer with a standard VMware Engine network. The provided network can be a consumer VPC network or another standard VMware Engine network. If the &#x60;peer_network_type&#x60; is VMWARE_ENGINE_NETWORK, specify the name in the form: &#x60;projects/{project}/locations/global/vmwareEngineNetworks/{vmware_engine_network_id}&#x60;. Otherwise specify the name in the form: &#x60;projects/{project}/global/networks/{network_id}&#x60;, where &#x60;{project}&#x60; can either be a project number or a project ID. | [optional] 
**peerNetworkType** | **String** | Required. The type of the network to peer with the VMware Engine network. | [optional] 
**state** | **String** | Output only. State of the network peering. This field has a value of &#39;ACTIVE&#39; when there&#39;s a matching configuration in the peer network. New values may be added to this enum when appropriate. | [optional] [readonly] 
**stateDetails** | **String** | Output only. Output Only. Details about the current state of the network peering. | [optional] [readonly] 
**uid** | **String** | Output only. System-generated unique identifier for the resource. | [optional] [readonly] 
**updateTime** | **String** | Output only. Last update time of this resource. | [optional] [readonly] 
**vmwareEngineNetwork** | **String** | Required. The relative resource name of the VMware Engine network. Specify the name in the following form: &#x60;projects/{project}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}&#x60; where &#x60;{project}&#x60; can either be a project number or a project ID. | [optional] 



## Enum: PeerNetworkTypeEnum


* `PEER_NETWORK_TYPE_UNSPECIFIED` (value: `"PEER_NETWORK_TYPE_UNSPECIFIED"`)

* `STANDARD` (value: `"STANDARD"`)

* `VMWARE_ENGINE_NETWORK` (value: `"VMWARE_ENGINE_NETWORK"`)

* `PRIVATE_SERVICES_ACCESS` (value: `"PRIVATE_SERVICES_ACCESS"`)

* `NETAPP_CLOUD_VOLUMES` (value: `"NETAPP_CLOUD_VOLUMES"`)

* `THIRD_PARTY_SERVICE` (value: `"THIRD_PARTY_SERVICE"`)

* `DELL_POWERSCALE` (value: `"DELL_POWERSCALE"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `INACTIVE` (value: `"INACTIVE"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `CREATING` (value: `"CREATING"`)

* `DELETING` (value: `"DELETING"`)




