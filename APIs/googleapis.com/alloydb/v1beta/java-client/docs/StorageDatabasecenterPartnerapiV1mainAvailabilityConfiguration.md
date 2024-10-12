

# StorageDatabasecenterPartnerapiV1mainAvailabilityConfiguration

Configuration for availability of database instance

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availabilityType** | [**AvailabilityTypeEnum**](#AvailabilityTypeEnum) | Availability type. Potential values: * &#x60;ZONAL&#x60;: The instance serves data from only one zone. Outages in that zone affect data accessibility. * &#x60;REGIONAL&#x60;: The instance can serve data from more than one zone in a region (it is highly available). |  [optional] |
|**externalReplicaConfigured** | **Boolean** |  |  [optional] |
|**promotableReplicaConfigured** | **Boolean** |  |  [optional] |



## Enum: AvailabilityTypeEnum

| Name | Value |
|---- | -----|
| AVAILABILITY_TYPE_UNSPECIFIED | &quot;AVAILABILITY_TYPE_UNSPECIFIED&quot; |
| ZONAL | &quot;ZONAL&quot; |
| REGIONAL | &quot;REGIONAL&quot; |
| MULTI_REGIONAL | &quot;MULTI_REGIONAL&quot; |
| AVAILABILITY_TYPE_OTHER | &quot;AVAILABILITY_TYPE_OTHER&quot; |



