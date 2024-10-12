

# StandardRolloutPolicy

Standard rollout policy is the default policy for blue-green.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**batchNodeCount** | **Integer** | Number of blue nodes to drain in a batch. |  [optional] |
|**batchPercentage** | **Float** | Percentage of the blue pool nodes to drain in a batch. The range of this field should be (0.0, 1.0]. |  [optional] |
|**batchSoakDuration** | **String** | Soak time after each batch gets drained. Default to zero. |  [optional] |



