

# Assertion

Represents an assertion upon a SQL query which is required return zero rows.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dependencyTargets** | [**List&lt;Target&gt;**](Target.md) | A list of actions that this action depends on. |  [optional] |
|**disabled** | **Boolean** | Whether this action is disabled (i.e. should not be run). |  [optional] |
|**parentAction** | [**Target**](Target.md) |  |  [optional] |
|**relationDescriptor** | [**RelationDescriptor**](RelationDescriptor.md) |  |  [optional] |
|**selectQuery** | **String** | The SELECT query which must return zero rows in order for this assertion to succeed. |  [optional] |
|**tags** | **List&lt;String&gt;** | Arbitrary, user-defined tags on this action. |  [optional] |



