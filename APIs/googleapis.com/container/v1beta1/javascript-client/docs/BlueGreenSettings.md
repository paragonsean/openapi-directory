# KubernetesEngineApi.BlueGreenSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoscaledRolloutPolicy** | **Object** | Autoscaled rollout policy uses cluster autoscaler during blue-green upgrades to scale both the green and blue pools. | [optional] 
**nodePoolSoakDuration** | **String** | Time needed after draining entire blue pool. After this period, blue pool will be cleaned up. | [optional] 
**standardRolloutPolicy** | [**StandardRolloutPolicy**](StandardRolloutPolicy.md) |  | [optional] 


