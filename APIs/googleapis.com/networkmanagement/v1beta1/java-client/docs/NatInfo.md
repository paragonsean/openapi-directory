

# NatInfo

For display only. Metadata associated with NAT.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**natGatewayName** | **String** | The name of Cloud NAT Gateway. Only valid when type is CLOUD_NAT. |  [optional] |
|**networkUri** | **String** | URI of the network where NAT translation takes place. |  [optional] |
|**newDestinationIp** | **String** | Destination IP address after NAT translation. |  [optional] |
|**newDestinationPort** | **Integer** | Destination port after NAT translation. Only valid when protocol is TCP or UDP. |  [optional] |
|**newSourceIp** | **String** | Source IP address after NAT translation. |  [optional] |
|**newSourcePort** | **Integer** | Source port after NAT translation. Only valid when protocol is TCP or UDP. |  [optional] |
|**oldDestinationIp** | **String** | Destination IP address before NAT translation. |  [optional] |
|**oldDestinationPort** | **Integer** | Destination port before NAT translation. Only valid when protocol is TCP or UDP. |  [optional] |
|**oldSourceIp** | **String** | Source IP address before NAT translation. |  [optional] |
|**oldSourcePort** | **Integer** | Source port before NAT translation. Only valid when protocol is TCP or UDP. |  [optional] |
|**protocol** | **String** | IP protocol in string format, for example: \&quot;TCP\&quot;, \&quot;UDP\&quot;, \&quot;ICMP\&quot;. |  [optional] |
|**routerUri** | **String** | Uri of the Cloud Router. Only valid when type is CLOUD_NAT. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of NAT. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| INTERNAL_TO_EXTERNAL | &quot;INTERNAL_TO_EXTERNAL&quot; |
| EXTERNAL_TO_INTERNAL | &quot;EXTERNAL_TO_INTERNAL&quot; |
| CLOUD_NAT | &quot;CLOUD_NAT&quot; |
| PRIVATE_SERVICE_CONNECT | &quot;PRIVATE_SERVICE_CONNECT&quot; |



