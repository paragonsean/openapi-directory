

# VpcPeeringConnection

<p>Represents a peering connection between a VPC on one of your Amazon Web Services accounts and the VPC for your Amazon GameLift fleets. This record may be for an active peering connection or a pending connection that has not yet been established.</p> <p> <b>Related actions</b> </p> <p> <a href=\"https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\">All APIs by task</a> </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fleetId** | [**String**](String.md) |  |  [optional] |
|**fleetArn** | [**String**](String.md) |  |  [optional] |
|**ipV4CidrBlock** | [**String**](String.md) |  |  [optional] |
|**vpcPeeringConnectionId** | [**String**](String.md) |  |  [optional] |
|**status** | [**VpcPeeringConnectionStatus**](VpcPeeringConnectionStatus.md) |  |  [optional] |
|**peerVpcId** | [**String**](String.md) |  |  [optional] |
|**gameLiftVpcId** | [**String**](String.md) |  |  [optional] |



