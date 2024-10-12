

# MaintenanceRedeployStatus

Maintenance Operation Status.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isCustomerInitiatedMaintenanceAllowed** | **Boolean** | True, if customer is allowed to perform Maintenance. |  [optional] |
|**lastOperationMessage** | **String** | Message returned for the last Maintenance Operation. |  [optional] |
|**lastOperationResultCode** | [**LastOperationResultCodeEnum**](#LastOperationResultCodeEnum) | The Last Maintenance Operation Result Code. |  [optional] |
|**maintenanceWindowEndTime** | **OffsetDateTime** | End Time for the Maintenance Window. |  [optional] |
|**maintenanceWindowStartTime** | **OffsetDateTime** | Start Time for the Maintenance Window. |  [optional] |
|**preMaintenanceWindowEndTime** | **OffsetDateTime** | End Time for the Pre Maintenance Window. |  [optional] |
|**preMaintenanceWindowStartTime** | **OffsetDateTime** | Start Time for the Pre Maintenance Window. |  [optional] |



## Enum: LastOperationResultCodeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| RETRY_LATER | &quot;RetryLater&quot; |
| MAINTENANCE_ABORTED | &quot;MaintenanceAborted&quot; |
| MAINTENANCE_COMPLETED | &quot;MaintenanceCompleted&quot; |



