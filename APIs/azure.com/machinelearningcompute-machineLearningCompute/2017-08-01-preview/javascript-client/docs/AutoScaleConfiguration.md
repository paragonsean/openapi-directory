# MachineLearningComputeManagementClient.AutoScaleConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxReplicas** | **Number** | The maximum number of replicas for each service. | [optional] 
**minReplicas** | **Number** | The minimum number of replicas for each service. | [optional] 
**refreshPeriodInSeconds** | **Number** | Refresh period in seconds. | [optional] 
**status** | **String** | If auto-scale is enabled for all services. Each service can turn it off individually. | [optional] [default to &#39;Disabled&#39;]
**targetUtilization** | **Number** | The target utilization. | [optional] 



## Enum: StatusEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




