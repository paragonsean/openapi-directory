# BigQueryApi.GlobalExplanation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classLabel** | **String** | Class label for this set of global explanations. Will be empty/null for binary logistic and linear regression models. Sorted alphabetically in descending order. | [optional] 
**explanations** | [**[Explanation]**](Explanation.md) | A list of the top global explanations. Sorted by absolute value of attribution in descending order. | [optional] 


