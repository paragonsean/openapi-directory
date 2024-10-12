

# Subnet

Subnet in a private cloud. Either `management` subnets (such as vMotion) that are read-only, or `userDefined`, which can also be updated.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gatewayIp** | **String** | The IP address of the gateway of this subnet. Must fall within the IP prefix defined above. |  [optional] |
|**ipCidrRange** | **String** | The IP address range of the subnet in CIDR format &#39;10.0.0.0/24&#39;. |  [optional] |
|**name** | **String** | Output only. The resource name of this subnet. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud/subnets/my-subnet&#x60; |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the resource. |  [optional] [readonly] |
|**type** | **String** | Output only. The type of the subnet. For example \&quot;management\&quot; or \&quot;userDefined\&quot;. |  [optional] [readonly] |
|**vlanId** | **Integer** | Output only. VLAN ID of the VLAN on which the subnet is configured |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| CREATING | &quot;CREATING&quot; |
| UPDATING | &quot;UPDATING&quot; |
| DELETING | &quot;DELETING&quot; |
| RECONCILING | &quot;RECONCILING&quot; |
| FAILED | &quot;FAILED&quot; |



