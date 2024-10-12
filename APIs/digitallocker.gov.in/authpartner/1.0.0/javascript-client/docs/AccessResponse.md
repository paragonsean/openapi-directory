# AuthorizedPartnerApiSpecification.AccessResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessToken** | **String** | The access token that can be used to call the DigiLocker APIs. | 
**digilockerId** | **String** | A unique 36 character DigiLocker Id of the user account. | 
**dob** | **Number** | This is date of birth of the user as registered with DigiLocker in DDMMYYYY format. | 
**eaadhar** | **String** | This indicates whether eAadhaar data is available for this account. Possible values are Y and N. | 
**expiresIn** | **Number** | The duration in seconds for which the access token is valid | 
**gender** | **String** | This is gender of the user as registered with DigiLocker. The possible values are M, F, T for male, female and transgender respectively. | 
**name** | **String** | The name of the user as registered with DigiLocker. | 
**referenceKey** | **String** | A unique reference of the user account. | 
**refreshToken** | **String** | The refresh token used to refresh the above access token when it expires. Please refer to Refresh Access Token API for more details. | 
**scope** | **String** | Scope of the token. | 
**tokenType** | **String** | The type of token which will always be Bearer. | 



## Enum: EaadharEnum


* `Y` (value: `"Y"`)

* `N` (value: `"N"`)





## Enum: GenderEnum


* `M` (value: `"M"`)

* `F` (value: `"F"`)

* `T` (value: `"T"`)




