# AccessContextManagerApi.OsConstraint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimumVersion** | **String** | The minimum allowed OS version. If not set, any version of this OS satisfies the constraint. Format: &#x60;\&quot;major.minor.patch\&quot;&#x60;. Examples: &#x60;\&quot;10.5.301\&quot;&#x60;, &#x60;\&quot;9.2.1\&quot;&#x60;. | [optional] 
**osType** | **String** | Required. The allowed OS type. | [optional] 
**requireVerifiedChromeOs** | **Boolean** | Only allows requests from devices with a verified Chrome OS. Verifications includes requirements that the device is enterprise-managed, conformant to domain policies, and the caller has permission to call the API targeted by the request. | [optional] 



## Enum: OsTypeEnum


* `OS_UNSPECIFIED` (value: `"OS_UNSPECIFIED"`)

* `DESKTOP_MAC` (value: `"DESKTOP_MAC"`)

* `DESKTOP_WINDOWS` (value: `"DESKTOP_WINDOWS"`)

* `DESKTOP_LINUX` (value: `"DESKTOP_LINUX"`)

* `DESKTOP_CHROME_OS` (value: `"DESKTOP_CHROME_OS"`)

* `ANDROID` (value: `"ANDROID"`)

* `IOS` (value: `"IOS"`)




