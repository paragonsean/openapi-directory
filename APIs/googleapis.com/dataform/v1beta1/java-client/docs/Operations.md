

# Operations

Represents a list of arbitrary database operations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dependencyTargets** | [**List&lt;Target&gt;**](Target.md) | A list of actions that this action depends on. |  [optional] |
|**disabled** | **Boolean** | Whether this action is disabled (i.e. should not be run). |  [optional] |
|**hasOutput** | **Boolean** | Whether these operations produce an output relation. |  [optional] |
|**queries** | **List&lt;String&gt;** | A list of arbitrary SQL statements that will be executed without alteration. |  [optional] |
|**relationDescriptor** | [**RelationDescriptor**](RelationDescriptor.md) |  |  [optional] |
|**tags** | **List&lt;String&gt;** | Arbitrary, user-defined tags on this action. |  [optional] |



