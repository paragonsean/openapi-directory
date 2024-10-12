

# WhatIfChange

Information about a single resource change predicted by What-If operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**after** | **Object** | The predicted snapshot of the resource after the deployment is executed. |  [optional] |
|**before** | **Object** | The snapshot of the resource before the deployment is executed. |  [optional] |
|**changeType** | [**ChangeTypeEnum**](#ChangeTypeEnum) | Type of change that will be made to the resource when the deployment is executed. |  |
|**delta** | [**List&lt;WhatIfPropertyChange&gt;**](WhatIfPropertyChange.md) | The predicted changes to resource properties. |  [optional] |
|**resourceId** | **String** | Resource ID |  |



## Enum: ChangeTypeEnum

| Name | Value |
|---- | -----|
| CREATE | &quot;Create&quot; |
| DELETE | &quot;Delete&quot; |
| IGNORE | &quot;Ignore&quot; |
| DEPLOY | &quot;Deploy&quot; |
| NO_CHANGE | &quot;NoChange&quot; |
| MODIFY | &quot;Modify&quot; |



