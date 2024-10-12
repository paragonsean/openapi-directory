# VMwareEngineApi.PrivateConnection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Creation time of this resource. | [optional] [readonly] 
**description** | **String** | Optional. User-provided description for this private connection. | [optional] 
**name** | **String** | Output only. The resource name of the private connection. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1/privateConnections/my-connection&#x60; | [optional] [readonly] 
**peeringId** | **String** | Output only. VPC network peering id between given network VPC and VMwareEngineNetwork. | [optional] [readonly] 
**peeringState** | **String** | Output only. Peering state between service network and VMware Engine network. | [optional] [readonly] 
**routingMode** | **String** | Optional. Routing Mode. Default value is set to GLOBAL. For type &#x3D; PRIVATE_SERVICE_ACCESS, this field can be set to GLOBAL or REGIONAL, for other types only GLOBAL is supported. | [optional] 
**serviceNetwork** | **String** | Required. Service network to create private connection. Specify the name in the following form: &#x60;projects/{project}/global/networks/{network_id}&#x60; For type &#x3D; PRIVATE_SERVICE_ACCESS, this field represents servicenetworking VPC, e.g. projects/project-tp/global/networks/servicenetworking. For type &#x3D; NETAPP_CLOUD_VOLUME, this field represents NetApp service VPC, e.g. projects/project-tp/global/networks/netapp-tenant-vpc. For type &#x3D; DELL_POWERSCALE, this field represent Dell service VPC, e.g. projects/project-tp/global/networks/dell-tenant-vpc. For type&#x3D; THIRD_PARTY_SERVICE, this field could represent a consumer VPC or any other producer VPC to which the VMware Engine Network needs to be connected, e.g. projects/project/global/networks/vpc. | [optional] 
**state** | **String** | Output only. State of the private connection. | [optional] [readonly] 
**type** | **String** | Required. Private connection type. | [optional] 
**uid** | **String** | Output only. System-generated unique identifier for the resource. | [optional] [readonly] 
**updateTime** | **String** | Output only. Last update time of this resource. | [optional] [readonly] 
**vmwareEngineNetwork** | **String** | Required. The relative resource name of Legacy VMware Engine network. Specify the name in the following form: &#x60;projects/{project}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}&#x60; where &#x60;{project}&#x60;, &#x60;{location}&#x60; will be same as specified in private connection resource name and &#x60;{vmware_engine_network_id}&#x60; will be in the form of &#x60;{location}&#x60;-default e.g. projects/project/locations/us-central1/vmwareEngineNetworks/us-central1-default. | [optional] 
**vmwareEngineNetworkCanonical** | **String** | Output only. The canonical name of the VMware Engine network in the form: &#x60;projects/{project_number}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}&#x60; | [optional] [readonly] 



## Enum: PeeringStateEnum


* `STATE_UNSPECIFIED` (value: `"PEERING_STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"PEERING_ACTIVE"`)

* `INACTIVE` (value: `"PEERING_INACTIVE"`)





## Enum: RoutingModeEnum


* `ROUTING_MODE_UNSPECIFIED` (value: `"ROUTING_MODE_UNSPECIFIED"`)

* `GLOBAL` (value: `"GLOBAL"`)

* `REGIONAL` (value: `"REGIONAL"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `UPDATING` (value: `"UPDATING"`)

* `DELETING` (value: `"DELETING"`)

* `UNPROVISIONED` (value: `"UNPROVISIONED"`)

* `FAILED` (value: `"FAILED"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `PRIVATE_SERVICE_ACCESS` (value: `"PRIVATE_SERVICE_ACCESS"`)

* `NETAPP_CLOUD_VOLUMES` (value: `"NETAPP_CLOUD_VOLUMES"`)

* `DELL_POWERSCALE` (value: `"DELL_POWERSCALE"`)

* `THIRD_PARTY_SERVICE` (value: `"THIRD_PARTY_SERVICE"`)




