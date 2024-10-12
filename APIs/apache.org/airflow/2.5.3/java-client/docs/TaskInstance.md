

# TaskInstance


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dagId** | **String** |  |  [optional] |
|**dagRunId** | **String** | The DagRun ID for this task instance  *New in version 2.3.0*  |  [optional] |
|**duration** | **BigDecimal** |  |  [optional] |
|**endDate** | **String** |  |  [optional] |
|**executionDate** | **String** |  |  [optional] |
|**executorConfig** | **String** |  |  [optional] |
|**hostname** | **String** |  |  [optional] |
|**mapIndex** | **Integer** |  |  [optional] |
|**maxTries** | **Integer** |  |  [optional] |
|**note** | **String** | Contains manually entered notes by the user about the TaskInstance.  *New in version 2.5.0*  |  [optional] |
|**operator** | **String** | *Changed in version 2.1.1*&amp;#58; Field becomes nullable.  |  [optional] |
|**pid** | **Integer** |  |  [optional] |
|**pool** | **String** |  |  [optional] |
|**poolSlots** | **Integer** |  |  [optional] |
|**priorityWeight** | **Integer** |  |  [optional] |
|**queue** | **String** |  |  [optional] |
|**queuedWhen** | **String** |  |  [optional] |
|**renderedFields** | **Object** | JSON object describing rendered fields.  *New in version 2.3.0*  |  [optional] |
|**slaMiss** | [**SLAMiss**](SLAMiss.md) |  |  [optional] |
|**startDate** | **String** |  |  [optional] |
|**state** | **TaskState** |  |  [optional] |
|**taskId** | **String** |  |  [optional] |
|**trigger** | [**Trigger**](Trigger.md) |  |  [optional] |
|**triggererJob** | [**Job**](Job.md) |  |  [optional] |
|**tryNumber** | **Integer** |  |  [optional] |
|**unixname** | **String** |  |  [optional] |



