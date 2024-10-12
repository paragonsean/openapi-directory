

# ResourceCreationLimitPolicy

<p>A policy that puts limits on the number of game sessions that a player can create within a specified span of time. With this policy, you can control players' ability to consume available resources.</p> <p>The policy is evaluated when a player tries to create a new game session. On receiving a <code>CreateGameSession</code> request, Amazon GameLift checks that the player (identified by <code>CreatorId</code>) has created fewer than game session limit in the specified time period.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**newGameSessionsPerCreator** | [**Integer**](Integer.md) |  |  [optional] |
|**policyPeriodInMinutes** | [**Integer**](Integer.md) |  |  [optional] |



