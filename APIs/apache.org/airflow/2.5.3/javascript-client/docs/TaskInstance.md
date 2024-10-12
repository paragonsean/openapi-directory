# AirflowApiStable.TaskInstance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dagId** | **String** |  | [optional] 
**dagRunId** | **String** | The DagRun ID for this task instance  *New in version 2.3.0*  | [optional] 
**duration** | **Number** |  | [optional] 
**endDate** | **String** |  | [optional] 
**executionDate** | **String** |  | [optional] 
**executorConfig** | **String** |  | [optional] 
**hostname** | **String** |  | [optional] 
**mapIndex** | **Number** |  | [optional] 
**maxTries** | **Number** |  | [optional] 
**note** | **String** | Contains manually entered notes by the user about the TaskInstance.  *New in version 2.5.0*  | [optional] 
**operator** | **String** | *Changed in version 2.1.1*&amp;#58; Field becomes nullable.  | [optional] 
**pid** | **Number** |  | [optional] 
**pool** | **String** |  | [optional] 
**poolSlots** | **Number** |  | [optional] 
**priorityWeight** | **Number** |  | [optional] 
**queue** | **String** |  | [optional] 
**queuedWhen** | **String** |  | [optional] 
**renderedFields** | **Object** | JSON object describing rendered fields.  *New in version 2.3.0*  | [optional] 
**slaMiss** | [**SLAMiss**](SLAMiss.md) |  | [optional] 
**startDate** | **String** |  | [optional] 
**state** | [**TaskState**](TaskState.md) |  | [optional] 
**taskId** | **String** |  | [optional] 
**trigger** | [**Trigger**](Trigger.md) |  | [optional] 
**triggererJob** | [**Job**](Job.md) |  | [optional] 
**tryNumber** | **Number** |  | [optional] 
**unixname** | **String** |  | [optional] 


