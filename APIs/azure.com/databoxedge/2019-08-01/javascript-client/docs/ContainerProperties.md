# DataBoxEdgeManagementClient.ContainerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containerStatus** | **String** | Current status of the container. | [optional] [readonly] 
**createdDateTime** | **Date** | The UTC time when container got created. | [optional] [readonly] 
**dataFormat** | **String** | DataFormat for Container | 
**refreshDetails** | [**RefreshDetails**](RefreshDetails.md) |  | [optional] 



## Enum: ContainerStatusEnum


* `OK` (value: `"OK"`)

* `Offline` (value: `"Offline"`)

* `Unknown` (value: `"Unknown"`)

* `Updating` (value: `"Updating"`)

* `NeedsAttention` (value: `"NeedsAttention"`)





## Enum: DataFormatEnum


* `BlockBlob` (value: `"BlockBlob"`)

* `PageBlob` (value: `"PageBlob"`)

* `AzureFile` (value: `"AzureFile"`)




