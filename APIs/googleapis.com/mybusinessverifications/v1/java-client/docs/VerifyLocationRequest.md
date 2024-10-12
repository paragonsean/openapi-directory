

# VerifyLocationRequest

Request message for Verifications.VerifyLocation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**context** | [**ServiceBusinessContext**](ServiceBusinessContext.md) |  |  [optional] |
|**emailAddress** | **String** | Optional. The input for EMAIL method. Email address where the PIN should be sent to. An email address is accepted only if it is one of the addresses provided by FetchVerificationOptions. If the EmailVerificationData has is_user_name_editable set to true, the client may specify a different user name (local-part) but must match the domain name. |  [optional] |
|**languageCode** | **String** | Optional. The BCP 47 language code representing the language that is to be used for the verification process. |  [optional] |
|**mailerContact** | **String** | Optional. The input for ADDRESS method. Contact name the mail should be sent to. |  [optional] |
|**method** | [**MethodEnum**](#MethodEnum) | Required. Verification method. |  [optional] |
|**phoneNumber** | **String** | Optional. The input for PHONE_CALL/SMS method The phone number that should be called or be sent SMS to. It must be one of the phone numbers in the eligible options. |  [optional] |
|**token** | [**VerificationToken**](VerificationToken.md) |  |  [optional] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| VERIFICATION_METHOD_UNSPECIFIED | &quot;VERIFICATION_METHOD_UNSPECIFIED&quot; |
| ADDRESS | &quot;ADDRESS&quot; |
| EMAIL | &quot;EMAIL&quot; |
| PHONE_CALL | &quot;PHONE_CALL&quot; |
| SMS | &quot;SMS&quot; |
| AUTO | &quot;AUTO&quot; |
| VETTED_PARTNER | &quot;VETTED_PARTNER&quot; |



