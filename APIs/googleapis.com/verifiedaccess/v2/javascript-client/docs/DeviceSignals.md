# ChromeVerifiedAccessApi.DeviceSignals

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowScreenLock** | **Boolean** | Value of the AllowScreenLock policy on the device. See https://chromeenterprise.google/policies/?policy&#x3D;AllowScreenLock for more details. Available on ChromeOS only. | [optional] 
**browserVersion** | **String** | Current version of the Chrome browser which generated this set of signals. Example value: \&quot;107.0.5286.0\&quot;. | [optional] 
**builtInDnsClientEnabled** | **Boolean** | Whether Chrome&#39;s built-in DNS client is used. The OS DNS client is otherwise used. This value may be controlled by an enterprise policy: https://chromeenterprise.google/policies/#BuiltInDnsClientEnabled. | [optional] 
**chromeRemoteDesktopAppBlocked** | **Boolean** | Whether access to the Chrome Remote Desktop application is blocked via a policy. | [optional] 
**crowdStrikeAgent** | [**CrowdStrikeAgent**](CrowdStrikeAgent.md) |  | [optional] 
**deviceAffiliationIds** | **[String]** | Affiliation IDs of the organizations that are affiliated with the organization that is currently managing the device. When the sets of device and profile affiliation IDs overlap, it means that the organizations managing the device and user are affiliated. To learn more about user affiliation, visit https://support.google.com/chrome/a/answer/12801245?ref_topic&#x3D;9027936. | [optional] 
**deviceEnrollmentDomain** | **String** | Enrollment domain of the customer which is currently managing the device. | [optional] 
**deviceManufacturer** | **String** | The name of the device&#39;s manufacturer. | [optional] 
**deviceModel** | **String** | The name of the device&#39;s model. | [optional] 
**diskEncryption** | **String** | The encryption state of the disk. On ChromeOS, the main disk is always ENCRYPTED. | [optional] 
**displayName** | **String** | The display name of the device, as defined by the user. | [optional] 
**hostname** | **String** | Hostname of the device. | [optional] 
**imei** | **[String]** | International Mobile Equipment Identity (IMEI) of the device. Available on ChromeOS only. | [optional] 
**macAddresses** | **[String]** | MAC addresses of the device. | [optional] 
**meid** | **[String]** | Mobile Equipment Identifier (MEID) of the device. Available on ChromeOS only. | [optional] 
**operatingSystem** | **String** | The type of the Operating System currently running on the device. | [optional] 
**osFirewall** | **String** | The state of the OS level firewall. On ChromeOS, the value will always be ENABLED on regular devices and UNKNOWN on devices in developer mode. | [optional] 
**osVersion** | **String** | The current version of the Operating System. On Windows and linux, the value will also include the security patch information. | [optional] 
**passwordProtectionWarningTrigger** | **String** | Whether the Password Protection Warning feature is enabled or not. Password protection alerts users when they reuse their protected password on potentially suspicious sites. This setting is controlled by an enterprise policy: https://chromeenterprise.google/policies/#PasswordProtectionWarningTrigger. Note that the policy unset does not have the same effects as having the policy explicitly set to &#x60;PASSWORD_PROTECTION_OFF&#x60;. | [optional] 
**profileAffiliationIds** | **[String]** | Affiliation IDs of the organizations that are affiliated with the organization that is currently managing the Chrome Profile’s user or ChromeOS user. | [optional] 
**realtimeUrlCheckMode** | **String** | Whether Enterprise-grade (i.e. custom) unsafe URL scanning is enabled or not. This setting may be controlled by an enterprise policy: https://chromeenterprise.google/policies/#EnterpriseRealTimeUrlCheckMode | [optional] 
**safeBrowsingProtectionLevel** | **String** | Safe Browsing Protection Level. That setting may be controlled by an enterprise policy: https://chromeenterprise.google/policies/#SafeBrowsingProtectionLevel. | [optional] 
**screenLockSecured** | **String** | The state of the Screen Lock password protection. On ChromeOS, this value will always be ENABLED as there is not way to disable requiring a password or pin when unlocking the device. | [optional] 
**secureBootMode** | **String** | Whether the device&#39;s startup software has its Secure Boot feature enabled. Available on Windows only. | [optional] 
**serialNumber** | **String** | The serial number of the device. On Windows, this represents the BIOS&#39;s serial number. Not available on most Linux distributions. | [optional] 
**siteIsolationEnabled** | **Boolean** | Whether the Site Isolation (a.k.a Site Per Process) setting is enabled. That setting may be controlled by an enterprise policy: https://chromeenterprise.google/policies/#SitePerProcess | [optional] 
**systemDnsServers** | **[String]** | List of the addesses of all OS level DNS servers configured in the device&#39;s network settings. | [optional] 
**thirdPartyBlockingEnabled** | **Boolean** | Whether Chrome is blocking third-party software injection or not. This setting may be controlled by an enterprise policy: https://chromeenterprise.google/policies/?policy&#x3D;ThirdPartyBlockingEnabled. Available on Windows only. | [optional] 
**trigger** | **String** | The trigger which generated this set of signals. | [optional] 
**windowsMachineDomain** | **String** | Windows domain that the current machine has joined. Available on Windows only. | [optional] 
**windowsUserDomain** | **String** | Windows domain for the current OS user. Available on Windows only. | [optional] 



## Enum: DiskEncryptionEnum


* `UNSPECIFIED` (value: `"DISK_ENCRYPTION_UNSPECIFIED"`)

* `UNKNOWN` (value: `"DISK_ENCRYPTION_UNKNOWN"`)

* `DISABLED` (value: `"DISK_ENCRYPTION_DISABLED"`)

* `ENCRYPTED` (value: `"DISK_ENCRYPTION_ENCRYPTED"`)





## Enum: OperatingSystemEnum


* `OPERATING_SYSTEM_UNSPECIFIED` (value: `"OPERATING_SYSTEM_UNSPECIFIED"`)

* `CHROME_OS` (value: `"CHROME_OS"`)

* `CHROMIUM_OS` (value: `"CHROMIUM_OS"`)

* `WINDOWS` (value: `"WINDOWS"`)

* `MAC_OS_X` (value: `"MAC_OS_X"`)

* `LINUX` (value: `"LINUX"`)





## Enum: OsFirewallEnum


* `UNSPECIFIED` (value: `"OS_FIREWALL_UNSPECIFIED"`)

* `UNKNOWN` (value: `"OS_FIREWALL_UNKNOWN"`)

* `DISABLED` (value: `"OS_FIREWALL_DISABLED"`)

* `ENABLED` (value: `"OS_FIREWALL_ENABLED"`)





## Enum: PasswordProtectionWarningTriggerEnum


* `PASSWORD_PROTECTION_WARNING_TRIGGER_UNSPECIFIED` (value: `"PASSWORD_PROTECTION_WARNING_TRIGGER_UNSPECIFIED"`)

* `POLICY_UNSET` (value: `"POLICY_UNSET"`)

* `PASSWORD_PROTECTION_OFF` (value: `"PASSWORD_PROTECTION_OFF"`)

* `PASSWORD_REUSE` (value: `"PASSWORD_REUSE"`)

* `PHISHING_REUSE` (value: `"PHISHING_REUSE"`)





## Enum: RealtimeUrlCheckModeEnum


* `UNSPECIFIED` (value: `"REALTIME_URL_CHECK_MODE_UNSPECIFIED"`)

* `DISABLED` (value: `"REALTIME_URL_CHECK_MODE_DISABLED"`)

* `ENABLED_MAIN_FRAME` (value: `"REALTIME_URL_CHECK_MODE_ENABLED_MAIN_FRAME"`)





## Enum: SafeBrowsingProtectionLevelEnum


* `SAFE_BROWSING_PROTECTION_LEVEL_UNSPECIFIED` (value: `"SAFE_BROWSING_PROTECTION_LEVEL_UNSPECIFIED"`)

* `INACTIVE` (value: `"INACTIVE"`)

* `STANDARD` (value: `"STANDARD"`)

* `ENHANCED` (value: `"ENHANCED"`)





## Enum: ScreenLockSecuredEnum


* `UNSPECIFIED` (value: `"SCREEN_LOCK_SECURED_UNSPECIFIED"`)

* `UNKNOWN` (value: `"SCREEN_LOCK_SECURED_UNKNOWN"`)

* `DISABLED` (value: `"SCREEN_LOCK_SECURED_DISABLED"`)

* `ENABLED` (value: `"SCREEN_LOCK_SECURED_ENABLED"`)





## Enum: SecureBootModeEnum


* `UNSPECIFIED` (value: `"SECURE_BOOT_MODE_UNSPECIFIED"`)

* `UNKNOWN` (value: `"SECURE_BOOT_MODE_UNKNOWN"`)

* `DISABLED` (value: `"SECURE_BOOT_MODE_DISABLED"`)

* `ENABLED` (value: `"SECURE_BOOT_MODE_ENABLED"`)





## Enum: TriggerEnum


* `UNSPECIFIED` (value: `"TRIGGER_UNSPECIFIED"`)

* `BROWSER_NAVIGATION` (value: `"TRIGGER_BROWSER_NAVIGATION"`)

* `LOGIN_SCREEN` (value: `"TRIGGER_LOGIN_SCREEN"`)




