# NamSorApiV2.FirstLastNamePhoneCodedOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countryIso2** | **String** |  | [optional] 
**firstName** | **String** | The first name (also known as given name) | [optional] 
**id** | **String** |  | [optional] 
**internationalPhoneNumberVerified** | **String** | The normalized phone number, verified using libphonenumber. | [optional] 
**lastName** | **String** | The last name (also known as family name, or surname) | [optional] 
**originCountryIso2** | **String** | The likely country of origin of the name. | [optional] 
**originCountryIso2Alt** | **String** | The best alternative country of origin of the name. | [optional] 
**phoneCountryCode** | **Number** | The phone country code of the phone number, verified using libphonenumber. | [optional] 
**phoneCountryCodeAlt** | **Number** | The best alternative phone country code of the phone number. | [optional] 
**phoneCountryIso2** | **String** | The likely country of the phone number. | [optional] 
**phoneCountryIso2Alt** | **String** | The best alternative country of the phone number. | [optional] 
**phoneCountryIso2Verified** | **String** | The phone ISO2 country code, verified using libphonenumber. | [optional] 
**phoneNumber** | **String** | The input phone number. | [optional] 
**score** | **Number** | Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] 
**script** | **String** |  | [optional] 
**verified** | **Boolean** | Indicates if the phone number could be positively verified using libphonenumber. | [optional] 


