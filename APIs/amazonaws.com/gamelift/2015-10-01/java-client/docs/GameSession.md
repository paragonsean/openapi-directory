

# GameSession

<p>Properties describing a game session.</p> <p>A game session in ACTIVE status can host players. When a game session ends, its status is set to <code>TERMINATED</code>. </p> <p>Once the session ends, the game session object is retained for 30 days. This means you can reuse idempotency token values after this time. Game session logs are retained for 14 days.</p> <p> <a href=\"https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\">All APIs by task</a> </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gameSessionId** | [**String**](String.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**fleetId** | [**String**](String.md) |  |  [optional] |
|**fleetArn** | [**String**](String.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**terminationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**currentPlayerSessionCount** | [**Integer**](Integer.md) |  |  [optional] |
|**maximumPlayerSessionCount** | [**Integer**](Integer.md) |  |  [optional] |
|**status** | [**GameSessionStatus**](GameSessionStatus.md) |  |  [optional] |
|**statusReason** | [**GameSessionStatusReason**](GameSessionStatusReason.md) |  |  [optional] |
|**gameProperties** | [**List**](List.md) |  |  [optional] |
|**ipAddress** | [**String**](String.md) |  |  [optional] |
|**dnsName** | [**String**](String.md) |  |  [optional] |
|**port** | [**Integer**](Integer.md) |  |  [optional] |
|**playerSessionCreationPolicy** | [**PlayerSessionCreationPolicy**](PlayerSessionCreationPolicy.md) |  |  [optional] |
|**creatorId** | [**String**](String.md) |  |  [optional] |
|**gameSessionData** | [**String**](String.md) |  |  [optional] |
|**matchmakerData** | [**String**](String.md) |  |  [optional] |
|**location** | [**String**](String.md) |  |  [optional] |



