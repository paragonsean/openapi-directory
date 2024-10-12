

# BrowserInfo

Browser-specific fields reported by the Endpoint Verification extension. LINT.IfChange

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**browserManagementState** | [**BrowserManagementStateEnum**](#BrowserManagementStateEnum) | Output only. Browser&#39;s management state. |  [optional] [readonly] |
|**browserVersion** | **String** | Version of the request initiating browser. |  [optional] |
|**isBuiltInDnsClientEnabled** | **Boolean** | Current state of [built-in DNS client](https://chromeenterprise.google/policies/#BuiltInDnsClientEnabled). |  [optional] |
|**isBulkDataEntryAnalysisEnabled** | **Boolean** | Current state of [bulk data analysis](https://chromeenterprise.google/policies/#OnBulkDataEntryEnterpriseConnector). Set to true if provider list from Chrome is non-empty. |  [optional] |
|**isChromeCleanupEnabled** | **Boolean** | Current state of [Chrome Cleanup](https://chromeenterprise.google/policies/#ChromeCleanupEnabled). |  [optional] |
|**isChromeRemoteDesktopAppBlocked** | **Boolean** | Current state of [Chrome Remote Desktop app](https://chromeenterprise.google/policies/#URLBlocklist). |  [optional] |
|**isFileDownloadAnalysisEnabled** | **Boolean** | Current state of [file download analysis](https://chromeenterprise.google/policies/#OnFileDownloadedEnterpriseConnector). Set to true if provider list from Chrome is non-empty. |  [optional] |
|**isFileUploadAnalysisEnabled** | **Boolean** | Current state of [file upload analysis](https://chromeenterprise.google/policies/#OnFileAttachedEnterpriseConnector). Set to true if provider list from Chrome is non-empty. |  [optional] |
|**isRealtimeUrlCheckEnabled** | **Boolean** | Current state of [real-time URL check](https://chromeenterprise.google/policies/#EnterpriseRealTimeUrlCheckMode). Set to true if provider list from Chrome is non-empty. |  [optional] |
|**isSecurityEventAnalysisEnabled** | **Boolean** | Current state of [security event analysis](https://chromeenterprise.google/policies/#OnSecurityEventEnterpriseConnector). Set to true if provider list from Chrome is non-empty. |  [optional] |
|**isSiteIsolationEnabled** | **Boolean** | Current state of [site isolation](https://chromeenterprise.google/policies/?policy&#x3D;IsolateOrigins). |  [optional] |
|**isThirdPartyBlockingEnabled** | **Boolean** | Current state of [third-party blocking](https://chromeenterprise.google/policies/#ThirdPartyBlockingEnabled). |  [optional] |
|**passwordProtectionWarningTrigger** | [**PasswordProtectionWarningTriggerEnum**](#PasswordProtectionWarningTriggerEnum) | Current state of [password protection trigger](https://chromeenterprise.google/policies/#PasswordProtectionWarningTrigger). |  [optional] |
|**safeBrowsingProtectionLevel** | [**SafeBrowsingProtectionLevelEnum**](#SafeBrowsingProtectionLevelEnum) | Current state of [Safe Browsing protection level](https://chromeenterprise.google/policies/#SafeBrowsingProtectionLevel). |  [optional] |



## Enum: BrowserManagementStateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNMANAGED | &quot;UNMANAGED&quot; |
| MANAGED_BY_OTHER_DOMAIN | &quot;MANAGED_BY_OTHER_DOMAIN&quot; |
| PROFILE_MANAGED | &quot;PROFILE_MANAGED&quot; |
| BROWSER_MANAGED | &quot;BROWSER_MANAGED&quot; |



## Enum: PasswordProtectionWarningTriggerEnum

| Name | Value |
|---- | -----|
| PASSWORD_PROTECTION_TRIGGER_UNSPECIFIED | &quot;PASSWORD_PROTECTION_TRIGGER_UNSPECIFIED&quot; |
| PROTECTION_OFF | &quot;PROTECTION_OFF&quot; |
| PASSWORD_REUSE | &quot;PASSWORD_REUSE&quot; |
| PHISHING_REUSE | &quot;PHISHING_REUSE&quot; |



## Enum: SafeBrowsingProtectionLevelEnum

| Name | Value |
|---- | -----|
| SAFE_BROWSING_LEVEL_UNSPECIFIED | &quot;SAFE_BROWSING_LEVEL_UNSPECIFIED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| STANDARD | &quot;STANDARD&quot; |
| ENHANCED | &quot;ENHANCED&quot; |



