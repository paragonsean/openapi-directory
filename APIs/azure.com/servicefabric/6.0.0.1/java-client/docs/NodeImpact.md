

# NodeImpact

Describes the expected impact of a repair to a particular node.  This type supports the Service Fabric platform; it is not meant to be used directly from your code. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**impactLevel** | [**ImpactLevelEnum**](#ImpactLevelEnum) | The level of impact expected. |  [optional] |
|**nodeName** | **String** | The name of the impacted node. |  |



## Enum: ImpactLevelEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| NONE | &quot;None&quot; |
| RESTART | &quot;Restart&quot; |
| REMOVE_DATA | &quot;RemoveData&quot; |
| REMOVE_NODE | &quot;RemoveNode&quot; |



