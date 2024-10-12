

# FleetCapacity

<p>Current resource capacity settings in a specified fleet or location. The location value might refer to a fleet's remote location or its home Region. </p> <p> <b>Related actions</b> </p> <p> <a href=\"https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html\">DescribeFleetCapacity</a> | <a href=\"https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html\">DescribeFleetLocationCapacity</a> | <a href=\"https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetCapacity.html\">UpdateFleetCapacity</a> </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fleetId** | [**String**](String.md) |  |  [optional] |
|**fleetArn** | [**String**](String.md) |  |  [optional] |
|**instanceType** | [**EC2InstanceType**](EC2InstanceType.md) |  |  [optional] |
|**instanceCounts** | [**EC2InstanceCounts**](EC2InstanceCounts.md) |  |  [optional] |
|**location** | [**String**](String.md) |  |  [optional] |



