

# PlayerSession

<p>Represents a player session. Player sessions are created either for a specific game session, or as part of a game session placement or matchmaking request. A player session can represents a reserved player slot in a game session (when status is <code>RESERVED</code>) or actual player activity in a game session (when status is <code>ACTIVE</code>). A player session object, including player data, is automatically passed to a game session when the player connects to the game session and is validated. After the game session ends, player sessions information is retained for 30 days and then removed.</p> <p> <b>Related actions</b> </p> <p> <a href=\"https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\">All APIs by task</a> </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**playerSessionId** | [**String**](String.md) |  |  [optional] |
|**playerId** | [**String**](String.md) |  |  [optional] |
|**gameSessionId** | [**String**](String.md) |  |  [optional] |
|**fleetId** | [**String**](String.md) |  |  [optional] |
|**fleetArn** | [**String**](String.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**terminationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**status** | [**PlayerSessionStatus**](PlayerSessionStatus.md) |  |  [optional] |
|**ipAddress** | [**String**](String.md) |  |  [optional] |
|**dnsName** | [**String**](String.md) |  |  [optional] |
|**port** | [**Integer**](Integer.md) |  |  [optional] |
|**playerData** | [**String**](String.md) |  |  [optional] |



