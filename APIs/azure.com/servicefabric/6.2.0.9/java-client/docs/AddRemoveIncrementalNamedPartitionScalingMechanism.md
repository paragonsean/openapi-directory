

# AddRemoveIncrementalNamedPartitionScalingMechanism

Represents a scaling mechanism for adding or removing named partitions of a stateless service. Partition names are in the format '0','1''N-1'

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxPartitionCount** | **Integer** | Maximum number of named partitions of the service. |  |
|**minPartitionCount** | **Integer** | Minimum number of named partitions of the service. |  |
|**scaleIncrement** | **Integer** | The number of instances to add or remove during a scaling operation. |  |



