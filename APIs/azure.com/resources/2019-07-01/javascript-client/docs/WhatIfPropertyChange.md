# ResourceManagementClient.WhatIfPropertyChange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | **Object** | The value of the property after the deployment is executed. | [optional] 
**before** | **Object** | The value of the property before the deployment is executed. | [optional] 
**children** | [**[WhatIfPropertyChange]**](WhatIfPropertyChange.md) | Nested property changes. | [optional] 
**path** | **String** | The path of the property. | 
**propertyChangeType** | **String** | The type of property change. | 



## Enum: PropertyChangeTypeEnum


* `Create` (value: `"Create"`)

* `Delete` (value: `"Delete"`)

* `Modify` (value: `"Modify"`)

* `Array` (value: `"Array"`)




