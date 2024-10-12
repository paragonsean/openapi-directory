

# NetworkAddress

Details of network address.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assignment** | [**AssignmentEnum**](#AssignmentEnum) | Whether DHCP is used to assign addresses. |  [optional] |
|**bcast** | **String** | Broadcast address. |  [optional] |
|**fqdn** | **String** | Fully qualified domain name. |  [optional] |
|**ipAddress** | **String** | Assigned or configured IP Address. |  [optional] |
|**subnetMask** | **String** | Subnet mask. |  [optional] |



## Enum: AssignmentEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ADDRESS_ASSIGNMENT_UNSPECIFIED&quot; |
| STATIC | &quot;ADDRESS_ASSIGNMENT_STATIC&quot; |
| DHCP | &quot;ADDRESS_ASSIGNMENT_DHCP&quot; |



