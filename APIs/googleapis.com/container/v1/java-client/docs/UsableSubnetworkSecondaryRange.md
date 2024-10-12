

# UsableSubnetworkSecondaryRange

Secondary IP range of a usable subnetwork.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ipCidrRange** | **String** | The range of IP addresses belonging to this subnetwork secondary range. |  [optional] |
|**rangeName** | **String** | The name associated with this subnetwork secondary range, used when adding an alias IP range to a VM instance. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | This field is to determine the status of the secondary range programmably. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| UNUSED | &quot;UNUSED&quot; |
| IN_USE_SERVICE | &quot;IN_USE_SERVICE&quot; |
| IN_USE_SHAREABLE_POD | &quot;IN_USE_SHAREABLE_POD&quot; |
| IN_USE_MANAGED_POD | &quot;IN_USE_MANAGED_POD&quot; |



