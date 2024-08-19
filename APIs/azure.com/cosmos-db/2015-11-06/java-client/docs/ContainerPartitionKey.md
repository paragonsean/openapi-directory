

# ContainerPartitionKey

The configuration of the partition key to be used for partitioning data into multiple partitions

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | [**KindEnum**](#KindEnum) | Indicates the kind of algorithm used for partitioning |  [optional] |
|**paths** | **List&lt;String&gt;** | List of paths using which data within the container can be partitioned |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| HASH | &quot;Hash&quot; |
| RANGE | &quot;Range&quot; |



