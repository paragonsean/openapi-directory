

# GameServerGroup

<p> <b>This data type is used with the Amazon GameLift FleetIQ and game server groups.</b> </p> <p>Properties that describe a game server group resource. A game server group manages certain properties related to a corresponding Amazon EC2 Auto Scaling group. </p> <p>A game server group is created by a successful call to <code>CreateGameServerGroup</code> and deleted by calling <code>DeleteGameServerGroup</code>. Game server group activity can be temporarily suspended and resumed by calling <code>SuspendGameServerGroup</code> and <code>ResumeGameServerGroup</code>, respectively. </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gameServerGroupName** | [**String**](String.md) |  |  [optional] |
|**gameServerGroupArn** | [**String**](String.md) |  |  [optional] |
|**roleArn** | [**String**](String.md) |  |  [optional] |
|**instanceDefinitions** | [**List**](List.md) |  |  [optional] |
|**balancingStrategy** | [**BalancingStrategy**](BalancingStrategy.md) |  |  [optional] |
|**gameServerProtectionPolicy** | [**GameServerProtectionPolicy**](GameServerProtectionPolicy.md) |  |  [optional] |
|**autoScalingGroupArn** | [**String**](String.md) |  |  [optional] |
|**status** | [**GameServerGroupStatus**](GameServerGroupStatus.md) |  |  [optional] |
|**statusReason** | [**String**](String.md) |  |  [optional] |
|**suspendedActions** | [**List**](List.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastUpdatedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |



