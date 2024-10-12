# CloudDataplexApi.GoogleCloudDataplexV1Environment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Environment creation time. | [optional] [readonly] 
**description** | **String** | Optional. Description of the environment. | [optional] 
**displayName** | **String** | Optional. User friendly display name. | [optional] 
**endpoints** | [**GoogleCloudDataplexV1EnvironmentEndpoints**](GoogleCloudDataplexV1EnvironmentEndpoints.md) |  | [optional] 
**infrastructureSpec** | [**GoogleCloudDataplexV1EnvironmentInfrastructureSpec**](GoogleCloudDataplexV1EnvironmentInfrastructureSpec.md) |  | [optional] 
**labels** | **{String: String}** | Optional. User defined labels for the environment. | [optional] 
**name** | **String** | Output only. The relative resource name of the environment, of the form: projects/{project_id}/locations/{location_id}/lakes/{lake_id}/environment/{environment_id} | [optional] [readonly] 
**sessionSpec** | [**GoogleCloudDataplexV1EnvironmentSessionSpec**](GoogleCloudDataplexV1EnvironmentSessionSpec.md) |  | [optional] 
**sessionStatus** | [**GoogleCloudDataplexV1EnvironmentSessionStatus**](GoogleCloudDataplexV1EnvironmentSessionStatus.md) |  | [optional] 
**state** | **String** | Output only. Current state of the environment. | [optional] [readonly] 
**uid** | **String** | Output only. System generated globally unique ID for the environment. This ID will be different if the environment is deleted and re-created with the same name. | [optional] [readonly] 
**updateTime** | **String** | Output only. The time when the environment was last updated. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `CREATING` (value: `"CREATING"`)

* `DELETING` (value: `"DELETING"`)

* `ACTION_REQUIRED` (value: `"ACTION_REQUIRED"`)




