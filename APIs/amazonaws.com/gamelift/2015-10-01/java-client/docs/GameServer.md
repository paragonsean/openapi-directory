

# GameServer

<p> <b>This data type is used with the Amazon GameLift FleetIQ and game server groups.</b> </p> <p>Properties describing a game server that is running on an instance in a game server group. </p> <p>A game server is created by a successful call to <code>RegisterGameServer</code> and deleted by calling <code>DeregisterGameServer</code>. A game server is claimed to host a game session by calling <code>ClaimGameServer</code>. </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gameServerGroupName** | [**String**](String.md) |  |  [optional] |
|**gameServerGroupArn** | [**String**](String.md) |  |  [optional] |
|**gameServerId** | [**String**](String.md) |  |  [optional] |
|**instanceId** | [**String**](String.md) |  |  [optional] |
|**connectionInfo** | [**String**](String.md) |  |  [optional] |
|**gameServerData** | [**String**](String.md) |  |  [optional] |
|**claimStatus** | [**GameServerClaimStatus**](GameServerClaimStatus.md) |  |  [optional] |
|**utilizationStatus** | [**GameServerUtilizationStatus**](GameServerUtilizationStatus.md) |  |  [optional] |
|**registrationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastClaimTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastHealthCheckTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |



