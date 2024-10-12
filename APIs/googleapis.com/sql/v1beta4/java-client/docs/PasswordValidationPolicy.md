

# PasswordValidationPolicy

Database instance local user password validation policy

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**complexity** | [**ComplexityEnum**](#ComplexityEnum) | The complexity of the password. |  [optional] |
|**disallowCompromisedCredentials** | **Boolean** | This field is deprecated and will be removed in a future version of the API. |  [optional] |
|**disallowUsernameSubstring** | **Boolean** | Disallow username as a part of the password. |  [optional] |
|**enablePasswordPolicy** | **Boolean** | Whether the password policy is enabled or not. |  [optional] |
|**minLength** | **Integer** | Minimum number of characters allowed. |  [optional] |
|**passwordChangeInterval** | **String** | Minimum interval after which the password can be changed. This flag is only supported for PostgreSQL. |  [optional] |
|**reuseInterval** | **Integer** | Number of previous passwords that cannot be reused. |  [optional] |



## Enum: ComplexityEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;COMPLEXITY_UNSPECIFIED&quot; |
| DEFAULT | &quot;COMPLEXITY_DEFAULT&quot; |



