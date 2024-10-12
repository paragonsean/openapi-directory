# EventHubManagementClient.EventHubProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | Exact time the Event Hub was created. | [optional] [readonly] 
**messageRetentionInDays** | **Number** | Number of days to retain the events for this Event Hub. | [optional] 
**partitionCount** | **Number** | Number of partitions created for the Event Hub. | [optional] 
**partitionIds** | **[String]** | Current number of shards on the Event Hub. | [optional] [readonly] 
**status** | **String** | Enumerates the possible values for the status of the Event Hub. | [optional] 
**updatedAt** | **Date** | The exact time the message was updated. | [optional] [readonly] 



## Enum: StatusEnum


* `Active` (value: `"Active"`)

* `Disabled` (value: `"Disabled"`)

* `Restoring` (value: `"Restoring"`)

* `SendDisabled` (value: `"SendDisabled"`)

* `ReceiveDisabled` (value: `"ReceiveDisabled"`)

* `Creating` (value: `"Creating"`)

* `Deleting` (value: `"Deleting"`)

* `Renaming` (value: `"Renaming"`)

* `Unknown` (value: `"Unknown"`)




