# AzureMigrateV2.GroupProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**areAssessmentsRunning** | **Boolean** | If the assessments are in running state. | [optional] [readonly] 
**assessments** | **[String]** | List of References to Assessments created on this group. | [optional] [readonly] 
**createdTimestamp** | **Date** | Time when this group was created. Date-Time represented in ISO-8601 format. | [optional] [readonly] 
**groupStatus** | **String** | Whether the group has been created and is valid. | [optional] [readonly] 
**machineCount** | **Number** | Number of machines part of this group. | [optional] [readonly] 
**updatedTimestamp** | **Date** | Time when this group was last updated. Date-Time represented in ISO-8601 format. | [optional] [readonly] 



## Enum: GroupStatusEnum


* `Created` (value: `"Created"`)

* `Updated` (value: `"Updated"`)

* `Running` (value: `"Running"`)

* `Completed` (value: `"Completed"`)

* `Invalid` (value: `"Invalid"`)




