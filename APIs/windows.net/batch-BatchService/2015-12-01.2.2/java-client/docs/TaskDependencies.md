

# TaskDependencies

Specifies any dependencies of a task.  Any task that is explicitly specified or within a dependency range must complete before the dependant task will be scheduled.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**taskIdRanges** | [**List&lt;TaskIdRange&gt;**](TaskIdRange.md) | Gets or sets the list of task ranges that must complete before this task can be scheduled. |  [optional] |
|**taskIds** | **List&lt;String&gt;** | Gets or sets the list of task ids that must complete before this task can be scheduled. |  [optional] |



