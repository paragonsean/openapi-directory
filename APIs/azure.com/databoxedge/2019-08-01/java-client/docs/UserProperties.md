

# UserProperties

The user properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encryptedPassword** | [**AsymmetricEncryptedSecret**](AsymmetricEncryptedSecret.md) |  |  [optional] |
|**shareAccessRights** | [**List&lt;ShareAccessRight&gt;**](ShareAccessRight.md) | List of shares that the user has rights on. This field should not be specified during user creation. |  [optional] |
|**userType** | [**UserTypeEnum**](#UserTypeEnum) | Type of the user. |  |



## Enum: UserTypeEnum

| Name | Value |
|---- | -----|
| SHARE | &quot;Share&quot; |
| LOCAL_MANAGEMENT | &quot;LocalManagement&quot; |
| ARM | &quot;ARM&quot; |



