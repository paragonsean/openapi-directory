# ComputeManagementClient.MaintenanceRedeployStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isCustomerInitiatedMaintenanceAllowed** | **Boolean** | True, if customer is allowed to perform Maintenance. | [optional] 
**lastOperationMessage** | **String** | Message returned for the last Maintenance Operation. | [optional] 
**lastOperationResultCode** | **String** | The Last Maintenance Operation Result Code. | [optional] 
**maintenanceWindowEndTime** | **Date** | End Time for the Maintenance Window. | [optional] 
**maintenanceWindowStartTime** | **Date** | Start Time for the Maintenance Window. | [optional] 
**preMaintenanceWindowEndTime** | **Date** | End Time for the Pre Maintenance Window. | [optional] 
**preMaintenanceWindowStartTime** | **Date** | Start Time for the Pre Maintenance Window. | [optional] 



## Enum: LastOperationResultCodeEnum


* `None` (value: `"None"`)

* `RetryLater` (value: `"RetryLater"`)

* `MaintenanceAborted` (value: `"MaintenanceAborted"`)

* `MaintenanceCompleted` (value: `"MaintenanceCompleted"`)




