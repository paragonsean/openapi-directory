

# GoogleCloudIdentitytoolkitAdminV2EmailTemplate

Email template. The subject and body fields can contain the following placeholders which will be replaced with the appropriate values: %LINK% - The link to use to redeem the send OOB code. %EMAIL% - The email where the email is being sent. %NEW_EMAIL% - The new email being set for the account (when applicable). %APP_NAME% - The GCP project's display name. %DISPLAY_NAME% - The user's display name.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **String** | Email body |  [optional] |
|**bodyFormat** | [**BodyFormatEnum**](#BodyFormatEnum) | Email body format |  [optional] |
|**customized** | **Boolean** | Output only. Whether the body or subject of the email is customized. |  [optional] [readonly] |
|**replyTo** | **String** | Reply-to address |  [optional] |
|**senderDisplayName** | **String** | Sender display name |  [optional] |
|**senderLocalPart** | **String** | Local part of From address |  [optional] |
|**subject** | **String** | Subject of the email |  [optional] |



## Enum: BodyFormatEnum

| Name | Value |
|---- | -----|
| BODY_FORMAT_UNSPECIFIED | &quot;BODY_FORMAT_UNSPECIFIED&quot; |
| PLAIN_TEXT | &quot;PLAIN_TEXT&quot; |
| HTML | &quot;HTML&quot; |



