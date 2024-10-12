# AirflowApiStable.Task

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classRef** | [**ClassReference**](ClassReference.md) |  | [optional] 
**dependsOnPast** | **Boolean** |  | [optional] [readonly] 
**downstreamTaskIds** | **[String]** |  | [optional] [readonly] 
**endDate** | **Date** |  | [optional] [readonly] 
**executionTimeout** | [**TimeDelta**](TimeDelta.md) |  | [optional] 
**extraLinks** | [**[TaskExtraLinksInner]**](TaskExtraLinksInner.md) |  | [optional] [readonly] 
**isMapped** | **Boolean** |  | [optional] [readonly] 
**owner** | **String** |  | [optional] [readonly] 
**pool** | **String** |  | [optional] [readonly] 
**poolSlots** | **Number** |  | [optional] [readonly] 
**priorityWeight** | **Number** |  | [optional] [readonly] 
**queue** | **String** |  | [optional] [readonly] 
**retries** | **Number** |  | [optional] [readonly] 
**retryDelay** | [**TimeDelta**](TimeDelta.md) |  | [optional] 
**retryExponentialBackoff** | **Boolean** |  | [optional] [readonly] 
**startDate** | **Date** |  | [optional] [readonly] 
**subDag** | [**DAG**](DAG.md) |  | [optional] 
**taskId** | **String** |  | [optional] [readonly] 
**templateFields** | **[String]** |  | [optional] [readonly] 
**triggerRule** | [**TriggerRule**](TriggerRule.md) |  | [optional] 
**uiColor** | **String** | Color in hexadecimal notation. | [optional] 
**uiFgcolor** | **String** | Color in hexadecimal notation. | [optional] 
**waitForDownstream** | **Boolean** |  | [optional] [readonly] 
**weightRule** | [**WeightRule**](WeightRule.md) |  | [optional] 


