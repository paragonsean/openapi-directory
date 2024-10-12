

# AddRemoveReplicaScalingMechanism

Describes the horizontal auto scaling mechanism that adds or removes replicas (containers or container groups).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxCount** | **Integer** | Maximum number of containers (scale up won&#39;t be performed above this number). |  |
|**minCount** | **Integer** | Minimum number of containers (scale down won&#39;t be performed below this number). |  |
|**scaleIncrement** | **Integer** | Each time auto scaling is performed, this number of containers will be added or removed. |  |



