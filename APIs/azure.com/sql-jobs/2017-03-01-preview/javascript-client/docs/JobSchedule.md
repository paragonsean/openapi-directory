# SqlManagementClient.JobSchedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **Boolean** | Whether or not the schedule is enabled. | [optional] 
**endTime** | **Date** | Schedule end time. | [optional] 
**interval** | **String** | Value of the schedule&#39;s recurring interval, if the schedule type is recurring. ISO8601 duration format. | [optional] 
**startTime** | **Date** | Schedule start time. | [optional] 
**type** | **String** | Schedule interval type | [optional] [default to &#39;Once&#39;]



## Enum: TypeEnum


* `Once` (value: `"Once"`)

* `Recurring` (value: `"Recurring"`)




