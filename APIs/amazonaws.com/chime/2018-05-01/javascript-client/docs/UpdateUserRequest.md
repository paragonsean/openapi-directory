# AmazonChime.UpdateUserRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**licenseType** | **String** | The user license type to update. This must be a supported license type for the Amazon Chime account that the user belongs to. | [optional] 
**userType** | **String** | The user type. | [optional] 
**alexaForBusinessMetadata** | [**UpdateUserRequestAlexaForBusinessMetadata**](UpdateUserRequestAlexaForBusinessMetadata.md) |  | [optional] 



## Enum: LicenseTypeEnum


* `Basic` (value: `"Basic"`)

* `Plus` (value: `"Plus"`)

* `Pro` (value: `"Pro"`)

* `ProTrial` (value: `"ProTrial"`)





## Enum: UserTypeEnum


* `PrivateUser` (value: `"PrivateUser"`)

* `SharedDevice` (value: `"SharedDevice"`)




