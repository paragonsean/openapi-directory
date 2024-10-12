

# HierarchiesExpandParameter

Definition of whether to expand hierarchy nodes in the same search instances call.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | [**KindEnum**](#KindEnum) | Kind of the expansion of hierarchy nodes. When it is set to &#39;UntilChildren&#39;, the hierarchy nodes are expanded recursively until there is more than one child. When it is set to &#39;OneLevel&#39;, the hierarchies are expanded only at the single level matching path search instances parameter. Optional, default is &#39;UntilChildren&#39;. |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| UNTIL_CHILDREN | &quot;UntilChildren&quot; |
| ONE_LEVEL | &quot;OneLevel&quot; |



