

# PlayerLatency

Regional latency information for a player, used when requesting a new game session. This value indicates the amount of time lag that exists when the player is connected to a fleet in the specified Region. The relative difference between a player's latency values for multiple Regions are used to determine which fleets are best suited to place a new game session for the player. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**playerId** | [**String**](String.md) |  |  [optional] |
|**regionIdentifier** | [**String**](String.md) |  |  [optional] |
|**latencyInMilliseconds** | [**Float**](Float.md) |  |  [optional] |



