# DataBoxEdgeManagementClient.UserProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryptedPassword** | [**AsymmetricEncryptedSecret**](AsymmetricEncryptedSecret.md) |  | [optional] 
**shareAccessRights** | [**[ShareAccessRight]**](ShareAccessRight.md) | List of shares that the user has rights on. This field should not be specified during user creation. | [optional] 
**userType** | **String** | Type of the user. | 



## Enum: UserTypeEnum


* `Share` (value: `"Share"`)

* `LocalManagement` (value: `"LocalManagement"`)

* `ARM` (value: `"ARM"`)




