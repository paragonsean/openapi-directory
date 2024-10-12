

# TaskDependencies


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**taskIdRanges** | [**List&lt;TaskIdRange&gt;**](TaskIdRange.md) |  |  [optional] |
|**taskIds** | **List&lt;String&gt;** | The taskIds collection is limited to 64000 characters total (i.e. the combined length of all task IDs). If the taskIds collection exceeds the maximum length, the Add Task request fails with error code TaskDependencyListTooLong. In this case consider using task ID ranges instead. |  [optional] |



