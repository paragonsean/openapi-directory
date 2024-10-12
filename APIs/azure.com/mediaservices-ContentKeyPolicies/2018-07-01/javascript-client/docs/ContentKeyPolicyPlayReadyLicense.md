# AzureMediaServices.ContentKeyPolicyPlayReadyLicense

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowTestDevices** | **Boolean** | A flag indicating whether test devices can use the license. | 
**beginDate** | **Date** | The begin date of license | [optional] 
**contentKeyLocation** | [**ContentKeyPolicyPlayReadyContentKeyLocation**](ContentKeyPolicyPlayReadyContentKeyLocation.md) |  | 
**contentType** | **String** | The PlayReady content type. | 
**expirationDate** | **Date** | The expiration date of license. | [optional] 
**gracePeriod** | **String** | The grace period of license. | [optional] 
**licenseType** | **String** | The license type. | 
**playRight** | [**ContentKeyPolicyPlayReadyPlayRight**](ContentKeyPolicyPlayReadyPlayRight.md) |  | [optional] 
**relativeBeginDate** | **String** | The relative begin date of license. | [optional] 
**relativeExpirationDate** | **String** | The relative expiration date of license. | [optional] 



## Enum: ContentTypeEnum


* `Unknown` (value: `"Unknown"`)

* `Unspecified` (value: `"Unspecified"`)

* `UltraVioletDownload` (value: `"UltraVioletDownload"`)

* `UltraVioletStreaming` (value: `"UltraVioletStreaming"`)





## Enum: LicenseTypeEnum


* `Unknown` (value: `"Unknown"`)

* `NonPersistent` (value: `"NonPersistent"`)

* `Persistent` (value: `"Persistent"`)




