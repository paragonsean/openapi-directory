

# TaskDefinitionPlacementConstraint

<p>The constraint on task placement in the task definition. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html\">Task placement constraints</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <note> <p>Task placement constraints aren't supported for tasks run on Fargate.</p> </note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TaskDefinitionPlacementConstraintType**](TaskDefinitionPlacementConstraintType.md) |  |  [optional] |
|**expression** | [**String**](String.md) |  |  [optional] |



