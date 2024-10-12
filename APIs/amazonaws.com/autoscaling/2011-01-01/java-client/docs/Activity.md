

# Activity

Describes scaling activity, which is a long-running process that represents a change to your Auto Scaling group, such as changing its size or replacing an instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activityId** | [**String**](String.md) |  |  |
|**autoScalingGroupName** | [**String**](String.md) |  |  |
|**description** | [**String**](String.md) |  |  [optional] |
|**cause** | [**String**](String.md) |  |  |
|**startTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**endTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**statusCode** | [**ScalingActivityStatusCode**](ScalingActivityStatusCode.md) |  |  |
|**statusMessage** | [**String**](String.md) |  |  [optional] |
|**progress** | [**Integer**](Integer.md) |  |  [optional] |
|**details** | [**String**](String.md) |  |  [optional] |
|**autoScalingGroupState** | [**String**](String.md) |  |  [optional] |
|**autoScalingGroupARN** | [**String**](String.md) |  |  [optional] |



