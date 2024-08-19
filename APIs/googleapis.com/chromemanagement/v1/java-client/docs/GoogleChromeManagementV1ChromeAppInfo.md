

# GoogleChromeManagementV1ChromeAppInfo

Chrome Web Store app information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**googleOwned** | **Boolean** | Output only. Whether the app or extension is built and maintained by Google. Version-specific field that will only be set when the requested app version is found. |  [optional] [readonly] |
|**isCwsHosted** | **Boolean** | Output only. Whether the app or extension is in a published state in the Chrome Web Store. |  [optional] [readonly] |
|**isExtensionPolicySupported** | **Boolean** | Output only. Whether an app supports policy for extensions. |  [optional] [readonly] |
|**isKioskOnly** | **Boolean** | Output only. Whether the app is only for Kiosk mode on ChromeOS devices |  [optional] [readonly] |
|**isTheme** | **Boolean** | Output only. Whether the app or extension is a theme. |  [optional] [readonly] |
|**kioskEnabled** | **Boolean** | Output only. Whether this app is enabled for Kiosk mode on ChromeOS devices |  [optional] [readonly] |
|**minUserCount** | **Integer** | Output only. The minimum number of users using this app. |  [optional] [readonly] |
|**permissions** | [**List&lt;GoogleChromeManagementV1ChromeAppPermission&gt;**](GoogleChromeManagementV1ChromeAppPermission.md) | Output only. Every custom permission requested by the app. Version-specific field that will only be set when the requested app version is found. |  [optional] [readonly] |
|**siteAccess** | [**List&lt;GoogleChromeManagementV1ChromeAppSiteAccess&gt;**](GoogleChromeManagementV1ChromeAppSiteAccess.md) | Output only. Every permission giving access to domains or broad host patterns. ( e.g. www.google.com). This includes the matches from content scripts as well as hosts in the permissions node of the manifest. Version-specific field that will only be set when the requested app version is found. |  [optional] [readonly] |
|**supportEnabled** | **Boolean** | Output only. The app developer has enabled support for their app. Version-specific field that will only be set when the requested app version is found. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. Types of an item in the Chrome Web Store |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ITEM_TYPE_UNSPECIFIED | &quot;ITEM_TYPE_UNSPECIFIED&quot; |
| EXTENSION | &quot;EXTENSION&quot; |
| OTHERS | &quot;OTHERS&quot; |



