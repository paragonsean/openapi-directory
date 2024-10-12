

# WhatIfPropertyChange

The predicted change to the resource property.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**after** | **Object** | The value of the property after the deployment is executed. |  [optional] |
|**before** | **Object** | The value of the property before the deployment is executed. |  [optional] |
|**children** | [**List&lt;WhatIfPropertyChange&gt;**](WhatIfPropertyChange.md) | Nested property changes. |  [optional] |
|**path** | **String** | The path of the property. |  |
|**propertyChangeType** | [**PropertyChangeTypeEnum**](#PropertyChangeTypeEnum) | The type of property change. |  |



## Enum: PropertyChangeTypeEnum

| Name | Value |
|---- | -----|
| CREATE | &quot;Create&quot; |
| DELETE | &quot;Delete&quot; |
| MODIFY | &quot;Modify&quot; |
| ARRAY | &quot;Array&quot; |



