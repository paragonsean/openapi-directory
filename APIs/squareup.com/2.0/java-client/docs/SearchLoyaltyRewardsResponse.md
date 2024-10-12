

# SearchLoyaltyRewardsResponse

A response that includes the loyalty rewards satisfying the search criteria.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | The pagination cursor to be used in a subsequent  request. If empty, this is the final response. |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |
|**rewards** | [**List&lt;LoyaltyReward&gt;**](LoyaltyReward.md) | The loyalty rewards that satisfy the search criteria. These are returned in descending order by &#x60;updated_at&#x60;. |  [optional] |



