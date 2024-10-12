# NetworkManagementApi.NatInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**natGatewayName** | **String** | The name of Cloud NAT Gateway. Only valid when type is CLOUD_NAT. | [optional] 
**networkUri** | **String** | URI of the network where NAT translation takes place. | [optional] 
**newDestinationIp** | **String** | Destination IP address after NAT translation. | [optional] 
**newDestinationPort** | **Number** | Destination port after NAT translation. Only valid when protocol is TCP or UDP. | [optional] 
**newSourceIp** | **String** | Source IP address after NAT translation. | [optional] 
**newSourcePort** | **Number** | Source port after NAT translation. Only valid when protocol is TCP or UDP. | [optional] 
**oldDestinationIp** | **String** | Destination IP address before NAT translation. | [optional] 
**oldDestinationPort** | **Number** | Destination port before NAT translation. Only valid when protocol is TCP or UDP. | [optional] 
**oldSourceIp** | **String** | Source IP address before NAT translation. | [optional] 
**oldSourcePort** | **Number** | Source port before NAT translation. Only valid when protocol is TCP or UDP. | [optional] 
**protocol** | **String** | IP protocol in string format, for example: \&quot;TCP\&quot;, \&quot;UDP\&quot;, \&quot;ICMP\&quot;. | [optional] 
**routerUri** | **String** | Uri of the Cloud Router. Only valid when type is CLOUD_NAT. | [optional] 
**type** | **String** | Type of NAT. | [optional] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `INTERNAL_TO_EXTERNAL` (value: `"INTERNAL_TO_EXTERNAL"`)

* `EXTERNAL_TO_INTERNAL` (value: `"EXTERNAL_TO_INTERNAL"`)

* `CLOUD_NAT` (value: `"CLOUD_NAT"`)

* `PRIVATE_SERVICE_CONNECT` (value: `"PRIVATE_SERVICE_CONNECT"`)




