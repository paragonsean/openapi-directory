

# MfaSetupStatus

Contains the save-to-send-out information of a MFA-setup

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | Creation date |  |
|**id** | **Long** | ID |  |
|**mfaType** | [**MfaTypeEnum**](#MfaTypeEnum) | Type of second factor authentication |  |
|**name** | **String** | A name to identify the MFA setup by the user. Default is MFA-type followed by a number |  |



## Enum: MfaTypeEnum

| Name | Value |
|---- | -----|
| TOTP | &quot;TOTP&quot; |
| EMERGENCY | &quot;EMERGENCY&quot; |
| U2_F | &quot;U2F&quot; |



