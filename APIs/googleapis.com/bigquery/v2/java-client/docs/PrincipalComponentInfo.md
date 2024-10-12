

# PrincipalComponentInfo

Principal component infos, used only for eigen decomposition based models, e.g., PCA. Ordered by explained_variance in the descending order.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cumulativeExplainedVarianceRatio** | **Double** | The explained_variance is pre-ordered in the descending order to compute the cumulative explained variance ratio. |  [optional] |
|**explainedVariance** | **Double** | Explained variance by this principal component, which is simply the eigenvalue. |  [optional] |
|**explainedVarianceRatio** | **Double** | Explained_variance over the total explained variance. |  [optional] |
|**principalComponentId** | **String** | Id of the principal component. |  [optional] |



