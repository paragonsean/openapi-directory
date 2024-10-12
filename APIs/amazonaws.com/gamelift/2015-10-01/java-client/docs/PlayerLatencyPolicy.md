

# PlayerLatencyPolicy

Sets a latency cap for individual players when placing a game session. With a latency policy in force, a game session cannot be placed in a fleet location where a player reports latency higher than the cap. Latency policies are used only with placement request that provide player latency information. Player latency policies can be stacked to gradually relax latency requirements over time. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maximumIndividualPlayerLatencyMilliseconds** | [**Integer**](Integer.md) |  |  [optional] |
|**policyDurationSeconds** | [**Integer**](Integer.md) |  |  [optional] |



