# AndroidDeviceProvisioningPartnerApi.DevicesLongRunningOperationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devicesCount** | **Number** | The number of metadata updates in the operation. This might be different from the number of updates in the request if the API can&#39;t parse some of the updates. | [optional] 
**processingStatus** | **String** | The processing status of the operation. | [optional] 
**progress** | **Number** | The processing progress of the operation. Measured as a number from 0 to 100. A value of 10O doesn&#39;t always mean the operation completed—check for the inclusion of a &#x60;done&#x60; field. | [optional] 



## Enum: ProcessingStatusEnum


* `STATUS_UNSPECIFIED` (value: `"BATCH_PROCESS_STATUS_UNSPECIFIED"`)

* `PENDING` (value: `"BATCH_PROCESS_PENDING"`)

* `IN_PROGRESS` (value: `"BATCH_PROCESS_IN_PROGRESS"`)

* `PROCESSED` (value: `"BATCH_PROCESS_PROCESSED"`)




