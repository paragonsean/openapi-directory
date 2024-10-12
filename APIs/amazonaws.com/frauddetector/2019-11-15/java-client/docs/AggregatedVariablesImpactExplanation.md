

# AggregatedVariablesImpactExplanation

<p> The details of the impact of aggregated variables on the prediction score. </p> <p>Account Takeover Insights (ATI) model uses the login data you provide to continuously calculate a set of variables (aggregated variables) based on historical events. For example, the model might calculate the number of times an user has logged in using the same IP address. In this case, event variables used to derive the aggregated variables are <code>IP address</code> and <code>user</code>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventVariableNames** | [**List**](List.md) |  |  [optional] |
|**relativeImpact** | [**String**](String.md) |  |  [optional] |
|**logOddsImpact** | [**Float**](Float.md) |  |  [optional] |



