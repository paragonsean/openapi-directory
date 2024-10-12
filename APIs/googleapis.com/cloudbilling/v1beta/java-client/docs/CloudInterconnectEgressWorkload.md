

# CloudInterconnectEgressWorkload

Includes the estimate for Interconnect Data Transfer only. To specify usage for data transfer between VMs and internet end-points, use the Standard Tier Internet Data Transfer interface.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**egressRate** | [**Usage**](Usage.md) |  |  [optional] |
|**interconnectConnectionLocation** | [**InterconnectConnectionLocationEnum**](#InterconnectConnectionLocationEnum) | Locations in the [Interconnect connection location table](https://cloud.google.com/vpc/network-pricing#interconnect-pricing). These are the Interconnect Data Transfer charges. |  [optional] |



## Enum: InterconnectConnectionLocationEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;INTERCONNECT_CONNECTION_LOCATION_UNSPECIFIED&quot; |
| ASIA | &quot;INTERCONNECT_CONNECTION_LOCATION_ASIA&quot; |
| EUROPE | &quot;INTERCONNECT_CONNECTION_LOCATION_EUROPE&quot; |
| NORTH_AMERICA | &quot;INTERCONNECT_CONNECTION_LOCATION_NORTH_AMERICA&quot; |
| SOUTH_AMERICA | &quot;INTERCONNECT_CONNECTION_LOCATION_SOUTH_AMERICA&quot; |
| AUSTRALIA | &quot;INTERCONNECT_CONNECTION_LOCATION_AUSTRALIA&quot; |



