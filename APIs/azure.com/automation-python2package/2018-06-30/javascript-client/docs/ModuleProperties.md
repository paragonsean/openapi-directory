# AutomationManagement.ModuleProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activityCount** | **Number** | Gets or sets the activity count of the module. | [optional] 
**contentLink** | [**ContentLink**](ContentLink.md) |  | [optional] 
**creationTime** | **Date** | Gets or sets the creation time. | [optional] 
**description** | **String** | Gets or sets the description. | [optional] 
**error** | [**ModuleErrorInfo**](ModuleErrorInfo.md) |  | [optional] 
**isComposite** | **Boolean** | Gets or sets type of module, if its composite or not. | [optional] 
**isGlobal** | **Boolean** | Gets or sets the isGlobal flag of the module. | [optional] 
**lastModifiedTime** | **Date** | Gets or sets the last modified time. | [optional] 
**provisioningState** | **String** | Gets or sets the provisioning state of the module. | [optional] 
**sizeInBytes** | **Number** | Gets or sets the size in bytes of the module. | [optional] 
**version** | **String** | Gets or sets the version of the module. | [optional] 



## Enum: ProvisioningStateEnum


* `Created` (value: `"Created"`)

* `Creating` (value: `"Creating"`)

* `StartingImportModuleRunbook` (value: `"StartingImportModuleRunbook"`)

* `RunningImportModuleRunbook` (value: `"RunningImportModuleRunbook"`)

* `ContentRetrieved` (value: `"ContentRetrieved"`)

* `ContentDownloaded` (value: `"ContentDownloaded"`)

* `ContentValidated` (value: `"ContentValidated"`)

* `ConnectionTypeImported` (value: `"ConnectionTypeImported"`)

* `ContentStored` (value: `"ContentStored"`)

* `ModuleDataStored` (value: `"ModuleDataStored"`)

* `ActivitiesStored` (value: `"ActivitiesStored"`)

* `ModuleImportRunbookComplete` (value: `"ModuleImportRunbookComplete"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Cancelled` (value: `"Cancelled"`)

* `Updating` (value: `"Updating"`)




