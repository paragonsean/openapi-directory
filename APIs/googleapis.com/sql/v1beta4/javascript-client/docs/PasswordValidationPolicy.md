# CloudSqlAdminApi.PasswordValidationPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complexity** | **String** | The complexity of the password. | [optional] 
**disallowCompromisedCredentials** | **Boolean** | This field is deprecated and will be removed in a future version of the API. | [optional] 
**disallowUsernameSubstring** | **Boolean** | Disallow username as a part of the password. | [optional] 
**enablePasswordPolicy** | **Boolean** | Whether the password policy is enabled or not. | [optional] 
**minLength** | **Number** | Minimum number of characters allowed. | [optional] 
**passwordChangeInterval** | **String** | Minimum interval after which the password can be changed. This flag is only supported for PostgreSQL. | [optional] 
**reuseInterval** | **Number** | Number of previous passwords that cannot be reused. | [optional] 



## Enum: ComplexityEnum


* `UNSPECIFIED` (value: `"COMPLEXITY_UNSPECIFIED"`)

* `DEFAULT` (value: `"COMPLEXITY_DEFAULT"`)




