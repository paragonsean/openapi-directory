# IoEIoTApiToCreateEndUserApplications.User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **String** | Unique identifier of the *Account* | [optional] 
**canLogin** | **Boolean** | true if the user owning the account (can get tokens with /auth/login) | [readonly] [default to false]
**email** | **String** |  | 
**locale** | **String** | Locale identifier (language, region). See https://tools.ietf.org/html/rfc5646 and https://www.iana.org/assignments/lang-subtags-templates/lang-subtags-templates.xhtml .  | 
**metadata** | **{String: Object}** | Keys are limited to the same format as tags (up to 21 characters, [a-z0-9], starting with [a-z]). Values can be any JSON value. | [optional] 
**name** | **String** |  | 
**phoneNumber** | **String** | Phone number of the *User* in international format, for SMS notifications. | [optional] 


