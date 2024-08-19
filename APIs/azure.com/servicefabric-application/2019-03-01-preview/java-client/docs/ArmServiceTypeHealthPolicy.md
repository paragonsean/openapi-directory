

# ArmServiceTypeHealthPolicy

Represents the health policy used to evaluate the health of services belonging to a service type. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxPercentUnhealthyPartitionsPerService** | **Integer** | The maximum percentage of partitions per service allowed to be unhealthy before your application is considered in error.  |  [optional] |
|**maxPercentUnhealthyReplicasPerPartition** | **Integer** | The maximum percentage of replicas per partition allowed to be unhealthy before your application is considered in error.  |  [optional] |
|**maxPercentUnhealthyServices** | **Integer** | The maximum percentage of services allowed to be unhealthy before your application is considered in error.  |  [optional] |



