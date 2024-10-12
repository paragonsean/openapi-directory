# DataformApi.Assertion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependencyTargets** | [**[Target]**](Target.md) | A list of actions that this action depends on. | [optional] 
**disabled** | **Boolean** | Whether this action is disabled (i.e. should not be run). | [optional] 
**parentAction** | [**Target**](Target.md) |  | [optional] 
**relationDescriptor** | [**RelationDescriptor**](RelationDescriptor.md) |  | [optional] 
**selectQuery** | **String** | The SELECT query which must return zero rows in order for this assertion to succeed. | [optional] 
**tags** | **[String]** | Arbitrary, user-defined tags on this action. | [optional] 


