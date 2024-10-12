# NetworkConnectivityApi.Group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time the group was created. | [optional] [readonly] 
**description** | **String** | Optional. The description of the group. | [optional] 
**labels** | **{String: String}** | Optional. Labels in key-value pair format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements). | [optional] 
**name** | **String** | Immutable. The name of the group. Group names must be unique. They use the following form: &#x60;projects/{project_number}/locations/global/hubs/{hub}/groups/{group_id}&#x60; | [optional] 
**state** | **String** | Output only. The current lifecycle state of this group. | [optional] [readonly] 
**uid** | **String** | Output only. The Google-generated UUID for the group. This value is unique across all group resources. If a group is deleted and another with the same name is created, the new route table is assigned a different unique_id. | [optional] [readonly] 
**updateTime** | **String** | Output only. The time the group was last updated. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DELETING` (value: `"DELETING"`)

* `ACCEPTING` (value: `"ACCEPTING"`)

* `REJECTING` (value: `"REJECTING"`)

* `UPDATING` (value: `"UPDATING"`)

* `INACTIVE` (value: `"INACTIVE"`)

* `OBSOLETE` (value: `"OBSOLETE"`)




