

# Device

A Device within the Cloud Identity Devices API. Represents a Device known to Google Cloud, independent of the device ownership, type, and whether it is assigned or in use by a user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**androidSpecificAttributes** | [**AndroidAttributes**](AndroidAttributes.md) |  |  [optional] |
|**assetTag** | **String** | Asset tag of the device. |  [optional] |
|**basebandVersion** | **String** | Output only. Baseband version of the device. |  [optional] [readonly] |
|**bootloaderVersion** | **String** | Output only. Device bootloader version. Example: 0.6.7. |  [optional] [readonly] |
|**brand** | **String** | Output only. Device brand. Example: Samsung. |  [optional] [readonly] |
|**buildNumber** | **String** | Output only. Build number of the device. |  [optional] [readonly] |
|**clientTypes** | [**List&lt;ClientTypesEnum&gt;**](#List&lt;ClientTypesEnum&gt;) | List of the clients the device is reporting to. |  [optional] |
|**compromisedState** | [**CompromisedStateEnum**](#CompromisedStateEnum) | Output only. Represents whether the Device is compromised. |  [optional] [readonly] |
|**createTime** | **String** | Output only. When the Company-Owned device was imported. This field is empty for BYOD devices. |  [optional] [readonly] |
|**deviceId** | **String** | Unique identifier for the device. |  [optional] |
|**deviceType** | [**DeviceTypeEnum**](#DeviceTypeEnum) | Output only. Type of device. |  [optional] [readonly] |
|**enabledDeveloperOptions** | **Boolean** | Output only. Whether developer options is enabled on device. |  [optional] [readonly] |
|**enabledUsbDebugging** | **Boolean** | Output only. Whether USB debugging is enabled on device. |  [optional] [readonly] |
|**encryptionState** | [**EncryptionStateEnum**](#EncryptionStateEnum) | Output only. Device encryption state. |  [optional] [readonly] |
|**endpointVerificationSpecificAttributes** | [**EndpointVerificationSpecificAttributes**](EndpointVerificationSpecificAttributes.md) |  |  [optional] |
|**hostname** | **String** | Host name of the device. |  [optional] |
|**imei** | **String** | Output only. IMEI number of device if GSM device; empty otherwise. |  [optional] [readonly] |
|**kernelVersion** | **String** | Output only. Kernel version of the device. |  [optional] [readonly] |
|**lastSyncTime** | **String** | Most recent time when device synced with this service. |  [optional] |
|**managementState** | [**ManagementStateEnum**](#ManagementStateEnum) | Output only. Management state of the device |  [optional] [readonly] |
|**manufacturer** | **String** | Output only. Device manufacturer. Example: Motorola. |  [optional] [readonly] |
|**meid** | **String** | Output only. MEID number of device if CDMA device; empty otherwise. |  [optional] [readonly] |
|**model** | **String** | Output only. Model name of device. Example: Pixel 3. |  [optional] [readonly] |
|**name** | **String** | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Device in format: &#x60;devices/{device_id}&#x60;, where device_id is the unique id assigned to the Device. |  [optional] [readonly] |
|**networkOperator** | **String** | Output only. Mobile or network operator of device, if available. |  [optional] [readonly] |
|**osVersion** | **String** | Output only. OS version of the device. Example: Android 8.1.0. |  [optional] [readonly] |
|**otherAccounts** | **List&lt;String&gt;** | Output only. Domain name for Google accounts on device. Type for other accounts on device. On Android, will only be populated if |ownership_privilege| is |PROFILE_OWNER| or |DEVICE_OWNER|. Does not include the account signed in to the device policy app if that account&#39;s domain has only one account. Examples: \&quot;com.example\&quot;, \&quot;xyz.com\&quot;. |  [optional] [readonly] |
|**ownerType** | [**OwnerTypeEnum**](#OwnerTypeEnum) | Output only. Whether the device is owned by the company or an individual |  [optional] [readonly] |
|**releaseVersion** | **String** | Output only. OS release version. Example: 6.0. |  [optional] [readonly] |
|**securityPatchTime** | **String** | Output only. OS security patch update time on device. |  [optional] [readonly] |
|**serialNumber** | **String** | Serial Number of device. Example: HT82V1A01076. |  [optional] |
|**wifiMacAddresses** | **List&lt;String&gt;** | WiFi MAC addresses of device. |  [optional] |



## Enum: List&lt;ClientTypesEnum&gt;

| Name | Value |
|---- | -----|
| CLIENT_TYPE_UNSPECIFIED | &quot;CLIENT_TYPE_UNSPECIFIED&quot; |
| DRIVE_FS | &quot;DRIVE_FS&quot; |
| FUNDAMENTAL | &quot;FUNDAMENTAL&quot; |
| ENDPOINT_VERIFICATION | &quot;ENDPOINT_VERIFICATION&quot; |
| WINDOWS_ADVANCED | &quot;WINDOWS_ADVANCED&quot; |
| GOOGLE_CREDENTIALS_PROVIDER_FOR_WINDOWS | &quot;GOOGLE_CREDENTIALS_PROVIDER_FOR_WINDOWS&quot; |



## Enum: CompromisedStateEnum

| Name | Value |
|---- | -----|
| COMPROMISED_STATE_UNSPECIFIED | &quot;COMPROMISED_STATE_UNSPECIFIED&quot; |
| COMPROMISED | &quot;COMPROMISED&quot; |
| UNCOMPROMISED | &quot;UNCOMPROMISED&quot; |



## Enum: DeviceTypeEnum

| Name | Value |
|---- | -----|
| DEVICE_TYPE_UNSPECIFIED | &quot;DEVICE_TYPE_UNSPECIFIED&quot; |
| ANDROID | &quot;ANDROID&quot; |
| IOS | &quot;IOS&quot; |
| GOOGLE_SYNC | &quot;GOOGLE_SYNC&quot; |
| WINDOWS | &quot;WINDOWS&quot; |
| MAC_OS | &quot;MAC_OS&quot; |
| LINUX | &quot;LINUX&quot; |
| CHROME_OS | &quot;CHROME_OS&quot; |



## Enum: EncryptionStateEnum

| Name | Value |
|---- | -----|
| ENCRYPTION_STATE_UNSPECIFIED | &quot;ENCRYPTION_STATE_UNSPECIFIED&quot; |
| UNSUPPORTED_BY_DEVICE | &quot;UNSUPPORTED_BY_DEVICE&quot; |
| ENCRYPTED | &quot;ENCRYPTED&quot; |
| NOT_ENCRYPTED | &quot;NOT_ENCRYPTED&quot; |



## Enum: ManagementStateEnum

| Name | Value |
|---- | -----|
| MANAGEMENT_STATE_UNSPECIFIED | &quot;MANAGEMENT_STATE_UNSPECIFIED&quot; |
| APPROVED | &quot;APPROVED&quot; |
| BLOCKED | &quot;BLOCKED&quot; |
| PENDING | &quot;PENDING&quot; |
| UNPROVISIONED | &quot;UNPROVISIONED&quot; |
| WIPING | &quot;WIPING&quot; |
| WIPED | &quot;WIPED&quot; |



## Enum: OwnerTypeEnum

| Name | Value |
|---- | -----|
| DEVICE_OWNERSHIP_UNSPECIFIED | &quot;DEVICE_OWNERSHIP_UNSPECIFIED&quot; |
| COMPANY | &quot;COMPANY&quot; |
| BYOD | &quot;BYOD&quot; |



