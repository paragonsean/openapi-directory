# AlloyDbApi.StorageDatabasecenterPartnerapiV1mainAvailabilityConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availabilityType** | **String** | Availability type. Potential values: * &#x60;ZONAL&#x60;: The instance serves data from only one zone. Outages in that zone affect data accessibility. * &#x60;REGIONAL&#x60;: The instance can serve data from more than one zone in a region (it is highly available). | [optional] 
**externalReplicaConfigured** | **Boolean** |  | [optional] 
**promotableReplicaConfigured** | **Boolean** |  | [optional] 



## Enum: AvailabilityTypeEnum


* `AVAILABILITY_TYPE_UNSPECIFIED` (value: `"AVAILABILITY_TYPE_UNSPECIFIED"`)

* `ZONAL` (value: `"ZONAL"`)

* `REGIONAL` (value: `"REGIONAL"`)

* `MULTI_REGIONAL` (value: `"MULTI_REGIONAL"`)

* `AVAILABILITY_TYPE_OTHER` (value: `"AVAILABILITY_TYPE_OTHER"`)




