# ApigeeApi.GoogleCloudApigeeV1EnvironmentGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **String** | Output only. The time at which the environment group was created as milliseconds since epoch. | [optional] [readonly] 
**hostnames** | **[String]** | Required. Host names for this environment group. | [optional] 
**lastModifiedAt** | **String** | Output only. The time at which the environment group was last updated as milliseconds since epoch. | [optional] [readonly] 
**name** | **String** | ID of the environment group. | [optional] 
**state** | **String** | Output only. State of the environment group. Values other than ACTIVE means the resource is not ready to use. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DELETING` (value: `"DELETING"`)

* `UPDATING` (value: `"UPDATING"`)




