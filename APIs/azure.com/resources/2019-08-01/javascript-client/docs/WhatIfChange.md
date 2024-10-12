# ResourceManagementClient.WhatIfChange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | **Object** | The predicted snapshot of the resource after the deployment is executed. | [optional] 
**before** | **Object** | The snapshot of the resource before the deployment is executed. | [optional] 
**changeType** | **String** | Type of change that will be made to the resource when the deployment is executed. | 
**delta** | [**[WhatIfPropertyChange]**](WhatIfPropertyChange.md) | The predicted changes to resource properties. | [optional] 
**resourceId** | **String** | Resource ID | 



## Enum: ChangeTypeEnum


* `Create` (value: `"Create"`)

* `Delete` (value: `"Delete"`)

* `Ignore` (value: `"Ignore"`)

* `Deploy` (value: `"Deploy"`)

* `NoChange` (value: `"NoChange"`)

* `Modify` (value: `"Modify"`)




