# ApiV1.SubmissionDataRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authPhoneNumberHash** | **String** |  | [optional] 
**authProvider** | **String** |  | [optional] 
**authSecondFactorType** | **String** |  | [optional] 
**authSessionIdHash** | **String** |  | [optional] 
**authSessionStartedAt** | **String** |  | [optional] 
**authType** | **String** |  | [optional] 
**authUserIdHash** | **String** |  | [optional] 
**authUsernameHash** | **String** |  | [optional] 
**completedAt** | **String** |  | [optional] 
**email** | **String** |  | 
**fields** | **[String]** |  | 
**id** | **String** |  | 
**ipAddress** | **String** |  | [optional] 
**metadata** | **Object** |  | 
**name** | **String** |  | 
**order** | **Number** |  | 
**sortOrder** | **Number** |  | 
**state** | **String** |  | 
**submissionId** | **String** |  | [optional] 
**userAgent** | **String** |  | [optional] 
**viewedAt** | **String** |  | [optional] 



## Enum: AuthSecondFactorTypeEnum


* `none` (value: `"none"`)

* `phone_number` (value: `"phone_number"`)

* `totp` (value: `"totp"`)

* `mobile_push` (value: `"mobile_push"`)

* `security_key` (value: `"security_key"`)

* `fingerprint` (value: `"fingerprint"`)





## Enum: AuthTypeEnum


* `none` (value: `"none"`)

* `password` (value: `"password"`)

* `oauth` (value: `"oauth"`)

* `email_link` (value: `"email_link"`)

* `phone_number` (value: `"phone_number"`)

* `ldap` (value: `"ldap"`)

* `saml` (value: `"saml"`)





## Enum: StateEnum


* `pending` (value: `"pending"`)

* `completed` (value: `"completed"`)




