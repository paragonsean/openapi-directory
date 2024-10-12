

# TrafficRoutingConfig

Defines the traffic routing strategy during an endpoint deployment to shift traffic from the old fleet to the new fleet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TrafficRoutingConfigType**](TrafficRoutingConfigType.md) |  |  |
|**waitIntervalInSeconds** | [**Integer**](Integer.md) |  |  |
|**canarySize** | [**TrafficRoutingConfigCanarySize**](TrafficRoutingConfigCanarySize.md) |  |  [optional] |
|**linearStepSize** | [**TrafficRoutingConfigLinearStepSize**](TrafficRoutingConfigLinearStepSize.md) |  |  [optional] |



