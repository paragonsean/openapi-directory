# ServiceConsumerManagementApi.MonitoredResourceDescriptor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Optional. A detailed description of the monitored resource type that might be used in documentation. | [optional] 
**displayName** | **String** | Optional. A concise name for the monitored resource type that might be displayed in user interfaces. It should be a Title Cased Noun Phrase, without any article or other determiners. For example, &#x60;\&quot;Google Cloud SQL Database\&quot;&#x60;. | [optional] 
**labels** | [**[LabelDescriptor]**](LabelDescriptor.md) | Required. A set of labels used to describe instances of this monitored resource type. For example, an individual Google Cloud SQL database is identified by values for the labels &#x60;\&quot;database_id\&quot;&#x60; and &#x60;\&quot;zone\&quot;&#x60;. | [optional] 
**launchStage** | **String** | Optional. The launch stage of the monitored resource definition. | [optional] 
**name** | **String** | Optional. The resource name of the monitored resource descriptor: &#x60;\&quot;projects/{project_id}/monitoredResourceDescriptors/{type}\&quot;&#x60; where {type} is the value of the &#x60;type&#x60; field in this object and {project_id} is a project ID that provides API-specific context for accessing the type. APIs that do not use project information can use the resource name format &#x60;\&quot;monitoredResourceDescriptors/{type}\&quot;&#x60;. | [optional] 
**type** | **String** | Required. The monitored resource type. For example, the type &#x60;\&quot;cloudsql_database\&quot;&#x60; represents databases in Google Cloud SQL. For a list of types, see [Monitored resource types](https://cloud.google.com/monitoring/api/resources) and [Logging resource types](https://cloud.google.com/logging/docs/api/v2/resource-list). | [optional] 



## Enum: LaunchStageEnum


* `LAUNCH_STAGE_UNSPECIFIED` (value: `"LAUNCH_STAGE_UNSPECIFIED"`)

* `UNIMPLEMENTED` (value: `"UNIMPLEMENTED"`)

* `PRELAUNCH` (value: `"PRELAUNCH"`)

* `EARLY_ACCESS` (value: `"EARLY_ACCESS"`)

* `ALPHA` (value: `"ALPHA"`)

* `BETA` (value: `"BETA"`)

* `GA` (value: `"GA"`)

* `DEPRECATED` (value: `"DEPRECATED"`)




