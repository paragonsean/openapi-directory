

# MonitoredResourceDescriptor

An object that describes the schema of a MonitoredResource object using a type name and a set of labels. For example, the monitored resource descriptor for Google Compute Engine VM instances has a type of \"gce_instance\" and specifies the use of the labels \"instance_id\" and \"zone\" to identify particular VM instances.Different APIs can support different monitored resource types. APIs generally provide a list method that returns the monitored resource descriptors used by the API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Optional. A detailed description of the monitored resource type that might be used in documentation. |  [optional] |
|**displayName** | **String** | Optional. A concise name for the monitored resource type that might be displayed in user interfaces. It should be a Title Cased Noun Phrase, without any article or other determiners. For example, \&quot;Google Cloud SQL Database\&quot;. |  [optional] |
|**labels** | [**List&lt;LabelDescriptor&gt;**](LabelDescriptor.md) | Required. A set of labels used to describe instances of this monitored resource type. For example, an individual Google Cloud SQL database is identified by values for the labels \&quot;database_id\&quot; and \&quot;zone\&quot;. |  [optional] |
|**launchStage** | [**LaunchStageEnum**](#LaunchStageEnum) | Optional. The launch stage of the monitored resource definition. |  [optional] |
|**name** | **String** | Optional. The resource name of the monitored resource descriptor: \&quot;projects/{project_id}/monitoredResourceDescriptors/{type}\&quot; where {type} is the value of the type field in this object and {project_id} is a project ID that provides API-specific context for accessing the type. APIs that do not use project information can use the resource name format \&quot;monitoredResourceDescriptors/{type}\&quot;. |  [optional] |
|**type** | **String** | Required. The monitored resource type. For example, the type \&quot;cloudsql_database\&quot; represents databases in Google Cloud SQL. For a list of types, see Monitored resource types (https://cloud.google.com/monitoring/api/resources) and Logging resource types (https://cloud.google.com/logging/docs/api/v2/resource-list). |  [optional] |



## Enum: LaunchStageEnum

| Name | Value |
|---- | -----|
| LAUNCH_STAGE_UNSPECIFIED | &quot;LAUNCH_STAGE_UNSPECIFIED&quot; |
| UNIMPLEMENTED | &quot;UNIMPLEMENTED&quot; |
| PRELAUNCH | &quot;PRELAUNCH&quot; |
| EARLY_ACCESS | &quot;EARLY_ACCESS&quot; |
| ALPHA | &quot;ALPHA&quot; |
| BETA | &quot;BETA&quot; |
| GA | &quot;GA&quot; |
| DEPRECATED | &quot;DEPRECATED&quot; |



