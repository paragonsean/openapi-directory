

# UniformInt64RangePartitionSchemeDescription

Describes a partitioning scheme where an integer range is allocated evenly across a number of partitions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **Integer** | The number of partitions. |  |
|**highKey** | **String** | String indicating the upper bound of the partition key range that should be split between the partition ‘Count’  |  |
|**lowKey** | **String** | String indicating the lower bound of the partition key range that should be split between the partition ‘Count’  |  |



