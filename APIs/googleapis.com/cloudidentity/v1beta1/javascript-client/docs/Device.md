# CloudIdentityApi.Device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**androidSpecificAttributes** | [**AndroidAttributes**](AndroidAttributes.md) |  | [optional] 
**assetTag** | **String** | Asset tag of the device. | [optional] 
**basebandVersion** | **String** | Output only. Baseband version of the device. | [optional] [readonly] 
**bootloaderVersion** | **String** | Output only. Device bootloader version. Example: 0.6.7. | [optional] [readonly] 
**brand** | **String** | Output only. Device brand. Example: Samsung. | [optional] [readonly] 
**buildNumber** | **String** | Output only. Build number of the device. | [optional] [readonly] 
**clientTypes** | **[String]** | List of the clients the device is reporting to. | [optional] 
**compromisedState** | **String** | Output only. Represents whether the Device is compromised. | [optional] [readonly] 
**createTime** | **String** | Output only. When the Company-Owned device was imported. This field is empty for BYOD devices. | [optional] [readonly] 
**deviceId** | **String** | Unique identifier for the device. | [optional] 
**deviceType** | **String** | Output only. Type of device. | [optional] [readonly] 
**enabledDeveloperOptions** | **Boolean** | Output only. Whether developer options is enabled on device. | [optional] [readonly] 
**enabledUsbDebugging** | **Boolean** | Output only. Whether USB debugging is enabled on device. | [optional] [readonly] 
**encryptionState** | **String** | Output only. Device encryption state. | [optional] [readonly] 
**endpointVerificationSpecificAttributes** | [**EndpointVerificationSpecificAttributes**](EndpointVerificationSpecificAttributes.md) |  | [optional] 
**hostname** | **String** | Host name of the device. | [optional] 
**imei** | **String** | Output only. IMEI number of device if GSM device; empty otherwise. | [optional] [readonly] 
**kernelVersion** | **String** | Output only. Kernel version of the device. | [optional] [readonly] 
**lastSyncTime** | **String** | Most recent time when device synced with this service. | [optional] 
**managementState** | **String** | Output only. Management state of the device | [optional] [readonly] 
**manufacturer** | **String** | Output only. Device manufacturer. Example: Motorola. | [optional] [readonly] 
**meid** | **String** | Output only. MEID number of device if CDMA device; empty otherwise. | [optional] [readonly] 
**model** | **String** | Output only. Model name of device. Example: Pixel 3. | [optional] [readonly] 
**name** | **String** | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Device in format: &#x60;devices/{device_id}&#x60;, where device_id is the unique id assigned to the Device. | [optional] [readonly] 
**networkOperator** | **String** | Output only. Mobile or network operator of device, if available. | [optional] [readonly] 
**osVersion** | **String** | Output only. OS version of the device. Example: Android 8.1.0. | [optional] [readonly] 
**otherAccounts** | **[String]** | Output only. Domain name for Google accounts on device. Type for other accounts on device. On Android, will only be populated if |ownership_privilege| is |PROFILE_OWNER| or |DEVICE_OWNER|. Does not include the account signed in to the device policy app if that account&#39;s domain has only one account. Examples: \&quot;com.example\&quot;, \&quot;xyz.com\&quot;. | [optional] [readonly] 
**ownerType** | **String** | Output only. Whether the device is owned by the company or an individual | [optional] [readonly] 
**releaseVersion** | **String** | Output only. OS release version. Example: 6.0. | [optional] [readonly] 
**securityPatchTime** | **String** | Output only. OS security patch update time on device. | [optional] [readonly] 
**serialNumber** | **String** | Serial Number of device. Example: HT82V1A01076. | [optional] 
**wifiMacAddresses** | **[String]** | WiFi MAC addresses of device. | [optional] 



## Enum: [ClientTypesEnum]


* `CLIENT_TYPE_UNSPECIFIED` (value: `"CLIENT_TYPE_UNSPECIFIED"`)

* `DRIVE_FS` (value: `"DRIVE_FS"`)

* `FUNDAMENTAL` (value: `"FUNDAMENTAL"`)

* `ENDPOINT_VERIFICATION` (value: `"ENDPOINT_VERIFICATION"`)

* `WINDOWS_ADVANCED` (value: `"WINDOWS_ADVANCED"`)

* `GOOGLE_CREDENTIALS_PROVIDER_FOR_WINDOWS` (value: `"GOOGLE_CREDENTIALS_PROVIDER_FOR_WINDOWS"`)





## Enum: CompromisedStateEnum


* `COMPROMISED_STATE_UNSPECIFIED` (value: `"COMPROMISED_STATE_UNSPECIFIED"`)

* `COMPROMISED` (value: `"COMPROMISED"`)

* `UNCOMPROMISED` (value: `"UNCOMPROMISED"`)





## Enum: DeviceTypeEnum


* `DEVICE_TYPE_UNSPECIFIED` (value: `"DEVICE_TYPE_UNSPECIFIED"`)

* `ANDROID` (value: `"ANDROID"`)

* `IOS` (value: `"IOS"`)

* `GOOGLE_SYNC` (value: `"GOOGLE_SYNC"`)

* `WINDOWS` (value: `"WINDOWS"`)

* `MAC_OS` (value: `"MAC_OS"`)

* `LINUX` (value: `"LINUX"`)

* `CHROME_OS` (value: `"CHROME_OS"`)





## Enum: EncryptionStateEnum


* `ENCRYPTION_STATE_UNSPECIFIED` (value: `"ENCRYPTION_STATE_UNSPECIFIED"`)

* `UNSUPPORTED_BY_DEVICE` (value: `"UNSUPPORTED_BY_DEVICE"`)

* `ENCRYPTED` (value: `"ENCRYPTED"`)

* `NOT_ENCRYPTED` (value: `"NOT_ENCRYPTED"`)





## Enum: ManagementStateEnum


* `MANAGEMENT_STATE_UNSPECIFIED` (value: `"MANAGEMENT_STATE_UNSPECIFIED"`)

* `APPROVED` (value: `"APPROVED"`)

* `BLOCKED` (value: `"BLOCKED"`)

* `PENDING` (value: `"PENDING"`)

* `UNPROVISIONED` (value: `"UNPROVISIONED"`)

* `WIPING` (value: `"WIPING"`)

* `WIPED` (value: `"WIPED"`)





## Enum: OwnerTypeEnum


* `DEVICE_OWNERSHIP_UNSPECIFIED` (value: `"DEVICE_OWNERSHIP_UNSPECIFIED"`)

* `COMPANY` (value: `"COMPANY"`)

* `BYOD` (value: `"BYOD"`)




