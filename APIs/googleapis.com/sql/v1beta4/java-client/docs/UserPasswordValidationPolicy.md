

# UserPasswordValidationPolicy

User level password validation policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedFailedAttempts** | **Integer** | Number of failed login attempts allowed before user get locked. |  [optional] |
|**enableFailedAttemptsCheck** | **Boolean** | If true, failed login attempts check will be enabled. |  [optional] |
|**enablePasswordVerification** | **Boolean** | If true, the user must specify the current password before changing the password. This flag is supported only for MySQL. |  [optional] |
|**passwordExpirationDuration** | **String** | Expiration duration after password is updated. |  [optional] |
|**status** | [**PasswordStatus**](PasswordStatus.md) |  |  [optional] |



