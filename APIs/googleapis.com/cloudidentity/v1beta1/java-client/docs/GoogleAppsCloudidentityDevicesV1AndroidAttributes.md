

# GoogleAppsCloudidentityDevicesV1AndroidAttributes

Resource representing the Android specific attributes of a Device.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ctsProfileMatch** | **Boolean** | Whether the device passes Android CTS compliance. |  [optional] |
|**enabledUnknownSources** | **Boolean** | Whether applications from unknown sources can be installed on device. |  [optional] |
|**hasPotentiallyHarmfulApps** | **Boolean** | Whether any potentially harmful apps were detected on the device. |  [optional] |
|**ownerProfileAccount** | **Boolean** | Whether this account is on an owner/primary profile. For phones, only true for owner profiles. Android 4+ devices can have secondary or restricted user profiles. |  [optional] |
|**ownershipPrivilege** | [**OwnershipPrivilegeEnum**](#OwnershipPrivilegeEnum) | Ownership privileges on device. |  [optional] |
|**supportsWorkProfile** | **Boolean** | Whether device supports Android work profiles. If false, this service will not block access to corp data even if an administrator turns on the \&quot;Enforce Work Profile\&quot; policy. |  [optional] |
|**verifiedBoot** | **Boolean** | Whether Android verified boot status is GREEN. |  [optional] |
|**verifyAppsEnabled** | **Boolean** | Whether Google Play Protect Verify Apps is enabled. |  [optional] |



## Enum: OwnershipPrivilegeEnum

| Name | Value |
|---- | -----|
| OWNERSHIP_PRIVILEGE_UNSPECIFIED | &quot;OWNERSHIP_PRIVILEGE_UNSPECIFIED&quot; |
| DEVICE_ADMINISTRATOR | &quot;DEVICE_ADMINISTRATOR&quot; |
| PROFILE_OWNER | &quot;PROFILE_OWNER&quot; |
| DEVICE_OWNER | &quot;DEVICE_OWNER&quot; |



