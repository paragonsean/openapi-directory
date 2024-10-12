

# RequestPhoneVerificationRequest

Request message for the RequestPhoneVerification method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**languageCode** | **String** | Language code [IETF BCP 47 syntax](https://tools.ietf.org/html/bcp47) (for example, en-US). Language code is used to provide localized &#x60;SMS&#x60; and &#x60;PHONE_CALL&#x60;. Default language used is en-US if not provided. |  [optional] |
|**phoneNumber** | **String** | Phone number to be verified. |  [optional] |
|**phoneRegionCode** | **String** | Required. Two letter country code for the phone number, for example &#x60;CA&#x60; for Canadian numbers. See the [ISO 3166-1 alpha-2](https://wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) officially assigned codes. |  [optional] |
|**phoneVerificationMethod** | [**PhoneVerificationMethodEnum**](#PhoneVerificationMethodEnum) | Verification method to receive verification code. |  [optional] |



## Enum: PhoneVerificationMethodEnum

| Name | Value |
|---- | -----|
| PHONE_VERIFICATION_METHOD_UNSPECIFIED | &quot;PHONE_VERIFICATION_METHOD_UNSPECIFIED&quot; |
| SMS | &quot;SMS&quot; |
| PHONE_CALL | &quot;PHONE_CALL&quot; |



