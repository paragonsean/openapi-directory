

# NetworkConfig

Network configuration for the instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectMode** | [**ConnectModeEnum**](#ConnectModeEnum) | The network connect mode of the Filestore instance. If not provided, the connect mode defaults to DIRECT_PEERING. |  [optional] |
|**ipAddresses** | **List&lt;String&gt;** | Output only. IPv4 addresses in the format &#x60;{octet1}.{octet2}.{octet3}.{octet4}&#x60; or IPv6 addresses in the format &#x60;{block1}:{block2}:{block3}:{block4}:{block5}:{block6}:{block7}:{block8}&#x60;. |  [optional] [readonly] |
|**modes** | [**List&lt;ModesEnum&gt;**](#List&lt;ModesEnum&gt;) | Internet protocol versions for which the instance has IP addresses assigned. For this version, only MODE_IPV4 is supported. |  [optional] |
|**network** | **String** | The name of the Google Compute Engine [VPC network](https://cloud.google.com/vpc/docs/vpc) to which the instance is connected. |  [optional] |
|**reservedIpRange** | **String** | Optional, reserved_ip_range can have one of the following two types of values. * CIDR range value when using DIRECT_PEERING connect mode. * [Allocated IP address range](https://cloud.google.com/compute/docs/ip-addresses/reserve-static-internal-ip-address) when using PRIVATE_SERVICE_ACCESS connect mode. When the name of an allocated IP address range is specified, it must be one of the ranges associated with the private service access connection. When specified as a direct CIDR value, it must be a /29 CIDR block for Basic tier, a /24 CIDR block for High Scale tier, or a /26 CIDR block for Enterprise tier in one of the [internal IP address ranges](https://www.arin.net/reference/research/statistics/address_filters/) that identifies the range of IP addresses reserved for this instance. For example, 10.0.0.0/29, 192.168.0.0/24 or 192.168.0.0/26, respectively. The range you specify can&#39;t overlap with either existing subnets or assigned IP address ranges for other Filestore instances in the selected VPC network. |  [optional] |



## Enum: ConnectModeEnum

| Name | Value |
|---- | -----|
| CONNECT_MODE_UNSPECIFIED | &quot;CONNECT_MODE_UNSPECIFIED&quot; |
| DIRECT_PEERING | &quot;DIRECT_PEERING&quot; |
| PRIVATE_SERVICE_ACCESS | &quot;PRIVATE_SERVICE_ACCESS&quot; |



## Enum: List&lt;ModesEnum&gt;

| Name | Value |
|---- | -----|
| ADDRESS_MODE_UNSPECIFIED | &quot;ADDRESS_MODE_UNSPECIFIED&quot; |
| MODE_IPV4 | &quot;MODE_IPV4&quot; |



