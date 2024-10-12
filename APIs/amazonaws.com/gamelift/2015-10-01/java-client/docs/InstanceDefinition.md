

# InstanceDefinition

<p> <b>This data type is used with the Amazon GameLift FleetIQ and game server groups.</b> </p> <p>An allowed instance type for a game server group. All game server groups must have at least two instance types defined for it. Amazon GameLift FleetIQ periodically evaluates each defined instance type for viability. It then updates the Auto Scaling group with the list of viable instance types.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instanceType** | [**GameServerGroupInstanceType**](GameServerGroupInstanceType.md) |  |  |
|**weightedCapacity** | [**String**](String.md) |  |  [optional] |



