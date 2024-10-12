

# ContentKeyPolicyPlayReadyLicense

The PlayReady license

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowTestDevices** | **Boolean** | A flag indicating whether test devices can use the license. |  |
|**beginDate** | **OffsetDateTime** | The begin date of license |  [optional] |
|**contentKeyLocation** | [**ContentKeyPolicyPlayReadyContentKeyLocation**](ContentKeyPolicyPlayReadyContentKeyLocation.md) |  |  |
|**contentType** | [**ContentTypeEnum**](#ContentTypeEnum) | The PlayReady content type. |  |
|**expirationDate** | **OffsetDateTime** | The expiration date of license. |  [optional] |
|**gracePeriod** | **String** | The grace period of license. |  [optional] |
|**licenseType** | [**LicenseTypeEnum**](#LicenseTypeEnum) | The license type. |  |
|**playRight** | [**ContentKeyPolicyPlayReadyPlayRight**](ContentKeyPolicyPlayReadyPlayRight.md) |  |  [optional] |
|**relativeBeginDate** | **String** | The relative begin date of license. |  [optional] |
|**relativeExpirationDate** | **String** | The relative expiration date of license. |  [optional] |



## Enum: ContentTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| UNSPECIFIED | &quot;Unspecified&quot; |
| ULTRA_VIOLET_DOWNLOAD | &quot;UltraVioletDownload&quot; |
| ULTRA_VIOLET_STREAMING | &quot;UltraVioletStreaming&quot; |



## Enum: LicenseTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| NON_PERSISTENT | &quot;NonPersistent&quot; |
| PERSISTENT | &quot;Persistent&quot; |



