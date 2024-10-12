

# GoogleIdentityAccesscontextmanagerV1OsConstraint

A restriction on the OS type and version of devices making requests.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**minimumVersion** | **String** | The minimum allowed OS version. If not set, any version of this OS satisfies the constraint. Format: &#x60;\&quot;major.minor.patch\&quot;&#x60;. Examples: &#x60;\&quot;10.5.301\&quot;&#x60;, &#x60;\&quot;9.2.1\&quot;&#x60;. |  [optional] |
|**osType** | [**OsTypeEnum**](#OsTypeEnum) | Required. The allowed OS type. |  [optional] |
|**requireVerifiedChromeOs** | **Boolean** | Only allows requests from devices with a verified Chrome OS. Verifications includes requirements that the device is enterprise-managed, conformant to domain policies, and the caller has permission to call the API targeted by the request. |  [optional] |



## Enum: OsTypeEnum

| Name | Value |
|---- | -----|
| OS_UNSPECIFIED | &quot;OS_UNSPECIFIED&quot; |
| DESKTOP_MAC | &quot;DESKTOP_MAC&quot; |
| DESKTOP_WINDOWS | &quot;DESKTOP_WINDOWS&quot; |
| DESKTOP_LINUX | &quot;DESKTOP_LINUX&quot; |
| DESKTOP_CHROME_OS | &quot;DESKTOP_CHROME_OS&quot; |
| ANDROID | &quot;ANDROID&quot; |
| IOS | &quot;IOS&quot; |



