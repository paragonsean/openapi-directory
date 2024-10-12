

# IterationResult

Information about a single iteration of the training run.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arimaResult** | [**ArimaResult**](ArimaResult.md) |  |  [optional] |
|**clusterInfos** | [**List&lt;ClusterInfo&gt;**](ClusterInfo.md) | Information about top clusters for clustering models. |  [optional] |
|**durationMs** | **String** | Time taken to run the iteration in milliseconds. |  [optional] |
|**evalLoss** | **Double** | Loss computed on the eval data at the end of iteration. |  [optional] |
|**index** | **Integer** | Index of the iteration, 0 based. |  [optional] |
|**learnRate** | **Double** | Learn rate used for this iteration. |  [optional] |
|**principalComponentInfos** | [**List&lt;PrincipalComponentInfo&gt;**](PrincipalComponentInfo.md) | The information of the principal components. |  [optional] |
|**trainingLoss** | **Double** | Loss computed on the training data at the end of iteration. |  [optional] |



