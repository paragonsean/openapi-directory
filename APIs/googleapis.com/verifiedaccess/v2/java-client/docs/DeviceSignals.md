

# DeviceSignals

The device signals as reported by Chrome. Unless otherwise specified, signals are available on all platforms.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowScreenLock** | **Boolean** | Value of the AllowScreenLock policy on the device. See https://chromeenterprise.google/policies/?policy&#x3D;AllowScreenLock for more details. Available on ChromeOS only. |  [optional] |
|**browserVersion** | **String** | Current version of the Chrome browser which generated this set of signals. Example value: \&quot;107.0.5286.0\&quot;. |  [optional] |
|**builtInDnsClientEnabled** | **Boolean** | Whether Chrome&#39;s built-in DNS client is used. The OS DNS client is otherwise used. This value may be controlled by an enterprise policy: https://chromeenterprise.google/policies/#BuiltInDnsClientEnabled. |  [optional] |
|**chromeRemoteDesktopAppBlocked** | **Boolean** | Whether access to the Chrome Remote Desktop application is blocked via a policy. |  [optional] |
|**crowdStrikeAgent** | [**CrowdStrikeAgent**](CrowdStrikeAgent.md) |  |  [optional] |
|**deviceAffiliationIds** | **List&lt;String&gt;** | Affiliation IDs of the organizations that are affiliated with the organization that is currently managing the device. When the sets of device and profile affiliation IDs overlap, it means that the organizations managing the device and user are affiliated. To learn more about user affiliation, visit https://support.google.com/chrome/a/answer/12801245?ref_topic&#x3D;9027936. |  [optional] |
|**deviceEnrollmentDomain** | **String** | Enrollment domain of the customer which is currently managing the device. |  [optional] |
|**deviceManufacturer** | **String** | The name of the device&#39;s manufacturer. |  [optional] |
|**deviceModel** | **String** | The name of the device&#39;s model. |  [optional] |
|**diskEncryption** | [**DiskEncryptionEnum**](#DiskEncryptionEnum) | The encryption state of the disk. On ChromeOS, the main disk is always ENCRYPTED. |  [optional] |
|**displayName** | **String** | The display name of the device, as defined by the user. |  [optional] |
|**hostname** | **String** | Hostname of the device. |  [optional] |
|**imei** | **List&lt;String&gt;** | International Mobile Equipment Identity (IMEI) of the device. Available on ChromeOS only. |  [optional] |
|**macAddresses** | **List&lt;String&gt;** | MAC addresses of the device. |  [optional] |
|**meid** | **List&lt;String&gt;** | Mobile Equipment Identifier (MEID) of the device. Available on ChromeOS only. |  [optional] |
|**operatingSystem** | [**OperatingSystemEnum**](#OperatingSystemEnum) | The type of the Operating System currently running on the device. |  [optional] |
|**osFirewall** | [**OsFirewallEnum**](#OsFirewallEnum) | The state of the OS level firewall. On ChromeOS, the value will always be ENABLED on regular devices and UNKNOWN on devices in developer mode. |  [optional] |
|**osVersion** | **String** | The current version of the Operating System. On Windows and linux, the value will also include the security patch information. |  [optional] |
|**passwordProtectionWarningTrigger** | [**PasswordProtectionWarningTriggerEnum**](#PasswordProtectionWarningTriggerEnum) | Whether the Password Protection Warning feature is enabled or not. Password protection alerts users when they reuse their protected password on potentially suspicious sites. This setting is controlled by an enterprise policy: https://chromeenterprise.google/policies/#PasswordProtectionWarningTrigger. Note that the policy unset does not have the same effects as having the policy explicitly set to &#x60;PASSWORD_PROTECTION_OFF&#x60;. |  [optional] |
|**profileAffiliationIds** | **List&lt;String&gt;** | Affiliation IDs of the organizations that are affiliated with the organization that is currently managing the Chrome Profile’s user or ChromeOS user. |  [optional] |
|**realtimeUrlCheckMode** | [**RealtimeUrlCheckModeEnum**](#RealtimeUrlCheckModeEnum) | Whether Enterprise-grade (i.e. custom) unsafe URL scanning is enabled or not. This setting may be controlled by an enterprise policy: https://chromeenterprise.google/policies/#EnterpriseRealTimeUrlCheckMode |  [optional] |
|**safeBrowsingProtectionLevel** | [**SafeBrowsingProtectionLevelEnum**](#SafeBrowsingProtectionLevelEnum) | Safe Browsing Protection Level. That setting may be controlled by an enterprise policy: https://chromeenterprise.google/policies/#SafeBrowsingProtectionLevel. |  [optional] |
|**screenLockSecured** | [**ScreenLockSecuredEnum**](#ScreenLockSecuredEnum) | The state of the Screen Lock password protection. On ChromeOS, this value will always be ENABLED as there is not way to disable requiring a password or pin when unlocking the device. |  [optional] |
|**secureBootMode** | [**SecureBootModeEnum**](#SecureBootModeEnum) | Whether the device&#39;s startup software has its Secure Boot feature enabled. Available on Windows only. |  [optional] |
|**serialNumber** | **String** | The serial number of the device. On Windows, this represents the BIOS&#39;s serial number. Not available on most Linux distributions. |  [optional] |
|**siteIsolationEnabled** | **Boolean** | Whether the Site Isolation (a.k.a Site Per Process) setting is enabled. That setting may be controlled by an enterprise policy: https://chromeenterprise.google/policies/#SitePerProcess |  [optional] |
|**systemDnsServers** | **List&lt;String&gt;** | List of the addesses of all OS level DNS servers configured in the device&#39;s network settings. |  [optional] |
|**thirdPartyBlockingEnabled** | **Boolean** | Whether Chrome is blocking third-party software injection or not. This setting may be controlled by an enterprise policy: https://chromeenterprise.google/policies/?policy&#x3D;ThirdPartyBlockingEnabled. Available on Windows only. |  [optional] |
|**trigger** | [**TriggerEnum**](#TriggerEnum) | The trigger which generated this set of signals. |  [optional] |
|**windowsMachineDomain** | **String** | Windows domain that the current machine has joined. Available on Windows only. |  [optional] |
|**windowsUserDomain** | **String** | Windows domain for the current OS user. Available on Windows only. |  [optional] |



## Enum: DiskEncryptionEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;DISK_ENCRYPTION_UNSPECIFIED&quot; |
| UNKNOWN | &quot;DISK_ENCRYPTION_UNKNOWN&quot; |
| DISABLED | &quot;DISK_ENCRYPTION_DISABLED&quot; |
| ENCRYPTED | &quot;DISK_ENCRYPTION_ENCRYPTED&quot; |



## Enum: OperatingSystemEnum

| Name | Value |
|---- | -----|
| OPERATING_SYSTEM_UNSPECIFIED | &quot;OPERATING_SYSTEM_UNSPECIFIED&quot; |
| CHROME_OS | &quot;CHROME_OS&quot; |
| CHROMIUM_OS | &quot;CHROMIUM_OS&quot; |
| WINDOWS | &quot;WINDOWS&quot; |
| MAC_OS_X | &quot;MAC_OS_X&quot; |
| LINUX | &quot;LINUX&quot; |



## Enum: OsFirewallEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;OS_FIREWALL_UNSPECIFIED&quot; |
| UNKNOWN | &quot;OS_FIREWALL_UNKNOWN&quot; |
| DISABLED | &quot;OS_FIREWALL_DISABLED&quot; |
| ENABLED | &quot;OS_FIREWALL_ENABLED&quot; |



## Enum: PasswordProtectionWarningTriggerEnum

| Name | Value |
|---- | -----|
| PASSWORD_PROTECTION_WARNING_TRIGGER_UNSPECIFIED | &quot;PASSWORD_PROTECTION_WARNING_TRIGGER_UNSPECIFIED&quot; |
| POLICY_UNSET | &quot;POLICY_UNSET&quot; |
| PASSWORD_PROTECTION_OFF | &quot;PASSWORD_PROTECTION_OFF&quot; |
| PASSWORD_REUSE | &quot;PASSWORD_REUSE&quot; |
| PHISHING_REUSE | &quot;PHISHING_REUSE&quot; |



## Enum: RealtimeUrlCheckModeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;REALTIME_URL_CHECK_MODE_UNSPECIFIED&quot; |
| DISABLED | &quot;REALTIME_URL_CHECK_MODE_DISABLED&quot; |
| ENABLED_MAIN_FRAME | &quot;REALTIME_URL_CHECK_MODE_ENABLED_MAIN_FRAME&quot; |



## Enum: SafeBrowsingProtectionLevelEnum

| Name | Value |
|---- | -----|
| SAFE_BROWSING_PROTECTION_LEVEL_UNSPECIFIED | &quot;SAFE_BROWSING_PROTECTION_LEVEL_UNSPECIFIED&quot; |
| INACTIVE | &quot;INACTIVE&quot; |
| STANDARD | &quot;STANDARD&quot; |
| ENHANCED | &quot;ENHANCED&quot; |



## Enum: ScreenLockSecuredEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SCREEN_LOCK_SECURED_UNSPECIFIED&quot; |
| UNKNOWN | &quot;SCREEN_LOCK_SECURED_UNKNOWN&quot; |
| DISABLED | &quot;SCREEN_LOCK_SECURED_DISABLED&quot; |
| ENABLED | &quot;SCREEN_LOCK_SECURED_ENABLED&quot; |



## Enum: SecureBootModeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SECURE_BOOT_MODE_UNSPECIFIED&quot; |
| UNKNOWN | &quot;SECURE_BOOT_MODE_UNKNOWN&quot; |
| DISABLED | &quot;SECURE_BOOT_MODE_DISABLED&quot; |
| ENABLED | &quot;SECURE_BOOT_MODE_ENABLED&quot; |



## Enum: TriggerEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;TRIGGER_UNSPECIFIED&quot; |
| BROWSER_NAVIGATION | &quot;TRIGGER_BROWSER_NAVIGATION&quot; |
| LOGIN_SCREEN | &quot;TRIGGER_LOGIN_SCREEN&quot; |



