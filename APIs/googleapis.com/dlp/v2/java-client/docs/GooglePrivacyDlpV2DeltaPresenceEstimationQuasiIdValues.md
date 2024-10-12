

# GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValues

A tuple of values for the quasi-identifier columns.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**estimatedProbability** | **Double** | The estimated probability that a given individual sharing these quasi-identifier values is in the dataset. This value, typically called δ, is the ratio between the number of records in the dataset with these quasi-identifier values, and the total number of individuals (inside *and* outside the dataset) with these quasi-identifier values. For example, if there are 15 individuals in the dataset who share the same quasi-identifier values, and an estimated 100 people in the entire population with these values, then δ is 0.15. |  [optional] |
|**quasiIdsValues** | [**List&lt;GooglePrivacyDlpV2Value&gt;**](GooglePrivacyDlpV2Value.md) | The quasi-identifier values. |  [optional] |



