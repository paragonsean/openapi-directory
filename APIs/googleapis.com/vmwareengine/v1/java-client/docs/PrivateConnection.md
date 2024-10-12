

# PrivateConnection

Private connection resource that provides connectivity for VMware Engine private clouds.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Creation time of this resource. |  [optional] [readonly] |
|**description** | **String** | Optional. User-provided description for this private connection. |  [optional] |
|**name** | **String** | Output only. The resource name of the private connection. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1/privateConnections/my-connection&#x60; |  [optional] [readonly] |
|**peeringId** | **String** | Output only. VPC network peering id between given network VPC and VMwareEngineNetwork. |  [optional] [readonly] |
|**peeringState** | [**PeeringStateEnum**](#PeeringStateEnum) | Output only. Peering state between service network and VMware Engine network. |  [optional] [readonly] |
|**routingMode** | [**RoutingModeEnum**](#RoutingModeEnum) | Optional. Routing Mode. Default value is set to GLOBAL. For type &#x3D; PRIVATE_SERVICE_ACCESS, this field can be set to GLOBAL or REGIONAL, for other types only GLOBAL is supported. |  [optional] |
|**serviceNetwork** | **String** | Required. Service network to create private connection. Specify the name in the following form: &#x60;projects/{project}/global/networks/{network_id}&#x60; For type &#x3D; PRIVATE_SERVICE_ACCESS, this field represents servicenetworking VPC, e.g. projects/project-tp/global/networks/servicenetworking. For type &#x3D; NETAPP_CLOUD_VOLUME, this field represents NetApp service VPC, e.g. projects/project-tp/global/networks/netapp-tenant-vpc. For type &#x3D; DELL_POWERSCALE, this field represent Dell service VPC, e.g. projects/project-tp/global/networks/dell-tenant-vpc. For type&#x3D; THIRD_PARTY_SERVICE, this field could represent a consumer VPC or any other producer VPC to which the VMware Engine Network needs to be connected, e.g. projects/project/global/networks/vpc. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the private connection. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. Private connection type. |  [optional] |
|**uid** | **String** | Output only. System-generated unique identifier for the resource. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Last update time of this resource. |  [optional] [readonly] |
|**vmwareEngineNetwork** | **String** | Required. The relative resource name of Legacy VMware Engine network. Specify the name in the following form: &#x60;projects/{project}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}&#x60; where &#x60;{project}&#x60;, &#x60;{location}&#x60; will be same as specified in private connection resource name and &#x60;{vmware_engine_network_id}&#x60; will be in the form of &#x60;{location}&#x60;-default e.g. projects/project/locations/us-central1/vmwareEngineNetworks/us-central1-default. |  [optional] |
|**vmwareEngineNetworkCanonical** | **String** | Output only. The canonical name of the VMware Engine network in the form: &#x60;projects/{project_number}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}&#x60; |  [optional] [readonly] |



## Enum: PeeringStateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;PEERING_STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;PEERING_ACTIVE&quot; |
| INACTIVE | &quot;PEERING_INACTIVE&quot; |



## Enum: RoutingModeEnum

| Name | Value |
|---- | -----|
| ROUTING_MODE_UNSPECIFIED | &quot;ROUTING_MODE_UNSPECIFIED&quot; |
| GLOBAL | &quot;GLOBAL&quot; |
| REGIONAL | &quot;REGIONAL&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| UPDATING | &quot;UPDATING&quot; |
| DELETING | &quot;DELETING&quot; |
| UNPROVISIONED | &quot;UNPROVISIONED&quot; |
| FAILED | &quot;FAILED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| PRIVATE_SERVICE_ACCESS | &quot;PRIVATE_SERVICE_ACCESS&quot; |
| NETAPP_CLOUD_VOLUMES | &quot;NETAPP_CLOUD_VOLUMES&quot; |
| DELL_POWERSCALE | &quot;DELL_POWERSCALE&quot; |
| THIRD_PARTY_SERVICE | &quot;THIRD_PARTY_SERVICE&quot; |



