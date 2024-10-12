# DataBoxManagementClient.DataBoxDiskCopyProgress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytesCopied** | **Number** | Bytes copied during the copy of disk. | [optional] [readonly] 
**percentComplete** | **Number** | Indicates the percentage completed for the copy of the disk. | [optional] [readonly] 
**serialNumber** | **String** | The serial number of the disk | [optional] [readonly] 
**status** | **String** | The Status of the copy | [optional] [readonly] 



## Enum: StatusEnum


* `NotStarted` (value: `"NotStarted"`)

* `InProgress` (value: `"InProgress"`)

* `Completed` (value: `"Completed"`)

* `CompletedWithErrors` (value: `"CompletedWithErrors"`)

* `Failed` (value: `"Failed"`)

* `NotReturned` (value: `"NotReturned"`)




