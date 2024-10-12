# MyBusinessVerificationsApi.VerifyLocationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**ServiceBusinessContext**](ServiceBusinessContext.md) |  | [optional] 
**emailAddress** | **String** | Optional. The input for EMAIL method. Email address where the PIN should be sent to. An email address is accepted only if it is one of the addresses provided by FetchVerificationOptions. If the EmailVerificationData has is_user_name_editable set to true, the client may specify a different user name (local-part) but must match the domain name. | [optional] 
**languageCode** | **String** | Optional. The BCP 47 language code representing the language that is to be used for the verification process. | [optional] 
**mailerContact** | **String** | Optional. The input for ADDRESS method. Contact name the mail should be sent to. | [optional] 
**method** | **String** | Required. Verification method. | [optional] 
**phoneNumber** | **String** | Optional. The input for PHONE_CALL/SMS method The phone number that should be called or be sent SMS to. It must be one of the phone numbers in the eligible options. | [optional] 
**token** | [**VerificationToken**](VerificationToken.md) |  | [optional] 



## Enum: MethodEnum


* `VERIFICATION_METHOD_UNSPECIFIED` (value: `"VERIFICATION_METHOD_UNSPECIFIED"`)

* `ADDRESS` (value: `"ADDRESS"`)

* `EMAIL` (value: `"EMAIL"`)

* `PHONE_CALL` (value: `"PHONE_CALL"`)

* `SMS` (value: `"SMS"`)

* `AUTO` (value: `"AUTO"`)

* `VETTED_PARTNER` (value: `"VETTED_PARTNER"`)




