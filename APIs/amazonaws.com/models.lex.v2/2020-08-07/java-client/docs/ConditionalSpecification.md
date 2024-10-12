

# ConditionalSpecification

Provides a list of conditional branches. Branches are evaluated in the order that they are entered in the list. The first branch with a condition that evaluates to true is executed. The last branch in the list is the default branch. The default branch should not have any condition expression. The default branch is executed if no other branch has a matching condition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | [**Boolean**](Boolean.md) |  |  |
|**conditionalBranches** | [**List**](List.md) |  |  |
|**defaultBranch** | [**ConditionalSpecificationDefaultBranch**](ConditionalSpecificationDefaultBranch.md) |  |  |



