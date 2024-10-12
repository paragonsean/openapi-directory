

# VpcPeeringAuthorization

<p>Represents an authorization for a VPC peering connection between the VPC for an Amazon GameLift fleet and another VPC on an account you have access to. This authorization must exist and be valid for the peering connection to be established. Authorizations are valid for 24 hours after they are issued.</p> <p> <b>Related actions</b> </p> <p> <a href=\"https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets\">All APIs by task</a> </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gameLiftAwsAccountId** | [**String**](String.md) |  |  [optional] |
|**peerVpcAwsAccountId** | [**String**](String.md) |  |  [optional] |
|**peerVpcId** | [**String**](String.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**expirationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |



