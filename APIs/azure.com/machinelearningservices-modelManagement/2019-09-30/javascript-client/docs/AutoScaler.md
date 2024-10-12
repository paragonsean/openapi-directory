# AzureMachineLearningModelManagementService.AutoScaler

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoscaleEnabled** | **Boolean** | Option to enable/disable auto scaling. | [optional] 
**maxReplicas** | **Number** | The maximum number of replicas in the cluster. | [optional] 
**minReplicas** | **Number** | The minimum number of replicas to scale down to. | [optional] 
**refreshPeriodInSeconds** | **Number** | The amount of seconds to wait between auto scale updates. | [optional] 
**targetUtilization** | **Number** | The target utilization percentage to use for determining whether to scale the cluster. | [optional] 


