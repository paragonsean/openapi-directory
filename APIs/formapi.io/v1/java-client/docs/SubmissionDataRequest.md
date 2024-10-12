

# SubmissionDataRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authPhoneNumberHash** | **String** |  |  [optional] |
|**authProvider** | **String** |  |  [optional] |
|**authSecondFactorType** | [**AuthSecondFactorTypeEnum**](#AuthSecondFactorTypeEnum) |  |  [optional] |
|**authSessionIdHash** | **String** |  |  [optional] |
|**authSessionStartedAt** | **String** |  |  [optional] |
|**authType** | [**AuthTypeEnum**](#AuthTypeEnum) |  |  [optional] |
|**authUserIdHash** | **String** |  |  [optional] |
|**authUsernameHash** | **String** |  |  [optional] |
|**completedAt** | **String** |  |  [optional] |
|**email** | **String** |  |  |
|**fields** | **List&lt;String&gt;** |  |  |
|**id** | **String** |  |  |
|**ipAddress** | **String** |  |  [optional] |
|**metadata** | **Object** |  |  |
|**name** | **String** |  |  |
|**order** | **Integer** |  |  |
|**sortOrder** | **Integer** |  |  |
|**state** | [**StateEnum**](#StateEnum) |  |  |
|**submissionId** | **String** |  |  [optional] |
|**userAgent** | **String** |  |  [optional] |
|**viewedAt** | **String** |  |  [optional] |



## Enum: AuthSecondFactorTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| PHONE_NUMBER | &quot;phone_number&quot; |
| TOTP | &quot;totp&quot; |
| MOBILE_PUSH | &quot;mobile_push&quot; |
| SECURITY_KEY | &quot;security_key&quot; |
| FINGERPRINT | &quot;fingerprint&quot; |



## Enum: AuthTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| PASSWORD | &quot;password&quot; |
| OAUTH | &quot;oauth&quot; |
| EMAIL_LINK | &quot;email_link&quot; |
| PHONE_NUMBER | &quot;phone_number&quot; |
| LDAP | &quot;ldap&quot; |
| SAML | &quot;saml&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| COMPLETED | &quot;completed&quot; |



