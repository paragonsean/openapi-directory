# GooglePlayEmmApi.Notification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appRestrictionsSchemaChangeEvent** | [**AppRestrictionsSchemaChangeEvent**](AppRestrictionsSchemaChangeEvent.md) |  | [optional] 
**appUpdateEvent** | [**AppUpdateEvent**](AppUpdateEvent.md) |  | [optional] 
**deviceReportUpdateEvent** | [**DeviceReportUpdateEvent**](DeviceReportUpdateEvent.md) |  | [optional] 
**enterpriseId** | **String** | The ID of the enterprise for which the notification is sent. This will always be present. | [optional] 
**installFailureEvent** | [**InstallFailureEvent**](InstallFailureEvent.md) |  | [optional] 
**newDeviceEvent** | [**NewDeviceEvent**](NewDeviceEvent.md) |  | [optional] 
**newPermissionsEvent** | [**NewPermissionsEvent**](NewPermissionsEvent.md) |  | [optional] 
**notificationType** | **String** | Type of the notification. | [optional] 
**productApprovalEvent** | [**ProductApprovalEvent**](ProductApprovalEvent.md) |  | [optional] 
**productAvailabilityChangeEvent** | [**ProductAvailabilityChangeEvent**](ProductAvailabilityChangeEvent.md) |  | [optional] 
**timestampMillis** | **String** | The time when the notification was published in milliseconds since 1970-01-01T00:00:00Z. This will always be present. | [optional] 



## Enum: NotificationTypeEnum


* `unknown` (value: `"unknown"`)

* `testNotification` (value: `"testNotification"`)

* `productApproval` (value: `"productApproval"`)

* `installFailure` (value: `"installFailure"`)

* `appUpdate` (value: `"appUpdate"`)

* `newPermissions` (value: `"newPermissions"`)

* `appRestricionsSchemaChange` (value: `"appRestricionsSchemaChange"`)

* `productAvailabilityChange` (value: `"productAvailabilityChange"`)

* `newDevice` (value: `"newDevice"`)

* `deviceReportUpdate` (value: `"deviceReportUpdate"`)




