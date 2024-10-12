

# TaskGroupStatus

Aggregated task status for a TaskGroup.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**counts** | **Map&lt;String, String&gt;** | Count of task in each state in the TaskGroup. The map key is task state name. |  [optional] |
|**instances** | [**List&lt;InstanceStatus&gt;**](InstanceStatus.md) | Status of instances allocated for the TaskGroup. |  [optional] |



