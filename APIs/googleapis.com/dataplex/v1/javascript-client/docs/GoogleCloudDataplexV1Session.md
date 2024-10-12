# CloudDataplexApi.GoogleCloudDataplexV1Session

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Session start time. | [optional] [readonly] 
**name** | **String** | Output only. The relative resource name of the content, of the form: projects/{project_id}/locations/{location_id}/lakes/{lake_id}/environment/{environment_id}/sessions/{session_id} | [optional] [readonly] 
**state** | **String** | Output only. State of Session | [optional] [readonly] 
**userId** | **String** | Output only. Email of user running the session. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `CREATING` (value: `"CREATING"`)

* `DELETING` (value: `"DELETING"`)

* `ACTION_REQUIRED` (value: `"ACTION_REQUIRED"`)




