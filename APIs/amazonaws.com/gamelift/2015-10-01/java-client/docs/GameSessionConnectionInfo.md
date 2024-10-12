

# GameSessionConnectionInfo

Connection information for a new game session that is created in response to a start matchmaking request. Once a match is made, the FlexMatch engine creates a new game session for it. This information, including the game session endpoint and player sessions for each player in the original matchmaking request, is added to the matchmaking ticket.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gameSessionArn** | [**String**](String.md) |  |  [optional] |
|**ipAddress** | [**String**](String.md) |  |  [optional] |
|**dnsName** | [**String**](String.md) |  |  [optional] |
|**port** | [**Integer**](Integer.md) |  |  [optional] |
|**matchedPlayerSessions** | [**List**](List.md) |  |  [optional] |



