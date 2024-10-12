

# ModuleProperties

Definition of the module property type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activityCount** | **Integer** | Gets or sets the activity count of the module. |  [optional] |
|**contentLink** | [**ContentLink**](ContentLink.md) |  |  [optional] |
|**creationTime** | **OffsetDateTime** | Gets or sets the creation time. |  [optional] |
|**description** | **String** | Gets or sets the description. |  [optional] |
|**error** | [**ModuleErrorInfo**](ModuleErrorInfo.md) |  |  [optional] |
|**isComposite** | **Boolean** | Gets or sets type of module, if its composite or not. |  [optional] |
|**isGlobal** | **Boolean** | Gets or sets the isGlobal flag of the module. |  [optional] |
|**lastModifiedTime** | **OffsetDateTime** | Gets or sets the last modified time. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Gets or sets the provisioning state of the module. |  [optional] |
|**sizeInBytes** | **Long** | Gets or sets the size in bytes of the module. |  [optional] |
|**version** | **String** | Gets or sets the version of the module. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATED | &quot;Created&quot; |
| CREATING | &quot;Creating&quot; |
| STARTING_IMPORT_MODULE_RUNBOOK | &quot;StartingImportModuleRunbook&quot; |
| RUNNING_IMPORT_MODULE_RUNBOOK | &quot;RunningImportModuleRunbook&quot; |
| CONTENT_RETRIEVED | &quot;ContentRetrieved&quot; |
| CONTENT_DOWNLOADED | &quot;ContentDownloaded&quot; |
| CONTENT_VALIDATED | &quot;ContentValidated&quot; |
| CONNECTION_TYPE_IMPORTED | &quot;ConnectionTypeImported&quot; |
| CONTENT_STORED | &quot;ContentStored&quot; |
| MODULE_DATA_STORED | &quot;ModuleDataStored&quot; |
| ACTIVITIES_STORED | &quot;ActivitiesStored&quot; |
| MODULE_IMPORT_RUNBOOK_COMPLETE | &quot;ModuleImportRunbookComplete&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| UPDATING | &quot;Updating&quot; |



