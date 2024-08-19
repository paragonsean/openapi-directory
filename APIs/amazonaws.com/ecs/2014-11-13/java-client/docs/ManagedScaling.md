

# ManagedScaling

<p>The managed scaling settings for the Auto Scaling group capacity provider.</p> <p>When managed scaling is turned on, Amazon ECS manages the scale-in and scale-out actions of the Auto Scaling group. Amazon ECS manages a target tracking scaling policy using an Amazon ECS managed CloudWatch metric with the specified <code>targetCapacity</code> value as the target value for the metric. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/asg-capacity-providers.html#asg-capacity-providers-managed-scaling\">Using managed scaling</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>If managed scaling is off, the user must manage the scaling of the Auto Scaling group.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**ManagedScalingStatus**](ManagedScalingStatus.md) |  |  [optional] |
|**targetCapacity** | [**Integer**](Integer.md) |  |  [optional] |
|**minimumScalingStepSize** | [**Integer**](Integer.md) |  |  [optional] |
|**maximumScalingStepSize** | [**Integer**](Integer.md) |  |  [optional] |
|**instanceWarmupPeriod** | [**Integer**](Integer.md) |  |  [optional] |



