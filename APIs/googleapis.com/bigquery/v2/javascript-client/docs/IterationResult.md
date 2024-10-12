# BigQueryApi.IterationResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arimaResult** | [**ArimaResult**](ArimaResult.md) |  | [optional] 
**clusterInfos** | [**[ClusterInfo]**](ClusterInfo.md) | Information about top clusters for clustering models. | [optional] 
**durationMs** | **String** | Time taken to run the iteration in milliseconds. | [optional] 
**evalLoss** | **Number** | Loss computed on the eval data at the end of iteration. | [optional] 
**index** | **Number** | Index of the iteration, 0 based. | [optional] 
**learnRate** | **Number** | Learn rate used for this iteration. | [optional] 
**principalComponentInfos** | [**[PrincipalComponentInfo]**](PrincipalComponentInfo.md) | The information of the principal components. | [optional] 
**trainingLoss** | **Number** | Loss computed on the training data at the end of iteration. | [optional] 


