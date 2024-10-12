

# Notification

A notification of one event relating to an enterprise.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appRestrictionsSchemaChangeEvent** | [**AppRestrictionsSchemaChangeEvent**](AppRestrictionsSchemaChangeEvent.md) |  |  [optional] |
|**appUpdateEvent** | [**AppUpdateEvent**](AppUpdateEvent.md) |  |  [optional] |
|**deviceReportUpdateEvent** | [**DeviceReportUpdateEvent**](DeviceReportUpdateEvent.md) |  |  [optional] |
|**enterpriseId** | **String** | The ID of the enterprise for which the notification is sent. This will always be present. |  [optional] |
|**installFailureEvent** | [**InstallFailureEvent**](InstallFailureEvent.md) |  |  [optional] |
|**newDeviceEvent** | [**NewDeviceEvent**](NewDeviceEvent.md) |  |  [optional] |
|**newPermissionsEvent** | [**NewPermissionsEvent**](NewPermissionsEvent.md) |  |  [optional] |
|**notificationType** | [**NotificationTypeEnum**](#NotificationTypeEnum) | Type of the notification. |  [optional] |
|**productApprovalEvent** | [**ProductApprovalEvent**](ProductApprovalEvent.md) |  |  [optional] |
|**productAvailabilityChangeEvent** | [**ProductAvailabilityChangeEvent**](ProductAvailabilityChangeEvent.md) |  |  [optional] |
|**timestampMillis** | **String** | The time when the notification was published in milliseconds since 1970-01-01T00:00:00Z. This will always be present. |  [optional] |



## Enum: NotificationTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| TEST_NOTIFICATION | &quot;testNotification&quot; |
| PRODUCT_APPROVAL | &quot;productApproval&quot; |
| INSTALL_FAILURE | &quot;installFailure&quot; |
| APP_UPDATE | &quot;appUpdate&quot; |
| NEW_PERMISSIONS | &quot;newPermissions&quot; |
| APP_RESTRICIONS_SCHEMA_CHANGE | &quot;appRestricionsSchemaChange&quot; |
| PRODUCT_AVAILABILITY_CHANGE | &quot;productAvailabilityChange&quot; |
| NEW_DEVICE | &quot;newDevice&quot; |
| DEVICE_REPORT_UPDATE | &quot;deviceReportUpdate&quot; |



