# CloudIdentityApi.BrowserInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browserManagementState** | **String** | Output only. Browser&#39;s management state. | [optional] [readonly] 
**browserVersion** | **String** | Version of the request initiating browser. | [optional] 
**isBuiltInDnsClientEnabled** | **Boolean** | Current state of [built-in DNS client](https://chromeenterprise.google/policies/#BuiltInDnsClientEnabled). | [optional] 
**isBulkDataEntryAnalysisEnabled** | **Boolean** | Current state of [bulk data analysis](https://chromeenterprise.google/policies/#OnBulkDataEntryEnterpriseConnector). Set to true if provider list from Chrome is non-empty. | [optional] 
**isChromeCleanupEnabled** | **Boolean** | Current state of [Chrome Cleanup](https://chromeenterprise.google/policies/#ChromeCleanupEnabled). | [optional] 
**isChromeRemoteDesktopAppBlocked** | **Boolean** | Current state of [Chrome Remote Desktop app](https://chromeenterprise.google/policies/#URLBlocklist). | [optional] 
**isFileDownloadAnalysisEnabled** | **Boolean** | Current state of [file download analysis](https://chromeenterprise.google/policies/#OnFileDownloadedEnterpriseConnector). Set to true if provider list from Chrome is non-empty. | [optional] 
**isFileUploadAnalysisEnabled** | **Boolean** | Current state of [file upload analysis](https://chromeenterprise.google/policies/#OnFileAttachedEnterpriseConnector). Set to true if provider list from Chrome is non-empty. | [optional] 
**isRealtimeUrlCheckEnabled** | **Boolean** | Current state of [real-time URL check](https://chromeenterprise.google/policies/#EnterpriseRealTimeUrlCheckMode). Set to true if provider list from Chrome is non-empty. | [optional] 
**isSecurityEventAnalysisEnabled** | **Boolean** | Current state of [security event analysis](https://chromeenterprise.google/policies/#OnSecurityEventEnterpriseConnector). Set to true if provider list from Chrome is non-empty. | [optional] 
**isSiteIsolationEnabled** | **Boolean** | Current state of [site isolation](https://chromeenterprise.google/policies/?policy&#x3D;IsolateOrigins). | [optional] 
**isThirdPartyBlockingEnabled** | **Boolean** | Current state of [third-party blocking](https://chromeenterprise.google/policies/#ThirdPartyBlockingEnabled). | [optional] 
**passwordProtectionWarningTrigger** | **String** | Current state of [password protection trigger](https://chromeenterprise.google/policies/#PasswordProtectionWarningTrigger). | [optional] 
**safeBrowsingProtectionLevel** | **String** | Current state of [Safe Browsing protection level](https://chromeenterprise.google/policies/#SafeBrowsingProtectionLevel). | [optional] 



## Enum: BrowserManagementStateEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNMANAGED` (value: `"UNMANAGED"`)

* `MANAGED_BY_OTHER_DOMAIN` (value: `"MANAGED_BY_OTHER_DOMAIN"`)

* `PROFILE_MANAGED` (value: `"PROFILE_MANAGED"`)

* `BROWSER_MANAGED` (value: `"BROWSER_MANAGED"`)





## Enum: PasswordProtectionWarningTriggerEnum


* `PASSWORD_PROTECTION_TRIGGER_UNSPECIFIED` (value: `"PASSWORD_PROTECTION_TRIGGER_UNSPECIFIED"`)

* `PROTECTION_OFF` (value: `"PROTECTION_OFF"`)

* `PASSWORD_REUSE` (value: `"PASSWORD_REUSE"`)

* `PHISHING_REUSE` (value: `"PHISHING_REUSE"`)





## Enum: SafeBrowsingProtectionLevelEnum


* `SAFE_BROWSING_LEVEL_UNSPECIFIED` (value: `"SAFE_BROWSING_LEVEL_UNSPECIFIED"`)

* `DISABLED` (value: `"DISABLED"`)

* `STANDARD` (value: `"STANDARD"`)

* `ENHANCED` (value: `"ENHANCED"`)




