# DataBoxManagementClient.JobProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellationReason** | **String** | Reason for cancellation. | [optional] [readonly] 
**details** | [**JobDetails**](JobDetails.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**isCancellable** | **Boolean** | Describes whether the job is cancellable or not. | [optional] [readonly] 
**isDeletable** | **Boolean** | Describes whether the job is deletable or not. | [optional] [readonly] 
**isShippingAddressEditable** | **Boolean** | Describes whether the shipping address is editable or not. | [optional] [readonly] 
**startTime** | **Date** | Time at which the job was started in UTC ISO 8601 format. | [optional] [readonly] 
**status** | **String** | Name of the stage which is in progress. | [optional] [readonly] 



## Enum: StatusEnum


* `DeviceOrdered` (value: `"DeviceOrdered"`)

* `DevicePrepared` (value: `"DevicePrepared"`)

* `Dispatched` (value: `"Dispatched"`)

* `Delivered` (value: `"Delivered"`)

* `PickedUp` (value: `"PickedUp"`)

* `AtAzureDC` (value: `"AtAzureDC"`)

* `DataCopy` (value: `"DataCopy"`)

* `Completed` (value: `"Completed"`)

* `CompletedWithErrors` (value: `"CompletedWithErrors"`)

* `Cancelled` (value: `"Cancelled"`)

* `Failed_IssueReportedAtCustomer` (value: `"Failed_IssueReportedAtCustomer"`)

* `Failed_IssueDetectedAtAzureDC` (value: `"Failed_IssueDetectedAtAzureDC"`)

* `Aborted` (value: `"Aborted"`)




