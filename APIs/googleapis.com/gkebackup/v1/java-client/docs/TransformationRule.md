

# TransformationRule

A transformation rule to be applied against Kubernetes resources as they are selected for restoration from a Backup. A rule contains both filtering logic (which resources are subject to transform) and transformation logic.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Optional. The description is a user specified string description of the transformation rule. |  [optional] |
|**fieldActions** | [**List&lt;TransformationRuleAction&gt;**](TransformationRuleAction.md) | Required. A list of transformation rule actions to take against candidate resources. Actions are executed in order defined - this order matters, as they could potentially interfere with each other and the first operation could affect the outcome of the second operation. |  [optional] |
|**resourceFilter** | [**ResourceFilter**](ResourceFilter.md) |  |  [optional] |



