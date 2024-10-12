

# UpdateUserRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**licenseType** | [**LicenseTypeEnum**](#LicenseTypeEnum) | The user license type to update. This must be a supported license type for the Amazon Chime account that the user belongs to. |  [optional] |
|**userType** | [**UserTypeEnum**](#UserTypeEnum) | The user type. |  [optional] |
|**alexaForBusinessMetadata** | [**UpdateUserRequestAlexaForBusinessMetadata**](UpdateUserRequestAlexaForBusinessMetadata.md) |  |  [optional] |



## Enum: LicenseTypeEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;Basic&quot; |
| PLUS | &quot;Plus&quot; |
| PRO | &quot;Pro&quot; |
| PRO_TRIAL | &quot;ProTrial&quot; |



## Enum: UserTypeEnum

| Name | Value |
|---- | -----|
| PRIVATE_USER | &quot;PrivateUser&quot; |
| SHARED_DEVICE | &quot;SharedDevice&quot; |



