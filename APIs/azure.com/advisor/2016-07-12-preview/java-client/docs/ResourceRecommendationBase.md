

# ResourceRecommendationBase

Advisor Recommendation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The fully qualified recommendation ID, for example /subscriptions/subscriptionId/resourceGroups/resourceGroup1/providers/Microsoft.ClassicCompute/virtualMachines/vm1/providers/Microsoft.Advisor/recommendations/recommendationGUID. |  [optional] |
|**name** | **String** | The name of recommendation. |  [optional] |
|**properties** | [**RecommendationProperties**](RecommendationProperties.md) |  |  [optional] |
|**suppressionIds** | **List&lt;UUID&gt;** | The list of snoozed and dismissed rules for the recommendation. |  [optional] |
|**type** | **String** | The recommendation type: Microsoft.Advisor/recommendations. |  [optional] |



