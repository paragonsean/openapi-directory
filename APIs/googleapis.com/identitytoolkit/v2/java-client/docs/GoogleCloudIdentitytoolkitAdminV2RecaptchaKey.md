

# GoogleCloudIdentitytoolkitAdminV2RecaptchaKey

The reCAPTCHA key config. reCAPTCHA Enterprise offers different keys for different client platforms.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** | The reCAPTCHA Enterprise key resource name, e.g. \&quot;projects/{project}/keys/{key}\&quot; |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The client&#39;s platform type. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CLIENT_TYPE_UNSPECIFIED | &quot;CLIENT_TYPE_UNSPECIFIED&quot; |
| WEB | &quot;WEB&quot; |
| IOS | &quot;IOS&quot; |
| ANDROID | &quot;ANDROID&quot; |



