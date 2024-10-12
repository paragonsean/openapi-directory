# DataformApi.Operations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependencyTargets** | [**[Target]**](Target.md) | A list of actions that this action depends on. | [optional] 
**disabled** | **Boolean** | Whether this action is disabled (i.e. should not be run). | [optional] 
**hasOutput** | **Boolean** | Whether these operations produce an output relation. | [optional] 
**queries** | **[String]** | A list of arbitrary SQL statements that will be executed without alteration. | [optional] 
**relationDescriptor** | [**RelationDescriptor**](RelationDescriptor.md) |  | [optional] 
**tags** | **[String]** | Arbitrary, user-defined tags on this action. | [optional] 


