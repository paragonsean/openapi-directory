

# TaskFilter

<p>You can use API filters to narrow down the list of resources returned by <code>ListTasks</code>. For example, to retrieve all tasks on a source location, you can use <code>ListTasks</code> with filter name <code>LocationId</code> and <code>Operator Equals</code> with the ARN for the location.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/query-resources.html\">filtering DataSync resources</a>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**TaskFilterName**](TaskFilterName.md) |  |  |
|**values** | [**List**](List.md) |  |  |
|**operator** | [**Operator**](Operator.md) |  |  |



