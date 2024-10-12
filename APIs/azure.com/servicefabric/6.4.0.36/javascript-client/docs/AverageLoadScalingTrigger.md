# ServiceFabricClientApis.AverageLoadScalingTrigger

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lowerLoadThreshold** | **Number** | Lower load threshold (if average load is below this threshold, service will scale down). | 
**metric** | [**AutoScalingMetric**](AutoScalingMetric.md) |  | 
**scaleIntervalInSeconds** | **Number** | Scale interval that indicates how often will this trigger be checked. | 
**upperLoadThreshold** | **Number** | Upper load threshold (if average load is above this threshold, service will scale up). | 


