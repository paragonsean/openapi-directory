

# GlobalExplanation

Global explanations containing the top most important features after training.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**classLabel** | **String** | Class label for this set of global explanations. Will be empty/null for binary logistic and linear regression models. Sorted alphabetically in descending order. |  [optional] |
|**explanations** | [**List&lt;Explanation&gt;**](Explanation.md) | A list of the top global explanations. Sorted by absolute value of attribution in descending order. |  [optional] |



