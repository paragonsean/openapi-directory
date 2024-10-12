# ConnectorsApi.EventingDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customEventTypes** | **Boolean** | Output only. Custom Event Types. | [optional] [readonly] 
**description** | **String** | Output only. Description. | [optional] [readonly] 
**documentationLink** | **String** | Output only. Link to public documentation. | [optional] [readonly] 
**iconLocation** | **String** | Output only. Cloud storage location of the icon. | [optional] [readonly] 
**launchStage** | **String** | Output only. Eventing Launch Stage. | [optional] [readonly] 
**name** | **String** | Output only. Name of the Eventing trigger. | [optional] [readonly] 
**searchTags** | **[String]** | Output only. Array of search keywords. | [optional] [readonly] 
**type** | **String** | Output only. The type of the event listener for a specific connector. | [optional] [readonly] 



## Enum: LaunchStageEnum


* `LAUNCH_STAGE_UNSPECIFIED` (value: `"LAUNCH_STAGE_UNSPECIFIED"`)

* `PREVIEW` (value: `"PREVIEW"`)

* `GA` (value: `"GA"`)

* `DEPRECATED` (value: `"DEPRECATED"`)

* `PRIVATE_PREVIEW` (value: `"PRIVATE_PREVIEW"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `WEBHOOK` (value: `"WEBHOOK"`)

* `JMS` (value: `"JMS"`)




